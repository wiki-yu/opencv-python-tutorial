import cv2
import numpy as np

# Arithmetic Operations like Addition, Subtraction, and Bitwise Operations(AND, OR, NOT, XOR).
# Both images should be of equal size and depth.
# Function cv2.add() directly adds up image pixels in the two images.
img1 = cv2.imread("./images/image1.jpg", 0)
img2 = cv2.imread("./images/image2.jpg", 0)
img = cv2.add(img1, img2)
# print(img1)
# print("**************************")
# print(img2)
# print("**************************")
# print(img)

# Function: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue), adds up using the weights
weighted_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow("Weighted Image", weighted_img)
cv2.imshow("add", img)
# print(img1)
# print("**************************")
# print(img2)
# print("**************************")
# print(weighted_img)


sub_img = cv2.subtract(img1, img2)
cv2.imshow("subtract", sub_img)
cv2.waitKey(0)