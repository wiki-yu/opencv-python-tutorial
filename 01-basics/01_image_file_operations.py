import cv2

# Read the image keeping all the channels
img = cv2.imread("./images/lenna.png")

# Read the image keeping just one channel
img_gray = cv2.imread("./images/lenna.png", 0)
cv2.imshow("original", img)
cv2.imshow("gray", img_gray)

# Display a frame for 1000 ms, if 0 then waits for user to press any key
cv2.waitKey(1000)
# Using cv2.imwrite() method saving the image
cv2.imwrite("./images/lenna_gray.png", img_gray)
