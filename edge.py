import cv2 as cv
cam = cv.VideoCapture(0)
while True:
    _, img = cam.read()
    img = cv.flip(img,1)
    edge1 = cv.Canny(img,100,200)
    edge2 = cv.Canny(img,200,300) 
    edge3 = cv.Canny(img,300,400)

    cv.imshow("frame", img)
    cv.imshow("egde1", edge1)
    cv.imshow("edge2", edge2)
    cv.imshow("edge3", edge3)
    key = cv.waitKey(1)
    if key == 27:
        cam.release()
        break

    if(key ==13):
        cv.imwrite("selfie.jpg",img)
        cam.release()
        break
