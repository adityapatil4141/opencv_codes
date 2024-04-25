import cv2
import numpy as np
import os
import os

# Specify the directory path containing the image files
directory = "images"

# Get the list of all files in the directory
file_list = os.listdir("images")
images_list = [file for file in file_list]
print(images_list)

for i in images_list:
    path="images"
    image_name = path+"/"+i
    print(image_name)
    img = cv2.imread(image_name,0)
    img = cv2.resize(img,(500,500))
    cv2.imshow('images',img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
