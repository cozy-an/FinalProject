import cv2

dna = cv2.VideoCapture("C:/Users/Student/desktop/dna.mp4")
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow("FACE")
face_cascade = cv2.CascadeClassifier("C:/Users/Student/desktop/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Users/Student/desktop/haarcascade_eye.xml")

while(True):
    ret, frame = dna.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame, 'FACE', (x - 5, y - 5), font, 0.9, (255, 21, 0), 2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(25,126,10),2)
            cv2.putText(frame, 'EYE', (x - 1, y - 1), font, 0.5, (100, 25, 10), 2)
        cv2.imshow('FACE', frame)
        if cv2.waitKey(30) >= 0:
            continue

        if cv2.waitKey(1) != 255:
            continue
cap.release()
cv2.destroyAllWindows()
