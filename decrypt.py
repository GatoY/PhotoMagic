import cv2
def decrypt(img):
    count=img.item(0,0,0)*255*255
    count=img.item(0,0,1)*255+count
    count=img.item(0,0,2)+count
    pixel_x=[]
    pixel_y=[]
    with open('record.txt','r') as f:
	lines=f.readlines()
	line=lines[count-1]
	line=line[(line.index(':')+1):]
	xandy=line.split(' ')[:-1]
	for i in xandy:
	    pixel_x.append(i[:i.index(',')])
	    pixel_y.append(i[i.index(',')+1:])
    s=''
    for i in xrange(len(pixel_x)):
	s=s+chr(img.item(int(pixel_x[i]),int(pixel_y[i]),1))
    print s
img=cv2.imread('encrypt.png')
decrypt(img)


