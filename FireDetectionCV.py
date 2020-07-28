import cv2
import numpy as np 
import tensorflow as tf 
from keras.preprocessing import image
from PIL import Image 


#load the model from the directory it is saved in
model = tf.keras.models.load_model("PATH TO THE MODEL")

cap = cv2.VideoCapture(0)
while True:

	ret, frame = cap.read()

	#make sure the frame captured is in RGB
	img = Image.fromarray(frame, 'RGB')
	img = img.resize((224, 224)) #model dims
	img = image.img_to_array(img)
	img = np.expand_dims(img, axis = 0)
	img = img/255
	predictions = model.predict(img)[0]
	pred = np.argmax(predictions)

	#0 indicates a fire, either mask it or change the color space of the needed ROI

	if pred = 0:
		frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV) #shows the probability value of the winning class
		print(predictions[pred])

		#can also use GRAYSCALE if needed
		#frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	cv2.imshow("Detection", frame)	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

