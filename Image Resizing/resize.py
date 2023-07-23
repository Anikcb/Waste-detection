import cv2
import os

path = os.chdir("D:\\Final Year Project\\New\\Classification\\Training_Data(Resized)\\Trash")

for file in os.listdir(path):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = cv2.imread(file)
        print(f"Original Dimensions : {img.shape}")
        resized = cv2.resize(img, (512,384))
        print(f"Resized Dimensions : {resized.shape}")
        cv2.imwrite(file, resized)














