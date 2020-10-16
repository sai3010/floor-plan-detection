import numpy as np
import cv2
import pytesseract
image = cv2.imread('img1.png')
# img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurry = cv2.GaussianBlur(image,(5,5),0)
hsv = cv2.cvtColor(blurry, cv2.COLOR_BGR2HSV)

# red wifi color
low_red = np.array([161,155,84])
high_red = np.array([179,255,255])
mask = cv2.inRange(hsv, low_red, high_red)
cv2.imwrite("wifi.png", mask) 
# image = cv2.imread('wifi.png')

# imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(mask,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# for c in contours:
#     # print(cv2.contourArea(c))
#     if cv2.contourArea(c) >= 300 :
#         img = cv2.drawContours(image, c, -1, (0,255,0), 3)
#         x,y,w,h = cv2.boundingRect(c)
#         cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255,0), 2)
#         center = (x,y)
#         print (center)
#         cv2.imshow("images", img)
#         c = cv2.waitKey(0)


# img = cv2.drawContours(image, contours, -1, (0,255,0), 3)

# blue color
low_blue = np.array([94,80,2])
high_blue = np.array([126,255,255])
mask = cv2.inRange(hsv, low_blue, high_blue)
ret,thresh = cv2.threshold(mask,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.drawContours(image, contours, -1, (0,255,0), 3)
# for c in contours:
#     # print(cv2.contourArea(c))
#     if cv2.contourArea(c) >= 400 :
#         img = cv2.drawContours(image, c, -1, (0,255,0), 3)
#         x,y,w,h = cv2.boundingRect(c)
#         cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255,0), 2)
#         center = (x,y)
#         print (center)
#         cv2.imshow("images", img)
#         c = cv2.waitKey(0)

# black color
low_black = np.array([0,5,50])
high_black = np.array([179, 50, 255])
mask = cv2.inRange(hsv, low_black, high_black)


ret,thresh = cv2.threshold(mask,255,255,255)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.drawContours(image, contours, -1, (0,255,0), 3)

for c in contours:
    
    if cv2.contourArea(c) >8 and  cv2.contourArea(c) < 15 :
        print(cv2.contourArea(c))
        img = cv2.drawContours(image, c, -1, (0,255,0), 3)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255,0), 2)
        center = (x,y)
        # print (center)
        cv2.imshow("images", img)
        c = cv2.waitKey(0)
        
# cv2.imshow("images", img)
# cv2.imshow("images", mask)


# c = cv2.waitKey(0)
# c.destroyAllWindows()
