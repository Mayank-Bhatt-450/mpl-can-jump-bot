import pyautogui,time
from PIL import Image
import math
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''

u=[0,0,0]
l=[112,194,127]
def dis(pt1,pt2=(2,35,47)):
    #pt1=[0,0,00]
    pt2=(0,0,0)#(230,210,207)#(145,144,143)#(145,35,43)
    distance=math.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2))
    return(distance)

img = Image.open("000.png")
g=[]
k=400
pix=[0,0,0]
pixno=0
no=[]
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if d[0]<250 and d[1]>0 and d[2]>0:#dis(d,[170,10,154])>10 and
            #print('in')
            pixno+=1
            pix[0]+=d[0]
            pix[1]+=d[1]
            pix[2]+=d[2]
            if d not in g :
                fr=dis(d)
                if k>fr and d not in no:
                    k=fr
                    print(d,',')
                    


print(k)#,round(pix[0]/pixno),round(pix[1]/pixno),round(pix[2]/pixno))



