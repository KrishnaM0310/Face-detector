import cv2

#essentially cv2.cascadeClassifier will detect something as a face (Classifier)  
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose image to detect faces in
#img = cv2.imread('jungkook.jpg')

webcam = cv2.VideoCapture(0) #0 for default webcam

#iterate forever over items
while True:

    ###read the current frame
    succesful_frame_read, frame = webcam.read()


    #makes frame into greyscale (iamge u want, what colur u want to change it)
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces (detectmultiscale = detect all faces no matter scale of face, small big, etc)
    face_coordinate = trained_face_data.detectMultiScale(grayscale_img)


    #draw rectangle around faces of each frame
    for (x,y,w,h) in face_coordinate:
        cv2.rectangle(frame, (x, y),(x+w,y+h),(0,255,0), 5)
        cv2.putText(frame,'face',(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    
    #show image
    cv2.imshow('Face Detector App',frame)

    #pauses code so the img doesnt just go away and code doesnt just execute immediately, will wait until a key is pressed to execute
    key = cv2.waitKey(1)

    #stop if q key is pressed
    if key==81 or key==113:
        break
    


'''
#detect faces (detectmultiscale = detect all faces no matter scale of face, small big, etc)
face_coordinate = trained_face_data.detectMultiScale(grayscale_img)

#draw rectangle around faces
for (x,y,w,h) in face_coordinate:
    cv2.rectangle(img, (x, y),(x+w,y+h),(0,255,0), 5)

#print(face_coordinate)

#show image
cv2.imshow('Face Detector App',img)

#pauses code so the img doesnt just go away and code doesnt just execute immediately, will wait until a key is pressed to execute
cv2.waitKey()
'''
print("Code Completed")