import matplotlib.pyplot as plt
import cv2

x = cv2.imread("data/FROM_kinect.jpg")
y = x[51:251,239:439]

print(x.shape)

plt.imshow(y)
plt.show()