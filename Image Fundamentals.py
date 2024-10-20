import random

import cv2


img = cv2.imread('assets/marvel 1.png', -1)

print(type(img))# <class 'numpy.ndarray'>
print(img.shape)# (300, 300, 3)
# Regular - RGB open cv - BGR

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255) , random.randint(0,255) , random.randint(0,255)]

cv2.imshow('Image ' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
