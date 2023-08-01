# DOCUMENTATION
<details>
  <summary> INSTALL </summary>

  ```sh
  git clone https://github.com/Anikcb/Waste-detection.git
  cd Waste-detection
  pip install -r requirements.txt
  ```
</details>

<details>
  <summary> TRAINING </summary>

  > If you want to train a model, you can use the "Dataset" folder for the dataset and train them by
  using the codes in "Algorithms"
 
</details>

## RUN IMAGE CLASSIFICATION
After installing the repository, install all packages from "requirments.txt" file and then run "reltime.py"

  ```sh
  python realtime.py
  ```

## INTRODUCTION

we are proposing a hybrid wastage classification and management system using DL and ML with other IoT devices. We are also proposing a reward-giving policy via our website to encourage the user to use our system. The aim of our task is to categorize wastes into five classes such as paper, glass, metal, plastic, and trash in an automated system. For our project, we have compared the result of different deep learning algorithms such as DenseNet169, MobileNetV2, ResNet50, VGG19, SVM, CNN, and YOLO v8. We used YOLO v8 for object detection as it gives the best real-time accuracy among others and it has mean average precision (mAP) around of 0.98 with an IoU threshold placed at 0.5. By the ESP8266 Wi-Fi module, the real-time bin level is being monitored by our server. Arduino Uno has been used for controlling sensors. These sensors have been used in metal detection and density classification. Our system can combine three classification results and detect the object according to that value. Overall merged accuracy for our system is 83.8 %. For ‘glass’ and ‘metal’ class merged accuracy is 98% and for ‘paper’ and ‘plastic’ accuracy is 93% and 95%, respectively. Our system will reduce the segregation cost and speed up the process of waste management. This will also reduce the environmental pollution and people will not be directly contacted with waste because segregation is done by our smart bin.

## TOOLS
software used for our project are given below:
- Google Colab
- Python
- Machine Learning
- Roboflow
- VS studio
- PHP
- C++
  
Hardware used for our project are:
- Camera
- Arduino
- Servo Motor
- Ultrasonic Sensor
- Metal Detector Sensor
- Weight Measurement Sensor
- Capacitive Sensor
- LCD display
- Wi-Fi Shield
- Conveyor Belt
- Bins

## OBJECT DETECTION

In our system object classification is done based on image processing, sensor-based classification, and density-based classification

![Object Detection](https://github.com/Anikcb/Waste-detection/blob/main/Data/detection.png?raw=true)
### <ins>IMAGE CLASSIFICATION</ins>
We have trained our model using CNN, SVM, DenseNet169, MobileNetV2, ResNet50, VGG19, and YOLO v8 algorithms with our datasets and compared the result for best accuracy

| Algorithms  | Accuracy    | Precesion   | Recall     |
| ----------- | ----------- | ----------- | -----------|
| CNN         | 90%         |    0.90     | 0.90       |
| DenseNet169 | 99%         |    0.99     | 0.99       |
| MobileNetV2 | 91%         |    0.92     | 0.91       |
| ResNet50    | 98%         |    0.98     | 0.98       |
| VGG19       | 98%         |    0.98     | 0.98       |
| YOLOv8      | 98%         |    0.96     | 0.95       |
| SVM         | 17%         |    0.18     | 0.17       |

### <ins>SENSOR BASED CLASSIFICATION</ins>
We have used two sensors for object detection. For metal detection, we used an LC Metal detector non-contact metal induction detection module. When it approaches any metal, it makes a sound. For non-metal object detection, we have used a capacitive sensor that can detect plastic, glass, and wood.

### <ins>DENSITY BASED CLASSIFICATION</ins>
For density-based object detection, we created a project which calculates the density from area and weight. Our area measurement model provides the dimensions of a reference object and finds the dimensions of other objects in a scene. Then our model calculates how many pixels are there per metric (centimeter is used here) and for computing results raw bounding boxes around each object and calculate its height and width. From height and width, we calculate the volume of an object. For weight measurement, we used Weighing Load Cell Sensor which can measure up to 1 kg of weight. We get our density by dividing a quantity such as mass by an area or volume. Based on the density we predict the type of waste.
