# Documentation
<details>
  <summary> INSTALL </summary>

  <blockquote>

  ```sh
  git clone https://github.com/Anikcb/Waste-detection.git
  cd Waste-detection
  pip install -r requirements.txt
  ```
</details>
<details>
  <summary> TRAINING </summary>

  <blockquote>

  ```sh
  If you want to train a model, you can use the "Dataset" folder for the dataset and train them by
  using the codes in "Algorithms"
  ```
</details>

### RUN Image Classification

After installing the repository, install all packages from "requirments.txt" file and then run "reltime.py"
```sh
python realtime.py
```


| Algorithms  | Accuracy    | Precesion   | Recall     |
| ----------- | ----------- | ----------- | -----------|
| CNN         | 90%         |    0.90     | 0.90       |
| DenseNet169 | 99%         |    0.99     | 0.99       |
| MobileNetV2 | 91%         |    0.92     | 0.91       |
| ResNet50    | 98%         |    0.98     | 0.98       |
| VGG19       | 98%         |    0.98     | 0.98       |
| YOLOv8      | 97%         |    0.96     | 0.95       |
| SVM         | 17%         |    0.18     | 0.17       |
