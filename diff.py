import cv2
import numpy as np
import imutils
from skimage.measure import compare_ssim as ssim
from imutils.video import VideoStream
vs=VideoStream(src=0).start()

def detect(im1,im2):
	im3=im1.copy()
	im4=im2.copy()
	im1=cv2.GaussianBlur(im1, (25, 25), 0)
	im2=cv2.GaussianBlur(im2, (25, 25), 0)
#producing diff image
	_,diff=ssim(cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY),cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY),full=True)
# 	cv2.imshow('diff',diff)

#producing threshold image for finding countours
	thresh = cv2.threshold((diff*255).astype('uint8'), 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#getting countors
	cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	for c in cnts:
		x,y,w,h=cv2.boundingRect(c)
		if w>50 and h>50:
# 			cv2.rectangle(im3,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.rectangle(im4,(x,y),(x+w,y+h),(0,0,255),2)
# 	cv2.imshow('im1',im3)
	cv2.imshow('im2',im4)
	return cv2.waitKey(1)


im1=vs.read()
im2=im1.copy()
while 1:
	im2=vs.read()
	k=detect(im1.copy(),im2.copy())
	if k==ord('1'):
		im1=vs.read()
	elif k==27:
		vs.stop()
		cv2.destroyAllWindows()
		break
		
	
