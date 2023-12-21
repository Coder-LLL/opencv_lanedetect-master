import cv2

img=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)

edge_img=cv2.Canny(img,70,120)

#cv2.imshow('edges',edge_img)
#cv2.waitKey(0)
cv2.imwrite('edge_img.jpg',edge_img)