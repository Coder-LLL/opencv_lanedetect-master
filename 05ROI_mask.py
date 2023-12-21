import cv2
import numpy as np

edge_img=cv2.imread('edge_img.jpg',cv2.IMREAD_GRAYSCALE)

mask=np.zeros_like(edge_img)
mask=cv2.fillPoly(mask,np.array([[[0,368],[300,210],[340,210],[640,368]]]),color=255)
#cv2.imshow('mask',mask)
#cv2.waitKey(0)
mask_edge_img=cv2.bitwise_and(edge_img,mask)
cv2.imshow('mask_edge_img.jpg',mask_edge_img)
cv2.imwrite('mask_edge_img.jpg',mask_edge_img)
cv2.waitKey(0)