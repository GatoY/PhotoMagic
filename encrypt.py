import cv2
import random
#img is RGB. s is the string which will be inserted to img.
def encrypt(img,s):
    with open('record.txt','r') as f:
	lines=f.readlines()
	print lines
	if len(lines)!=0:
	    print 'lines is not null'
	    last_line=lines[-1]
	    print last_line
	    count=int(last_line[:last_line.index(':')])
	else:
	    count=0
    num=random.randint(0,img.size)
    for i in xrange(10):
	pixel_x=random.randint(0,img.shape[0]-1)
	pixel_y=random.randint(0,img.shape[1]-1)
	img.itemset((pixel_x,pixel_y,0),img.item(pixel_x,pixel_y,0)+random.randint(-10,10))
	img.itemset((pixel_x,pixel_y,1),img.item(pixel_x,pixel_y,1)+random.randint(-10,10))
	img.itemset((pixel_x,pixel_y,2),img.item(pixel_x,pixel_y,2)+random.randint(-10,10))
    count+=1
    print count
    img.itemset((0,0,0),count/255/255%255)
    img.itemset((0,0,1),count/255%255)
    img.itemset((0,0,2),count%255)
    record_addr=[]
    with open ('record.txt','a+') as f:
	f.write(str(count)+':')
	for i in xrange(len(s)):
	    pixel_x=random.randint(1,img.shape[0])
	    pixel_y=random.randint(1,img.shape[1])
	    img.itemset((pixel_x,pixel_y,1),ord(s[i]))
            print ord(s[i])
	    f.write(str(pixel_x)+',')
	    f.write(str(pixel_y)+' ')
	    
	print 'success'
	f.write("\n")    
    cv2.imwrite('encrypt.png',img)
img=cv2.imread('1.jpg')
s='zxc dsfawe ./'
encrypt(img,s)

