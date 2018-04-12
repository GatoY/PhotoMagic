import cv2
import numpy as np
import math
import argparse

def fishEye(imgName):
    oriImg=cv2.imread(imgName)
    size=oriImg.shape
    fromX=size[0]
    newImg=np.zeros([2*size[0],2*size[0],3])
    for i in xrange(2*fromX):
        for j in xrange(2*fromX):
            newImg[i][j]=[255,255,255]
    origin=size[0]/2
    degPerPix=360.0/size[1]
    
    for p in range(0,fromX):
        for i in xrange(size[1]):
            x=int(size[0]+p*math.sin(degPerPix*i/180*math.pi))
            y=int(size[0]+p*math.cos(degPerPix*i/180*math.pi))
            #print x,y
            #print '00000'
            #print p,i
            if (newImg[x,y]==255).all():
                newImg[x][y]=oriImg[fromX-p-1][size[1]-i-1]
        
            else:
                newImg[x][y]=(oriImg[fromX-p-1][size[1]-i-1]+newImg[x][y])/2
    newImg=cv2.resize(newImg,(fromX,fromX),interpolation=cv2.INTER_CUBIC)
    newImg=cv2.GaussianBlur(newImg,(5,5),0)
    cv2.imwrite(outputfile),newImg)

def main(filepath,outputfile):
    fishEye(filepath,outputfile)

if __name__ == "__main__":
    parser =argparse.ArgumentParser()
    parser.add_argument('-s','--sourcefile')
    parser.add_argument('-o','--outputfile')
    args=parser.parse_args()

    filepath=args.sourcefile
    outputfile=args.outputfile
    main(filepath,outputfile)
#imgName='test.jpeg'

