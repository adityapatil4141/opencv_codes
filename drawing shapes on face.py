# import cv2
# old_img = cv2.imread('profile.jpg')
# old_img = cv2.resize(old_img,(400,400))
# new_img = cv2.line(img = old_img,pt1=(110,140),pt2=(30,140),color=(0,255,0),thickness=2 )
# cv2.imshow('me',old_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows( )



import cv2
old_img = cv2.imread('profile.jpg')
old_img = cv2.resize(old_img,(400,400))
tx_img = cv2.putText(img=old_img,text="Aditya",org=(30,115),fontFace=1,fontScale=1,
                     color=(0,0,255),thickness=1,lineType=16,bottomLeftOrigin=False)
new_img = cv2.rectangle(img = old_img,pt1=(30,120),pt2=(110,210),color=(0,255,0),thickness=2 )
cv2.imshow('me',old_img)
cv2.waitKey(0)
cv2.destroyAllWindows( )