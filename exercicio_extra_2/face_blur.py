# import the necessary packages
import argparse
import imutils
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
ap.add_argument("-c", "--cascade", type=str,
	default="cascade/haarcascade_frontalface_default.xml",
	help="path to haar cascade face detector")
args = vars(ap.parse_args())

# load the haar cascade face detector from
print("[INFO] loading face detector...")
detector = cv2.CascadeClassifier(args["cascade"])
# load the input image from disk, resize it, and convert it to
# grayscale
#TODO

# detect faces in the input image using the haar cascade face
# detector
print("[INFO] performing face detection...")
#TODO
print("[INFO] {} faces detected...".format(len(rects)))
# loop over the bounding boxes
for (x, y, w, h) in rects:
	# draw the face bounding box on the image
	# TODO
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)

# bluring image
h, w = image.shape[:2]
kernel_width = (w // 7) | 1
kernel_height = (h // 7) | 1
for (x, y, w, h) in rects:
    # getting face.
    face = image[y: y+h, x: x+w]
    # apply gaussian blur to this face
	# TODO
    # put the blurred face into the original image
	# TODO
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
