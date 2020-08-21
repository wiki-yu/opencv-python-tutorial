import numpy as np
import cv2

# RGB color space describes colors in terms of the amount of red, green, and blue present.
# HSV color space describes colors in terms of the Hue, Saturation, and Value.
# Hue represents the color type.
# Saturation represents the vibrancy of the color. The lower, the more gray is present in the color.
# Value represents the brightness of the color, with 0 being completely dark and 255 being fully bright.
# As for OpenCV, For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

# pass the BGR values to find HSV values
green = np.uint8([[[0, 255, 0 ]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)
# We would get [[[ 60 255 255]]] for green
# We can take [H-10, 100,100] and [H+10, 255, 255] as lower/upper bound

img = cv2.imread("./images/color_space.png")
cv2.imshow("image", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

lower_blue=np.array([110, 100, 100]) #blue
upper_blue=np.array([130, 255, 255])

lower_green=np.array([60, 100, 100]) #green
upper_green=np.array([70, 255, 255])

lower_red=np.array([0, 100, 100]) #red
upper_red=np.array([10, 255, 255])

# Threshold the HSV image to get specific colors
red_mask = cv2.inRange(hsv, lower_red, upper_red)
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
green_mask = cv2.inRange(hsv, lower_green, upper_green)

red_img = cv2.bitwise_and(img, img, mask=red_mask) #对原图像处理
green_img = cv2.bitwise_and(img, img, mask=green_mask)
blue_img = cv2.bitwise_and(img, img, mask=blue_mask)

res = green_img + red_img + blue_img
cv2.imshow("red", red_img)
cv2.imshow("blue", blue_img)
cv2.imshow("green", green_img)
cv2.imshow("res", res)
cv2.waitKey(0)
