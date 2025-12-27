import cv2
import os

# ================= CONFIG =================
IMAGES_DIR = "images"
LABELS_DIR = "labels"
CLASS_ID = 0        # ball
BOX_SIZE = 28       # pixels
IMAGE_EXTS = (".jpg", ".jpeg", ".png")
# ==========================================

os.makedirs(LABELS_DIR, exist_ok=True)

clicked = False
skip = False
click_x, click_y = -1, -1

def mouse_callback(event, x, y, flags, param):
    global clicked, click_x, click_y, img, h, w, img_name
    if event == cv2.EVENT_LBUTTONDOWN and not clicked:
        clicked = True
        click_x, click_y = x, y

        xc = click_x / w
        yc = click_y / h
        bw = BOX_SIZE / w
        bh = BOX_SIZE / h

        label_path = os.path.join(
            LABELS_DIR, os.path.splitext(img_name)[0] + ".txt"
        )

        with open(label_path, "w") as f:
            f.write(f"{CLASS_ID} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

        print(f"[SAVED] labels/{os.path.splitext(img_name)[0]}.txt")

        cv2.rectangle(
            img,
            (click_x - BOX_SIZE // 2, click_y - BOX_SIZE // 2),
            (click_x + BOX_SIZE // 2, click_y + BOX_SIZE // 2),
            (0, 255, 0), 2
        )
        cv2.imshow("Annotator", img)
        cv2.waitKey(150)
        cv2.destroyAllWindows()

image_files = sorted([
    f for f in os.listdir(IMAGES_DIR)
    if f.lower().endswith(IMAGE_EXTS)
])

print(f"[INFO] Found {len(image_files)} images")

for img_name in image_files:
    img_path = os.path.join(IMAGES_DIR, img_name)
    img = cv2.imread(img_path)

    if img is None:
        print(f"[WARNING] Could not read {img_name}")
        continue

    h, w = img.shape[:2]
    clicked = False
    skip = False

    cv2.namedWindow("Annotator", cv2.WINDOW_NORMAL)
    cv2.imshow("Annotator", img)
    cv2.setMouseCallback("Annotator", mouse_callback)

    print(f"[INFO] {img_name} | Click = label | S = skip")

    while not clicked and not skip:
        key = cv2.waitKey(20) & 0xFF

        if key == ord('s'):   # press 's' to skip
            skip = True
            print("[SKIPPED] No label saved")
            cv2.destroyAllWindows()

        elif key == 27:       # ESC also skip
            skip = True
            print("[SKIPPED - ESC]")
            cv2.destroyAllWindows()

print("\n[DONE] Annotation finished.")
