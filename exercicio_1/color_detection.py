import numpy as np
import argparse
import cv2


limites_bgr = {
    "coca": [(20, 20, 140), (50, 50, 255)],
    "pepsi": [(120, 40, 40), (255, 80, 80)],
    "guarana": [(30, 50, 10), (40, 255, 60)]
}

def read_image(path):
    pass

def apply_mask(image, lower, upper, draw_bb=True):
    if draw_bb:
        output = cv2.rectangle(image, tuple(top_left), tuple(bottom_right), (0,0,0), 2)
    else:
        output = cv2.bitwise_and(image, image, mask = mask)
    return output

def show_image(image, name="mini_curso"):
    cv2.imshow(name, cv2.resize(image, (720, 480)))
    cv2.waitKey(0)

def run_bgr(path, refri):
    image = read_image(path)
    image = apply_mask(image, limites_bgr[refri][0], limites_bgr[refri][1])
    show_image(image)

if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "path to the image")
    ap.add_argument("-r", "--refri", help = "refri to detect <coca | pepsi | guarana>")
    args = vars(ap.parse_args())

    run_bgr(args["image"], args["refri"])
