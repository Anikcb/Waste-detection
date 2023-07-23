import os

from ultralytics import YOLO
import cv2




cap = cv2.VideoCapture(0)
model_path = os.path.join('.', 'best.pt')

# Load model
model = YOLO(model_path) 

threshold = 0.5
class_name_dict = {0: 'Glass',1:'Metal',2:'Paper',3:'Plastic',4:'Trash'}

i=1
while (cap.isOpened()):
    ret, frame = cap.read()
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    if ret==True:
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(i)
    i=i+1

cap.release()
cv2.destroyAllWindows()
