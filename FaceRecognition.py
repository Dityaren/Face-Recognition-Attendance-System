import cv2
import numpy as np
import face_recognition
import os
from tkinter import *
from datetime import datetime
import time

from PIL import Image, ImageTk

root = Tk()

root.geometry("760x570")

path = 'gambar'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markMasuk(name):
    with open('Absensi.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString},MASUK')
                break


def markKeluar(name):
    with open('Absensi.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString},KELUAR')
                break


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)


def absenMasuk():
    selesai = 0
    while selesai != 1:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(img, "Masuk", (70, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                selesai = 1

        if selesai != 1:
            cv2.imshow('Mencari Wajah......', img)
        else:
            cv2.destroyAllWindows()
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)
        gambar = Label(left_frame, width=500, height=500)
        gambar.imgtk = imgtk
        gambar.configure(image=imgtk)
        gambar.grid(row=1, column=1, rowspan=4)
        cv2.waitKey(1)
    print("Cetak")
    markMasuk(name)


def absenKeluar():
    selesai = 0
    while selesai != 1:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(img, "Keluar", (70, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                selesai = 1

        if selesai != 1:
            cv2.imshow('Webcam', img)
        else:
            cv2.destroyAllWindows()
            markKeluar(name)
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        gambar = Label(left_frame, width=500, height=500)
        gambar.imgtk = imgtk
        gambar.configure(image=imgtk)
        gambar.grid(row=1, column=1, rowspan=4)
        cv2.waitKey(1)


root.title("Program Absensi dengan Face Recognition")

myLabel = Label(root, text="")
myLabel.grid(row=0, column=0, columnspan=2)

left_frame = Frame(root, width=150, height=200)
left_frame.grid(column=1, padx=10, pady=5)

myButton = Button(left_frame, text="Absen Masuk", command=absenMasuk, padx=50, pady=50)
myButton.grid(row=2, column=0, padx=10, pady=10)

myButton2 = Button(left_frame, text="Absen Keluar", command=absenKeluar, padx=50, pady=50)
myButton2.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
