import cv2
import numpy as np
width, height = 8, 8
image = np.zeros((height, width), dtype=np.uint8)
for row in range(height):
    for col in range(width):
        if (row + col) % 2 == 0:
            image[row, col] = 255
resized_image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_NEAREST)
cv2.imshow("Checkerboard", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
