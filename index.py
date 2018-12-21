"""
A script that inddentifies faces on an image passed as an argument when executing the file
"""



import sys
import cv2
#getting the image and cascade from the commandline
image_path = sys.argv[1]
cascade_path = sys.aargv[2]

#Creating a cascade classifier - loading face cascade into memory
face_cascade = cv2.CascadeClassifier(cascade_path)

#read the image and convert it to a grayscale
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detecting faces and storing them into a variable
faces = face_cascade.detectMultiScale(
			
				gray_image,
				scaleFactor=1.4,
				minNeighbors=5,
				minSize=(4,4),
				flags=cv2.cv.CV_HAAR_SCALE_IMAGE				

)

#Nnumber of faces detected
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		
#display the detected faces		
cv2.imshow("Faces found", image)
cv2.waitKey(0)		

