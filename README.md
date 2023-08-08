# DOCUMENTATION
<details>
  <summary> INSTALL(Python 3.8) </summary>

  ```sh
  git clone https://github.com/Anikcb/Waste-detection.git
  cd Waste-detection
  pip install -r requirements.txt
  ```
</details>

<details>
  <summary> TRAINING </summary>

  > To train a model, use "Dataset" folder and use the codes from "Algorithms"
 
</details>


### <ins>RUN REALTIME WASTE DETECTION</ins>
Install all packages from "requirements.txt" file and then run "reltime.py"

  ```sh
  pip install -r requirements.txt
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
![Sensors](https://github.com/Anikcb/Waste-detection/blob/main/Data/sensors.png?raw=true)

### <ins>DENSITY BASED CLASSIFICATION</ins>
For density-based object detection, we created a project which calculates the density from area and weight. Our area measurement model provides the dimensions of a reference object and finds the dimensions of other objects in a scene. Then our model calculates how many pixels are there per metric (centimeter is used here) and for computing results raw bounding boxes around each object and calculate its height and width. From height and width, we calculate the volume of an object. For weight measurement, we used Weighing Load Cell Sensor which can measure up to 1 kg of weight. We get our density by dividing a quantity such as mass by an area or volume. Based on the density we predict the type of waste.

![Weight measurement](https://github.com/Anikcb/Waste-detection/blob/main/Data/weight.png?raw=true)

![Area measurement](https://github.com/Anikcb/Waste-detection/blob/main/Data/area.png?raw=true)

By camera, our system will detect the size of an object and the sensor will provide the weight. we can see how our system will measure the length, width, and height of an object. We used two cameras for measuring the sizes. One will get length, and width and the other will get height. It will calculate the volume by multiplying them.

## Merged Classification Technique

We have used three classifications in our system. The first one is image classification, in which the camera will detect the image with image processing. We can get the accuracy value from image processing. We called it Image Classification Value (I.C.V.). Second one is sensor-based classification, in which our system will detect if the object is metal or not. We have given some value to the result of the sensors. That is Sensor Classification Value (S.C.V). If the object is metal, the metal detector will give ‘1’ value, then the other class will get ‘0’. If the object is not metal then the Capacitive sensor will give ‘0’ for metal. The third one is density-based classification, in which our system will detect the density of an object from its volume and weight. Our system can check our collected database in which we have collected some data through resources and testing of density. If the density of that object matched with any object’s density scale from our database, our system will put probability for that object</br></br>
We have given some weighted values for this classification result. We got these values by trial and error. In the table given below, we can see the weighted value for individual classes.

|        |I.C.V.|S.C.V.|D.C.V.|
|--------|------|------|------|
|Plastic |75%   |15%   |10%   |
|Metal   |5%    |75%   |20%   |
|Glass   |70%   |15%   |15%   |
|Paper   |70%   |10%   |20%   |
|Trash   |90%   |5%    |5%    |

**New Classification Value** = ( **ICV** X **Corresponding Weight** + **SCV** X **Corresponding Weight** + **DCV** X **Corresponding Weight** )

## Server

### <ins>Bin Monitoring</ins>
Admins can see the location of bins. When the bin reaches its limit, the system will call to garbage truck to remove the waste from the bin. Admins can directly log in and access the server and see the level of garbage in every bin which reduces the physical labor.

![Real-time bin monitoring](https://github.com/Anikcb/Waste-detection/blob/main/Data/bin%20level.png?raw=true)</br>


### <ins>Website for Reward Module</ins>

This subsystem basically deals with users and their rewards. Rewards will be provided based on their contribution. The users can redeem their rewards points to buy products/tickets from authorized sellers. This module has two parts. One is for admin another is for general users.Users need an account for accessing our website. New users can register with their NID and phone number and access their accounts.

![Registration Form](https://github.com/Anikcb/Waste-detection/blob/main/Data/registration.png?raw=true)

Users who already have accounts, can simply login with their registered phone number and password.
![User Login](https://github.com/Anikcb/Waste-detection/blob/main/Data/login.png?raw=true)

When users register on our website, a QR code will be provided according to their number. When they scan the QR code and throw waste in the bin, points will be added to our database according to the phone number and the points of that particular account will be increased.

![QR Scan](https://github.com/Anikcb/Waste-detection/blob/main/Data/identifying%20user.png?raw=true)

They can check their points by accessing their account. After using the points, users can check their usage history sorted by date.
Points will be added based on the type and weight of waste, the user throws in the bin. For example, if a user throws 10g of metal, he will get 20 points. If the user throws 20g of plastic, he will get 20 points. For 30g of trash objects, he will get 10 points. For 100 points, user will get 10tk from our website.

![Users account](https://github.com/Anikcb/Waste-detection/blob/main/Data/history.png?raw=true)

Users can use that points for mobile recharge or generate a promo code for buying staff in many shops. There are several sim companies in Bangladesh such as Robi, Grameenphone, Teletalk etc. Users can select the sim name and give their number to recharge. They also can create promo codes to use in some shops such as Shwapno, Daraz, Bigbazar, Alibaba, etc. for buying products.

![use rewards](https://github.com/Anikcb/Waste-detection/blob/main/Data/user%20reward.png?raw=true)

Users also can check nearby bin locations from our site for throwing their waste. If users know the location of bins it will be easier for them to locate where to throw the trash. Because of that, they will not throw trash everywhere

![Bin Location](https://github.com/Anikcb/Waste-detection/blob/main/Data/bin%20location.png?raw=true)

### <ins>Admin Panel</ins>
Administration can manually update the points or details of users from their portal. They will have separate emails and passwords for accessing in the admin panel on our website. This email and password will be given by us because admins cannot register on the website. Their data will be in the database from the start.

![Admin Login](https://github.com/Anikcb/Waste-detection/blob/main/Data/admin%20login.png?raw=true)

They also can check the user's point history from their panel and delete user if its necessary. They can see the details of any user from our site. Basically, admins have access to the information of users

![User information in admin area](https://github.com/Anikcb/Waste-detection/blob/main/Data/user%20data.png?raw=true)

Admins can update user’s points manually. After checking, they can increment or decrement points. They can also see user point usage history from their side. They can monitor the bin levels and bin location also.

![Manually update](https://github.com/Anikcb/Waste-detection/blob/main/Data/manual%20update%20of%20user.png?raw=true)

## Conclusion
Garbage management is one of the most concerned issues in recent era. Garbage overflow happens as a result of a lack of an effective waste management system, causing severe damage to the environment. Waste management system is essential to keep environment clean and to reduce the diseases caused by waste. In this study, we aimed to create automated waste management system with reward module integrated with IOT devices. We have used three classification techniques for object detection to make a smart bin, which automatically segregates wastes. Image processing is done by YOLO v8 and sensor based classification and density based classification is done by sensors. Here we classified wastes into five recyclable categories such as paper, plastic, glass, metal, and trash. Once the object detection is done, a servo motor rotates garbage bins to show the appropriate container based on the waste that has been identified. Garbage bin capacity is determined using ultrasonic sensors mounted to the top of each container, which calculated the distance from the closest object inside the container. For real-time bin capacity monitoring, the Arduino transmits the trash can capacity to the ESP8266 Wi-Fi module, which subsequently uploads it to our server. Citizens register on our website with their details and then they can throw their waste in our smart bin by QR code scanning. Depending on their throwing waste, they will get points, which will be added to their account. They will able to redeem it as mobile recharge or promo code.
In order to analyze the accuracy and other parameters; we compared DesnseNet169, MobileNetV2, ResNet50, VGG19, CNN, SVM, and YOLO v8 models in this report. We discovered that every classifier’s accuracy grew as the number of epoch levels did. From our comparison, we can see almost every model’s accuracy is good after increased epoch number except SVM. But after testing YOLO v8 is the best model for real-time testing as it could identify most objects accurately. This model has less accuracy in the trash class because the number of trash images is less compared to other objects. Though YOLO v8 does not get the highest accuracy comparing other models we have achieved our aim to create an automated waste object segregation system. YOLO v8 provides an accuracy of 0.98 after being fitted in 35 epochs. This model also has 0.96 and 0.95 as precision and recall, respectively. We have also used sensors for metal detection and density based classification which will increase our system’s accuracy along with YOLO v8. After merging the results, we get about 84% of accuracy for our system. Because of the lack of trash data accuracy is less than 90% even though other’s classes accuracy is more than 90%.
The effect of our system will be quite helpful for society. Citizens will throw waste in bins as they will get points which is the success of our reward module and real-time bin level monitoring will help people reduce physical labor as they do not have to monitor 24/7 by sitting in front of the desk. Segregating waste by humans is quite unhygienic. Our system will make it easier by automating it and the waste not being in the open place will be better for climate change.

## Challenges and Issues
There are various difficulties with the system used in this study. First of all, users need to wait for throwing multiple wastes as it take time for processing one waste. This is due to the fact that the system is unable to identify numerous items since the servo can only spin once to show the right container before detecting the waste again and rotating to reveal a different container. The second problem is, if one separated bin for particular class is full, even if other bins are empty, users can not throw waste as the system will not run. Thirdly, sending real-time data requires constant electricity, which is a hurdle. Lastly, datasets which contains photos of objects that are a little distinct from local wastes was the project's major problem. This explains why the algorithm made the wrong prediction on a few pictures of local garbage.





