from Source import Colors
import cv2

unsplash_link = "https://api.unsplash.com/photos/?client_id=d0012cf0474c5276ab2c2a9db274aea9b0d23b81361435fa9a2e37bed8992bc9"

cv2_directory = "C:/Users/Rustom Ichhaporia/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/"
face_cascade = cv2.CascadeClassifier(cv2_directory+"haarcascade_frontalface_default.xml")
face_image = cv2.imread("Images/Inputs/Group4.jpg")
grey = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=6,  minSize=(1, 1), flags=cv2.CASCADE_SCALE_IMAGE)
print(faces)
for (x, y, w, h) in faces:
    # box_color = Colors.get_colors(1)
    # print(box_color)
    cv2.rectangle(face_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces Detected", face_image)
cv2.waitKey(0)

