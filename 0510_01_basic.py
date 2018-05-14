import cv2

# 입력파일 지정하기

image_file = "C:/Users/Student/Desktop/dna1.jpg"

# 출력파일 이름지정하기
output_file = "C:/Users/Student/Desktop/dna_face.jpg"

# 케스케이드 파일의 경로 지정하기
cascade_file = "C:/Users/Student/Desktop/haarcascade_frontface.xml"

# 이미지 읽어 들이기
image = cv2.imread(image_file)
#
# # 그레이 스케일로 변환하기
image_gs = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#
# # 얼굴 인식 전용 캐스케이드 파일 읽어 들이기
cascade = cv2.CascadeClassifier(cascade_file)




# 얼굴 인식 실행하기

face_list = cascade.detectMultiScale(image_gs,scaleFactor=1.1,minNeighbors=1)


if len(face_list)>0:
    print(face_list)
    color = (255,0,0)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image,(x,y),(x+w,y+h),color,thickness=2)
    cv2.imwrite(output_file,image)
    cv2.imshow("img", cv2.imread("C:/Users/Student/desktop/dna_face.jpg"))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("no face")