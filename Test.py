import cv2
import numpy as np
import face_recognition

imgBill = face_recognition.load_image_file('gambar/bill_gates.jpg')
imgBill = cv2.cvtColor(imgBill, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('gambar/bill_test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgBill)[0]
encodeBill = face_recognition.face_encodings(imgBill)[0]
cv2.rectangle(imgBill, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

hasil = face_recognition.compare_faces([encodeBill], encodeTest)
perbedaan = face_recognition.face_distance([encodeBill], encodeTest)
print(hasil, perbedaan)
cv2.putText(imgTest, f'{hasil} {round(perbedaan[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Bill Gates', imgBill)
cv2.imshow('Bill Test', imgTest)
cv2.waitKey(0)
