import os

path = os.chdir("D:\\Final Year Project\\New\\Classification\\Data\\Training\\Yolo_Dataset1\\Trash")

i=0
for file in os.listdir(path):
    file = file.lower()
    pre_name = "Trash"
    print(file)

    if file.endswith('.jpg'):
        new_name = pre_name + "{}.jpg".format(i)
        os.rename(file,new_name)
        i=i+1

    elif file.endswith('.jpeg'):
        new_name = pre_name + "{}.jpeg".format(i)
        os.rename(file,new_name)
        i=i+1

    elif file.endswith('.png'):
        new_name = pre_name + "{}.png".format(i)
        os.rename(file,new_name)
        i=i+1