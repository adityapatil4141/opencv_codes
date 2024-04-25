import cv2
img = cv2.imread('me.jpg',0)
re_img = cv2.resize(img,(500,800))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(re_img.shape)