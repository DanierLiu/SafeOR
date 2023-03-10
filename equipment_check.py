import tensorflow.keras
import numpy as np
import cv2
import firebase_admin
from firebase_admin import credentials, db, firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Generates a dict to store the labels(keys) and its names(values)

def gen_labels():
        labels = {}
        with open("labels.txt", "r") as label:
            text = label.read()
            lines = text.split("\n")
            print(lines)
            for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    labels[hold[0]] = hold[1]
        return labels

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
image = cv2.VideoCapture(1)
# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

"""
Create the array of the right shape to feed into the keras model
The 'length' or number of images you can put into the array is
determined by the first position in the shape tuple, in this case 1."""
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# A dict that stores the labels
labels = gen_labels()

while True:
    # Choose a suitable font
    font = cv2.FONT_HERSHEY_SIMPLEX
    ret, frame = image.read()
    key = cv2.waitKey(1) & 0xFF
    frame = cv2.flip(frame, 1)
    # In case the image is not read properly
    if not ret:
        continue
    # Draw a rectangle, in the frame
    frame = cv2.rectangle(frame, (100, 80), (1800, 1000), (0, 0, 255), 3)
    # Draw another rectangle in which the image to labelled is to be shown.
    frame2 = frame[80:360, 220:530]
    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    frame2 = cv2.resize(frame2, (224, 224))
    # turn the image into a numpy array
    image_array = np.asarray(frame2)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    pred = model.predict(data)
    result = np.argmax(pred[0])

    # Print the predicted label into the screen.
    cv2.putText(frame,  "Label : " +
                labels[str(result)], (230, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    if(labels[str(result)] == "Fork"):
        doc_ref = db.collection(u'equipment').document(u'scalpel')
        doc_ref.update({u'taken':True})

    if(labels[str(result)] == "Scalpel"):
        doc_ref = db.collection(u'equipment').document(u'fork')
        doc_ref.update({u'taken':True})
    
    if(labels[str(result)] == "Fork and Scalpel"):
        doc_ref = db.collection(u'equipment').document(u'fork')
        doc_ref.update({u'taken':False})
        doc_ref = db.collection(u'equipment').document(u'fork')
        doc_ref.update({u'taken':False})
    
    # Show the frame   
    cv2.imshow('Frame', frame)

 
	# if the `esc` key was pressed, break from the loop
    if key == 27:
        break

image.release()
cv2.destroyAllWindows()

