import numpy as np
import cv2

# Common arguments as given below
# img : The image where you want to draw the shapes
# color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
# thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
# lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1) # -1 means not hollow but concrete
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 255, 255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("shape", img)
cv2.waitKey(0)