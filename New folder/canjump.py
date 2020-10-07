import pyautogui
import time
import PIL
import math,os,subprocess

#input('start '+str(times))
def dragTo(x):
    #print('i m in sending shell')
    process = subprocess.Popen(
    "adb shell",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)
    time.sleep(0.3)
    #print('i m in')
    process.communicate( b"input touchscreen draganddrop 700 700 700 700  "+str.encode(str(x)+" \n"))
    #print('i m in')
    #input touchscreen draganddrop 700 700 700 700 100ms

def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
def dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance)
#
distance=[25, 30,30,
          30, 30, 30,
          25, 246.24581214713075]
no=[(254, 231, 94), (254, 208, 100), (254, 186, 108),
    (254, 163, 115), (254, 147, 119), (254, 117, 129),
    (254, 94, 135), (254, 71, 143)]

'''
times=0.002238805970149254
#0.002238805970149254/pixel
input('start '+str(times))
pyautogui.mouseDown(700,700)
time.sleep(times*126)
pyautogui.mouseUp(700,700)'''
#20 vertical slots
#tell_color_dis(im.getpixel((685,110+i),(145,144,143),49.08156476723211)
for jk in range(100):
    im = PIL.ImageGrab.grab()
    start=0
    max_end=(10000,100000)
    for x in range(497,943,15):
        for y in range(100,900-20):
            if tell_color_dis(im.getpixel((x,y)),no[int(y/100)-1],distance[int(y/100)-1])!=True:
                '''
                print('no match',(x,y),int(y/100),
                      dis(im.getpixel((x,y)),no[int(y/100)-1],distance[int(y/100)-1]),
                      distance[int(y/100)-1],
                      im.getpixel((x,y)),no[int(y/100)-1])
                '''
                #pyautogui.moveTo(x,y+5)
                if  tell_color_dis(im.getpixel((x,y+5)),(145,144,143),49.08156476723211):
                    #print((x,y+5))
                    pt=x-40
                    flg=0
                    flg1=0
                    for i in range(40):
                        flg=0
                        flg1=0
                        #print('loop')
                        #pyautogui.moveTo(pt+i,y+15)
                        if tell_color_dis(im.getpixel((pt+i,y+15)),(183,26, 38),104.5609869884557):
                            for gt in range(15):
                                #'''
                                #pyautogui.moveTo(pt+i+1,y+15+gt)
                                '''
                                print((pt+i+1,y+15+gt),((tell_color_dis(im.getpixel((pt+i+1,y+15+gt)),(183,26, 38),104.5609869884557)and
                                                         tell_color_dis(im.getpixel((pt+i+2,y+15+gt)),(183,26, 38),104.5609869884557)and
                                                        tell_color_dis(im.getpixel((pt+i+3,y+15+gt)),(183,26, 38),104.5609869884557))and
                                (tell_color_dis(im.getpixel((pt+i+1+24,y+15+gt)),(183,26, 38),104.5609869884557)and
                                 tell_color_dis(im.getpixel((pt+i+2+24,y+15+gt)),(183,26, 38),104.560986))),
                                      ((tell_color_dis(im.getpixel((pt+i+1,y+15+gt)),(183,26, 38),104.5609869884557),
                                        tell_color_dis(im.getpixel((pt+i+2,y+15+gt)),(183,26, 38),104.5609869884557),
                                        tell_color_dis(im.getpixel((pt+i+3,y+15+gt)),(183,26, 38),104.5609869884557)),
                                (tell_color_dis(im.getpixel((pt+i+1+24,y+15+gt)),(183,26, 38),104.5609869884557),
                                 tell_color_dis(im.getpixel((pt+i+2+24,y+15+gt)),(183,26, 38),104.560986))))#'''

                                if (tell_color_dis(im.getpixel((pt+i+1,y+15+gt)),(183,26, 38),104.5609869884557)and
                                     tell_color_dis(im.getpixel((pt+i+2,y+15+gt)),(183,26, 38),104.5609869884557)and
                                     tell_color_dis(im.getpixel((pt+i+3,y+15+gt)),(183,26, 38),104.5609869884557)and
                                tell_color_dis(im.getpixel((pt+i+1+24,y+15+gt)),(183,26, 38),104.5609869884557)and
                                 tell_color_dis(im.getpixel((pt+i+2+24,y+15+gt)),(183,26, 38),104.5609869884557)and
                                 tell_color_dis(im.getpixel((pt+i+3+24,y+15+gt)),(183,26, 38),104.5609869884557))!=True:
                                    flg+=1
                                    #pyautogui.moveTo(pt+i+1,y+15+gt)
                                    #print('here it break')
                                    break
                            for gti in range(10):
                                #pyautogui.moveTo(pt+i+11,y+30+gt)
                                if tell_color_dis(im.getpixel((pt+i+11,y+30+gti)),(230,210,207),80)==True:
                                    flg1+=1
                                    break

                            if flg==0 and flg1==1:
                                #print('start=',((pt+i,y+15)))
                                start=pt+i+15
                                break
                            #print('t')
                            #break
                    break
                if max_end[1]>y:
                    max_end=(x,y)
                    break
    drsn=''
    if tell_color_dis(im.getpixel((max_end[0]-1,max_end[1])),no[int(max_end[1]/100)-1],distance[int(max_end[1]/100)-1]):
        drsn='r'
    else:
        drsn='l'
    cunt=0
    sptc=0
    print('max_end=',max_end,'\nstart=',start,'\n',sptc)
    #'''
    
    while True:
        ptr=[0,max_end[1]]
        if drsn=='r':
            ptr[0]=max_end[0]-cunt
        else:
            ptr[0]=max_end[0]-cunt
        if tell_color_dis(im.getpixel((ptr[0],ptr[1])),no[int(max_end[1]/100)-1],distance[int(max_end[1]/100)-1])!=True:
            #print('in')
            sptc+=1
        else:
            break
        cunt+=1
    if drsn=='r':
        #print('Rrrrrrr')
        sptc=max_end[0]+round(sptc/2)
    else:
        #print('Llllll',max_end[0],cunt)
        sptc=max_end[0]-round(sptc/2)
    pyautogui.moveTo(sptc,max_end[1])
    #>200=0.0023578643750758405

    
    #     0.002238805970149254/pixel
    s=sptc-start
    if '-'in str(s):
        s=int(str(s)[1:])
        
    times=0.002239515970149254
    if s>=250 and s<300:
        times=0.0023578783750758405
    if s>=210 and s<250:
        times=0.0023578683750758405
    if s>=150 and s<210:
        times=0.002239511970149254##
    if s>=100 and s<130:
        times=0.002239510970149254
    if start==0 or s<70:
        continue
        f=os.listdir('.')
        k7i=0
        while True:
            g=str(k7i)+'.jpg'
            if  g in f:
               k7i+=1
            else:
                im.save(g)
                break
    tm=times*(s)
    #tm=round(tm)
    print('pixels=',s,'time=',tm,'\n\n')
    #input('')
    pyautogui.mouseDown(700,700)
    time.sleep(tm)#round(times*(s),5))
    #dragTo(tm)
    pyautogui.mouseUp(700,700)
    time.sleep(2.2)
    #print('max_end=',max_end,'\nstart=',start,'\n',sptc)
    #'''
