import tensorflow as tf
import numpy as np
import cv2
from keras.utils import load_img, img_to_array
from keras.models import model_from_json



json_file = open('DenseNet_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("DenseNet_model.h5")


def getClassName(classNo):
    if   classNo == 0: return 'Glass'
    elif classNo == 1: return 'Metal'
    elif classNo == 2: return 'Paper'
    elif classNo == 3: return 'Plastic'
    elif classNo == 4: return 'Trash'




threshold = 75 
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # READ IMAGE
    success, imgOrignal = cap.read()

    cv2.putText(imgOrignal, "CLASS: " , (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    img=img_to_array(imgOrignal)
    img = tf.keras.preprocessing.image.smart_resize(img, (224, 224))
    img = img / 255.0
    img =np.expand_dims(img, axis =0)
    predictions = model.predict(img)
    print(predictions)


    probabilityValue = predictions[0][np.argmax(predictions)]*100
    classIndex = np.argmax(predictions)
    classType = getClassName(np.argmax(predictions))
    if probabilityValue > threshold:
        print(classType)
        cv2.putText(imgOrignal,str(classIndex)+" "+str(getClassName(classIndex)), (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(imgOrignal, str(probabilityValue)+"%", (180, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Result", imgOrignal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()