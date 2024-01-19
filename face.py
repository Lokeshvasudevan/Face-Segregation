import face_recognition as fr
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import shutil

Tk().withdraw()

# load sample image and encode
load_image = askopenfilename()
target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)


# encoding the image
def encode_faces(folder):
    list_people_encoding = []
    for filename in os.listdir(folder):
        known_image = fr.load_image_file(f'{folder}{filename}')
        known_encoding = fr.face_encodings(known_image)[0]
        list_people_encoding.append((known_encoding, filename))
    return list_people_encoding


# finding the faces and saving in new folder
def find_target_face():
    for person in encode_faces('py/people/'):
        encode_face = person[0]
        filename = person[1]
        is_target_face = fr.compare_faces(encode_face, target_encoding, tolerance=0.550)
        print(f'{is_target_face} {filename}')
        if is_target_face == [True]:
            origin = fr'people\{filename}'
            directory = r"Data"
            shutil.copy(origin, directory)


find_target_face()
