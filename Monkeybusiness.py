import cv2
cap = cv2.VideoCapture('http://24.213.59.14:80')

object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    mask = object_detector.apply(frame)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitkey(30)
    if key ==27:
        break

    cap.release()
    cv2.destroyAllWindows()
