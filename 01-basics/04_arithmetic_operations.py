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
cv2.waitKey(2000)
cv2.destroyAllWindows()

image1 = cv2.imread("./images/input1.jpg")
image2 = cv2.imread("./images/input2.jpg")
and_image = cv2.bitwise_and(image1, image2, mask=None)
or_image = cv2.bitwise_or(image1, image2, mask=None)
xor_image = cv2.bitwise_xor(image1, image2, mask=None)
inverse_image = cv2.bitwise_not(image1, mask=None)
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("bitwise and", and_image)
cv2.imshow("bitwise or", or_image)
cv2.imshow("bitwise xor", xor_image)
cv2.imshow("bitwise not", inverse_image)
cv2.waitKey(0)

# Piexel value operations
# Get the image properties
img = cv2.imread("./images/lenna.png")
print("Image shape: {}, size: {}, type: {}".format(img.shape, img.size, img.dtype))
# Access and modify pixel values
px = img[50, 50]
print(px)
blue = img[50, 50, 0]
print(blue)
img[50, 50] = [255,255,255]
print(img[50, 50])
# Better way to access and modify pixel values
print(img.item(50, 50, 1))
img.itemset((50, 50, 1), 100)
print(img.item(50, 50, 1))

x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))
print(x + y)