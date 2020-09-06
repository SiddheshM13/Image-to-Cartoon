import cv2
import os
import numpy as np

def cartoonify(img_rgb):
    numBilateralFilters = 4
    img_color = img_rgb
    frame= np.uint8(img_rgb)


    for _ in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 15, 30, 20)

        
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)
        
        img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 11, 2)

    
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    
    return cv2.bitwise_and(img_color, img_edge)

real_inputs = []

cartoon_outputs = []

img_rgb = cv2.imread("img.jpg")

output = cartoonify(img_rgb)

real_inputs.append(img_rgb)

cartoon_outputs.append(output)

cv2.imwrite('finalframe.jpg', output)
cv2.waitKey(0) 

