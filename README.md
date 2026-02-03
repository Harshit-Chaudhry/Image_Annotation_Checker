# YOLO Annotation Review Tool

This script is a simple OpenCV-based utility for **manually reviewing YOLO-format bounding box annotations**. It displays each image with its bounding boxes drawn and lets you quickly **accept or reject** annotations using the keyboard.

Accepted and rejected images are logged to separate text files for later use (e.g., dataset cleanup, retraining, or auditing).

---

## Features

- 📦 Supports YOLO `.txt` label format (`class x_center y_center width height`)
- 🖼️ Displays images with bounding boxes and class IDs
- ⌨️ Keyboard-based review:
  - **`a`** → accept image
  - **`r`** → reject image

- 📝 Logs accepted and rejected image paths to text files
- 🚫 Skips images with missing or empty label files

---

## Directory Structure

Expected directory layout:

```
data/
└── test/
    ├── images/
    │   ├── img1.jpg
    │   ├── img2.png
    │   └── ...
    └── labels/
        ├── img1.txt
        ├── img2.txt
        └── ...
```

Each image must have a corresponding label file with the same base name.

---

## YOLO Label Format

Each line in a label file should be:

```
<class_id> <x_center> <y_center> <width> <height>
```

All coordinates are **normalized** (values between 0 and 1).

Example:

```
0 0.512 0.481 0.234 0.317
```

---

## Output Files

- `accepted.txt` → paths of images you approve
- `rejected.txt` → paths of images you reject

Each entry is written as an absolute or relative image path (based on how the script is run).

---

## Requirements

- Python 3.11
- OpenCV

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script:

```bash
python checkers.py
```

For each image:

1. The image is displayed with bounding boxes
2. Check annotation quality
3. Press:
   - **`a`** to accept
   - **`r`** to reject

The window closes automatically and moves to the next image.
