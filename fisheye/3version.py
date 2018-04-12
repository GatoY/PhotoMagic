import cv2
import numpy as np
import math
import argparse
import time

def fishEye(imgName, outputfile):
    oriImg=cv2.imread(imgName)
    size=oriImg.shape
    fromX=size[0]
    newImg=np.zeros([2*size[0],2*size[0],3])
    for i in xrange(2*fromX):
        for j in xrange(2*fromX):
            newImg[i][j]=[255,255,255]
    a=0
    b=0
    c=0
    d=0
    for i in xrange(2*fromX):
        for j in xrange(2*fromX):
            p=int(math.sqrt((i-fromX)*(i-fromX)+(j-fromX)*(j-fromX)))
            if p<fromX:
                if j-fromX!=0:
                    theta=math.atan(abs(i-fromX)/float(abs(j-fromX)))
                    if i-fromX<0 and j-fromX<0:
                        y=int(size[1]*3/4.0-theta/2.0/math.pi*size[1])
                        
                        a=a+1
                    if i-fromX<0 and j-fromX>0:
                        y=int(theta/2.0/math.pi*size[1]+size[1]/4.0)
                        b+=1
                    if i-fromX>0 and j-fromX<0:
                        y=int(size[1]*3/4.0+theta/2.0/math.pi*size[1])
                        
                        c+=1
                    if i-fromX>0 and j-fromX>0:
                        y=int(size[1]/4.0-theta/2.0/math.pi*size[1])
                        d+=1
                    #print y
                    newImg[i][j]=oriImg[size[0]-p-1][y]

#newImg=cv2.resize(newImg,(fromX,fromX),interpolation=cv2.INTER_CUBIC)
    #newImg=cv2.GaussianBlur(newImg,(5,5),0)
    cv2.imwrite(outputfile,newImg)

def main(filepath,outputfile):
    fishEye(filepath,outputfile)
    end_time = time.time()
    print('running time is ')
    print(str(end_time-start_time)+'s')
if __name__ == "__main__":
    parser =argparse.ArgumentParser()
    parser.add_argument('-s','--sourcefile')
    parser.add_argument('-o','--outputfile')
    args=parser.parse_args()
    
    filepath=args.sourcefile
    outputfile=args.outputfile
    start_time = time.time()
    main(filepath,outputfile)
#imgName='test.jpeg'
