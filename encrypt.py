import cv2
import random
#img is RGB. s is the string which will be inserted to img.
def encrypt(img,s):
    with open('record.txt','w+') as f:
	lines=f.readlines()
	last_line=lines[-1]
	count=last_line[:last_line.index(':')]
    num=random.randint(0,img.size)
    for i in xrange(num):
	pixel_x=random.randint(0,img.shape[0])
	pixel_y=random.randint(0,img.shape[1])
	img.itemset((pixel_x,pixel_y,0),img.item(pixel_x,pixel_y,0)+randint(-10,10))
	img.itemset((pixel_x,pixel_y,1),img.item(pixel_x,pixel_y,1)+randint(-10,10))
	img.itemset((pixel_x,pixel_y,2),img.item(pixel_x,pixel_y,2)+randint(-10,10))
    count+=1
    img.itemset((0,0,0),count/255/255%255)
    img.itemset((0,0,1),count/255%255)
    img.itemset((0,0,2),count%255)
    record_addr=[]
    for i in xrange(len(s)):
	pixel_x=random.randint(1,img.shape[0])
	pixel_y=random.randint(1,img.shape[1])
	img.itemset((pixel_x,pixel_y,0),encode(s[i])/255/255%255)
	img.itemset((pixel_x,pixel_y,1),encode(s[i])/255%255)
	img.itemset((pixel_x,pixel_y,2),encode(s[i])%255)
        record_addr.append([pixel_x,pixel_y])



