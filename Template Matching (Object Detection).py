import numpy as np
import cv2

# Read and resize the main image
img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.6, fy=0.6)
# Read and resize the template
template = cv2.resize(cv2.imread('assets/ball.PNG', 0), (0, 0), fx=0.6, fy=0.6)
h, w = template.shape

# List of template matching methods
methods = [
    cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED
]

for method in methods:
    img2 = img.copy()
    # Apply template matching
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Determine the top-left corner of the matched region
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # Determine the bottom-right corner of the matched region
    bottom_right = (location[0] + w, location[1] + h)
    # Draw a rectangle around the matched region
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    # Display the result
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
