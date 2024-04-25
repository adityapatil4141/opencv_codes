import cv2
import numpy as np
img = cv2.imread('me.jpg',0)
print(img)
re_img = cv2.resize(img,(500,500))   #width,height
h = np.hstack((re_img,re_img))
cv2.imshow('img',h)
cv2.waitKey(0)
cv2.destroyAllWindows()

#For Vertical
prof = cv2.imread('profile.jpg')
re_prof = cv2.resize(prof,(500,500))
v = np.vstack((re_prof,re_prof))
cv2.imshow('profile',v)
cv2.waitKey(0)
cv2.destroyAllWindows()


#for all images in grid
prof = cv2.imread('profile.jpg')
re_prof = cv2.resize(prof,(300,300))
h = np.hstack((re_prof,re_prof,re_prof)) # 3 images horizontally
v = np.vstack((h,h,h,h)) # 4 images vertivally
cv2.imshow("profile",v) # Total = 4 x 3=12 images
cv2.waitKey(0)
cv2.destroyAllWindows()