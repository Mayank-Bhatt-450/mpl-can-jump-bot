import pyautogui,time
from PIL import Image
import math,PIL
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
#8 100
u=[0,0,0]
l=[112,194,127]
def dis(pt1,pt2=(2,35,47)):
    #pt1=[170,10,154]
    #pt2=(145,35,43)#(145,144,143)#(145,35,43)
    distance=math.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2))
    return(distance)

img = Image.open("000.png")#PIL.ImageGrab.grab()#



distance=[]

no=[(254, 231, 94), (254, 208, 100), (254, 186, 108), (254, 163, 115), (254, 147, 119), (254, 117, 129), (254, 94, 135), (254, 71, 143)]
h=0
for y in range(100,900,100):
    print(y)
    g=[]
    k=0
    pix=[0,0,0]
    pixno=0
    for i in range(100):
        for x in range(497,505):#,943):
            if y>800:
                print(x,y+i)
            d=img.getpixel((x,y+i))
            #print(d)
            if d[1]>10 and d[0]>10:#dis(d,[170,10,154])>10 and 
                pixno+=1
                pix[0]+=d[0]
                pix[1]+=d[1]
                pix[2]+=d[2]
                fr=dis(d,no[h])
                if k<fr :
                    k=fr
                    print(d,',')
    distance.append(k)
    #no.append((round(pix[0]/pixno),round(pix[1]/pixno),round(pix[2]/pixno)))
    #print(k,pix[0],pixno,pix[1],pixno,pix[2],pixno)
    print(k,pix[0]/pixno,pix[1]/pixno,pix[2]/pixno)
    h+=1
print (no)
print (distance)


    






