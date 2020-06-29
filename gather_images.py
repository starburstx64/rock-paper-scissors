desc = '''Script to gather data images with a particular label.

Usage: python gather_images.py <label_name> <num_samples>

The script will collect <num_samples> number of images and store them
in its own directory.

Only the portion of the image within the box displayed
will be captured and stored.

Press 'a' to start/pause the image collecting process.
Press 'q' to quit.

'''

import cv2
import os
from utils.cv_resolution import set_res


def gather_images(label_name, num_samples, train):
    IMG_SAVE_PATH = ('image_data\\train', 'image_data\\test')[train]
    IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name.lower())

    try:
        os.mkdir(IMG_SAVE_PATH)
    except FileExistsError:
        pass
    try:
        os.mkdir(IMG_CLASS_PATH)
    except FileExistsError:
        print("{} directory already exists.".format(IMG_CLASS_PATH))
        print("All images gathered will be saved along with existing items in this folder")

    cap = cv2.VideoCapture(0)
    set_res(cap, 1224, 768)

    start = False
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        if count == num_samples:
            break

        cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

        if start:
            roi = frame[100:500, 100:500]
            save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
            cv2.imwrite(save_path, roi)
            count += 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Collecting {}".format(count),
                    (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Collecting images", frame)

        k = cv2.waitKey(10)
        if k == ord('a'):
            start = not start

        if k == ord('q'):
            break

    print("\n{} image(s) saved to {}".format(count, IMG_CLASS_PATH))
    cap.release()
    cv2.destroyAllWindows()
