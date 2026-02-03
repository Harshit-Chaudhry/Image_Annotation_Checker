import os
import cv2


images_dir = "data/test/images"
labels_dir = "data/test/labels"
accepted_file = "accepted.txt"
rejected_file = "rejected.txt"


def draw_yolo_boxes(img_path, label_path):
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    with open(label_path) as f:
        for line in f:
            cls, xc, yc, bw, bh = map(float, line.split())   # cls, xc, yc, bw, bh = map(float, line.split())[:5]

            x1 = int((xc - bw / 2) * w)
            y1 = int((yc - bh / 2) * h)
            x2 = int((xc + bw / 2) * w)
            y2 = int((yc + bh / 2) * h)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(img, str(int(cls)), (x1, y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    return img


for img_name in os.listdir(images_dir):
    if not img_name.lower().endswith(('.jpg', '.jpeg','.png')):
        continue

    base = os.path.splitext(img_name)[0]
    label_path = os.path.join(labels_dir, base + ".txt")
    img_path = os.path.join(images_dir, img_name)

    if not os.path.exists(label_path) or os.path.getsize(label_path) == 0:
        continue

    img = draw_yolo_boxes(img_path, label_path)

    # Display
    cv2.imshow(f"Annotation Review - {img_name}", img)
    print(f"Reviewing: {img_name} | Press 'a' = Accept, 'r' = Reject")
    key = cv2.waitKey(0) & 0xFF

    if key == ord('a'):
        with open(accepted_file, "a") as f:
            f.write(img_path + "\n")
    elif key == ord('r'):
        with open(rejected_file, "a") as f:
            f.write(img_path + "\n")
    cv2.destroyAllWindows()