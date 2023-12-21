import cv2

img=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE) #此为以灰度图格式读入，彩色读入则shape是3通道
print(type(img)) #<class 'numpy.ndarray'>
print(img.shape) #(368, 640)

cv2.imshow('image',img)#一闪而逝
#cv2.waitKey(0)#延时阻塞 0一直阻直到键入  单位毫秒
#k=cv2.waitKey(0)
#print(k)  #输出键入的ASCII值

cv2.imwrite('img_gray.jpg',img)#灰度图重组到文件里，图片要指定后缀，cv以此确定压缩格式

