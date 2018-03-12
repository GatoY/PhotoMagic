import cv2
import numpy as np
import math
def fishEye(imgName):
    oriImg=cv2.imread(imgName)
    size=oriImg.shape
    fromX=size[0]
    newImg=np.zeros([2*size[0],2*size[0],3])
    for i in xrange(2*fromX):
        for j in xrange(2*fromX):
            newImg[i][j]=[255,255,255]

    for i in xrange(2*fromX):
        for j in xrange(2*fromX):
            p=int(math.sqrt((i-fromX)*(i-fromX)+(j-fromX)*(j-fromX)))
            if p<1080:
                if i-fromX<0 and j!=0:
                    thet=math.atan(i/float(j))
                    y=int(thet/2.0/math.pi*size[1])
                if i-fromX>=0 and j!=0:
                    thet=math.atan(i/float(j))
                    y=int(size[1]-thet/2.0/math.pi*size[1])
                if j!=0:
                    #print j,i,p,y
                    newImg[i][j]=oriImg[size[0]-p-1][y]

    newImg=cv2.resize(newImg,(fromX,fromX),interpolation=cv2.INTER_CUBIC)
    #newImg=cv2.GaussianBlur(newImg,(5,5),0)
    cv2.imwrite('Ep%y%m.png',newImg)
#cv2.imshow('image',newImg)
#cv2.waitKey()
imgName='test.jpeg'
fishEye(imgName)
