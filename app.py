import cv2 as cv


cam = cv.VideoCapture(0)
while True:
    _,img = cam.read()
    img = cv.flip(img,1)
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)


    #  rgb color extraction  
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]

#  hsv color extraction    

    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]


    cv.imshow("frame", img)
    cv.imshow("red", r)
    cv.imshow("green", g)
    cv.imshow("blue", b)
    cv.imshow("HSV", hsv)
    cv.imshow("hue", h)
    cv.imshow("saturation", s)
    cv.imshow("value", v)

    key = cv.waitKey(1)
    if key == 27:
        cam.release()
        break




