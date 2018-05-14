import cv2
import argparse
import io
import time
import json

from google.cloud import vision

def video2frame(video,save_path):
    vidcap = cv2.VideoCapture(video)
    count = 0;
    while True:
        success,image = vidcap.read()
        if not success:
            break


        print('Read a new Frame : ',success)
        fname = "{}.jpg".format("{0:05d}".format(count))
        cv2.imwrite(save_path+fname,image)
        detect_faces(save_path+fname)
        time.sleep(1)

        count +=1
    print("{} images are extracted in {}.".format(count,save_path))




# [START def_detect_faces]
def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    # [START migration_face_detection]
    # [START migration_image_file]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    # [END migration_image_file]

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
    # [END migration_face_detection]
# [END def_detect_faces]





video2frame("C:/Users/Student/Desktop/iuiuiu.mp4","c:/users/Student/desktop/capture/")