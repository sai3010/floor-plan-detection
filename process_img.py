import numpy as np
import cv2

# importing the image through opencv
image = cv2.imread('img.png')
# using GaussianBlur to remove noise from the image
blurry = cv2.GaussianBlur(image,(5,5),0)
# Converting to HSV for object detection
hsv = cv2.cvtColor(blurry, cv2.COLOR_BGR2HSV)

wifi_area = ["Manager's office","Office Area B","Waiting Room","Lift lobby","Conference Room","Office Area A"]
ble_area = ["Manager's office","Office Area B","Office Area A","Conference Room"]

def wifi(dev_id):
    wifi_list =[]
    # specifying the uppper and lower range of red colour.
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    # detecting the boundary 
    mask = cv2.inRange(hsv, low_red, high_red)
    ret,thresh = cv2.threshold(mask,127,255,0)
    # finding white objects in black bg using contours
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    j=0
    for c in contours:
        if cv2.contourArea(c) >= 300 :
            img = cv2.drawContours(image, c, -1, (0,255,0), 3)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255,0), 2)
            center = (x,y)
            wifi_list.append({"ID":j,"Co-ordinates":{"x":x,"y":y},"Location":wifi_area[j]})
            j=j+1
    if dev_id and int(dev_id)<len(wifi_list):
        return wifi_list[int(dev_id)]
    return wifi_list

def ble(dev_id):
    ble_list =[]
    # specifying the uppper and lower range of red colour.
    low_blue = np.array([94,80,2])
    high_blue = np.array([126,255,255])
    # detecting the boundary 
    mask = cv2.inRange(hsv, low_blue, high_blue)
    ret,thresh = cv2.threshold(mask,127,255,0)
    # finding white objects in black bg using contours
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    j=0
    for c in contours:
        if cv2.contourArea(c) >= 400 :
            img = cv2.drawContours(image, c, -1, (0,255,0), 3)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255,0), 2)
            center = (x,y)
            ble_list.append({"ID":j,"Co-ordinates":{"x":x,"y":y},"Location":ble_area[j]})
            j=j+1
    if dev_id and int(dev_id)<len(ble_list):
        return ble_list[int(dev_id)]
    return ble_list
