import cv2


img = cv2.imread('assets/marvel 1.png', 1)
img =cv2.resize(img , (300,300)) # in pixel
cv2.imwrite('assets/marvel 1.png' , img)

# -1 , cv2.IMREAD_COLOR : Loads a color image . Any transparency of image will be neglected. It is the default flag
# 0 , cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1 , cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

cv2.imshow('Image ', img)
cv2.waitKey(0)# ex 1 seconds mean 1 second pa chi jatu reshe
cv2.destroyAllWindows()