import cv2

cap = cv2.VideoCapture("c:/Users/Student/desktop/dna.mp4")
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow("FACE")

#haar코드 사용 > 어떤 파일을 쓰느냐에 따라 인식할 객체가 달라짐
face_cascade = cv2.CascadeClassifier("C:/Users/Student/Desktop/haarcascade_frontface.xml")

while(True):
    # 카메라에서 이미지 얻기
    ret, frame = cap.read()
    # cv2.imshow('FACE', frame)
    #gray로 변환!
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #
    # # gray로 변환된 이미지를 cascade를 이용하여 detect
    faces = face_cascade.detectMultiScale(grayframe,1.8,2,0,(30,30))
    #
    # # 얼굴을 인식하는 사각프레임에 대한 내용
    # # 얼굴을 인식하는 사각프레임에 넣을 글자내용
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3,4,0)
        cv2.putText(frame,'face',(x-5,y-5),font,0.9,(255,255,0),2)

    # face로 정의된 프레임을 보여준다.

    cv2.imshow('FACE', frame)
    if cv2.waitKey(30)>=0:
        continue

    if cv2.waitKey(1)!=255:
        continue
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()