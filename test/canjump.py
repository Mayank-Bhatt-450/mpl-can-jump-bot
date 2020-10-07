import pyautogui
import time
import PIL
import math,os,subprocess
tm=[0.002239511970149254]
rng=[[0,400]]
"""
file1=open('file1.txt','r')
tm=file1.read()[1:len(file1.read())-1].split(',')

file1.close()
for it in  range(len(tm)):
    tm[it]=float(tm[it])

file2=open('file2.txt','r')
h=file2.read()
#print(h)
rng=h[:len(h)-1].split('\n')
#print(rng)
file2.close()
#print (rng)

for it in  range(len(rng)):
    rng[it]=(rng[it][1:len(rng[it])-1].split(','))
    for ji in range(len(rng[it])):
        rng[it][ji]=int(rng[it][ji].replace("'",''))
"""
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

for jk in range(1):
    im = PIL.ImageGrab.grab()
    start=0
    max_end=(10000,100000)
    """
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
    #sptc=890
    #start=621
    s=sptc-start
    if '-'in str(s):
        s=int(str(s)[1:])


    if start==0 or s<70:
        continue
        f=os.listdir('.')
        k7i=0
        while True:
            g=str(k7i)+'-.jpg'
            if  g in f:
               k7i+=1
            else:
                #im.save(g)
                break
    tmo=0
    tmno=0
    for i in range(len(rng)):
        #print('p',i,s,(rng[i][len(rng[i])-1])-1)
        if s>=int(rng[i][0]) and s<int(rng[i][1]) and s!=(rng[i][len(rng[i])-1])-1:
            tmo=tm[i]
            tmno=i
            break

    times=tmo*(s)
    #'''
    #tm=round(tm)
    print('pixels=',s,'time=',tmo,'\n\n')
    #input('')
    pyautogui.mouseDown(700,700)
    time.sleep(times)#round(times*(s),5))
    #dragTo(tm)
    pyautogui.mouseUp(700,700)
    #time.sleep(2.2)
    #print('max_end=',max_end,'\nstart=',start,'\n',sptc)
    
    #"""
    #max_end=[758,535]
    time.sleep(1.13)#s*0.009904621704895584)
    #'''
    
    #input('-0-0-0')
    max_end=[755,392]###############################
    

    hy=[max_end[0]-81,max_end[1]-42]

    bf=0
    for tt in range(1):#15):
        #print(tt,'---')
        img = PIL.Image.open("30.jpg")#PIL.ImageGrab.grab()'
        #img = PIL.ImageGrab.grab()
        '''
        img = PIL.ImageGrab.grab()
        f=os.listdir('.')
        k7i=0
        while True:
            g=str(k7i)+'.jpg'
            if  g in f:
               k7i+=1
            else:
                img.save(g)
                break'''

        flg3=0
        end2=0
        flg4=0
        flg6=0
        flg3=0
        for ti in range(0,162,10):
            for tk in range(50):
                x=hy[0]+ti
                y=hy[1]+tk
                #print((x,y+5))
                #pyautogui.moveTo(x,y)
                if  tell_color_dis(img.getpixel((x,y+5)),(145,144,143),60):
                    #pyautogui.moveTo(x,y+5)
                    pt=x-40
                    flg4=0
                    flg6=0
                    for i in range(40):
                        flg4=0
                        flg6=0
                        #print('loop')
                        #pyautogui.moveTo(pt+i,y+15)
                        if tell_color_dis(img.getpixel((pt+i,y+15)),(183,26, 38),104.5609869884557):
                            for gt in range(15):
                                #'''
                                #pyautogui.moveTo(pt+i+1,y+15+gt)

                                if (tell_color_dis(img.getpixel((pt+i+1,y+15+gt)),(183,26, 38),104.5609869884557)and
                                     tell_color_dis(img.getpixel((pt+i+2,y+15+gt)),(183,26, 38),104.5609869884557)and
                                     tell_color_dis(img.getpixel((pt+i+3,y+15+gt)),(183,26, 38),104.5609869884557)and
                                tell_color_dis(img.getpixel((pt+i+1+24,y+15+gt)),(183,26, 38),104.5609869884557)and
                                 tell_color_dis(img.getpixel((pt+i+2+24,y+15+gt)),(183,26, 38),104.5609869884557)and
                                 tell_color_dis(img.getpixel((pt+i+3+24,y+15+gt)),(183,26, 38),104.5609869884557))!=True:
                                    flg6+=1
                                    #pyautogui.moveTo(pt+i+1,y+15+gt)
                                    #print('here it break')
                                    break#FOR 15

                            for gti in range(10):
                                #pyautogui.moveTo(pt+i+11,y+30+gt)
                                if tell_color_dis(img.getpixel((pt+i+11,y+30+gti)),(230,210,207),80)==True:
                                    flg4+=1
                                    break#FOR 10
                            #print(flg6,flg4)
                            if flg6==0 and flg4==1:
                                #print('in',flg3)
                                for ii in range(20):
                                    #print('---',(pt+i+18+9,y+15-ii-20))#(pt+i+18,y+15-ii-44)
                                    #pyautogui.moveTo(pt+i+18,y+15-ii-40)
                                    if tell_color_dis(img.getpixel(((pt+i+18+9,y+15-ii-20))),(0,0,0),228.1446909309967) and tell_color_dis(img.getpixel((x,y+5)),(145,144,143),60) and flg3==0:
                                        #print('---',(pt+i+18,y+15-ii-44))
                                        f=os.listdir('.')
                                        k7i=0
                                        while True:
                                            g=str(k7i)+'.jpg'
                                            if  g in f:
                                               k7i+=1
                                            else:
                                                img.save(g)
                                                break
                                        flg3+=1
                                        break

                            if flg6==0 and flg4==1 and flg3==1:
                                print('start=',((pt+i,y+15)))#,s*0.009904621704895584)
                                end2=pt+i+15
                                bf+=1
                                break#FOR 40
                            else:
                                pass
                    if bf==1:
                        break#print('start=',((pt+i,y+15)))
            if bf==1:
                break
        if bf==1:
            break
                    #break
    #print('end:',sptc,end2,s)
    print('end:',end2)
"""#####################################
    if end2!=0:
        f=os.listdir('.')
        k7i=0
        while True:
            g=str(k7i)+'.jpg'
            if  g in f:
               k7i+=1
            else:
                img.save(g)
                break
    ed=end2-start
    if '-'in str(ed):
        ed=int(str(ed)[1:])
    
    if sptc>end2 and end2!=0 and tmo!=0:
        #print('inn')
        tem=[s-(sptc-end2)+1,rng[tmno][1]]
        rng[tmno][1]=s-(sptc-end2)+1
        s1=s-(sptc-end2)+1
        tm.append((tmo*s)/s1)
        rng.append(tem)
        #print(tm,rng)
    if sptc<end2 and end2!=0 and tmo!=0:
        tem=[s+1,rng[tmno][1]]
        rng[tmno][1]=s+1
        s1=s+(end2-sptc)
        tem1=tm[tmno]
        tm[tmno]=(tmo*s)/s1
        tm.append(tem1)
        rng.append(tem)
    print(tm,rng,'\n__________')


        
    if end2!=0:
        file1=open('log3.txt','a')
        it='''\n\ntm='''+str(tm)+'\nrng='+str(rng)+'\n'
        file1.write(str(it))
        file1.close()
    file1=open('file1.txt','w')
    file1.write(str(tm))
    file1.close()
    file1=open('file1.txt','r')
    tm=file1.read()[1:len(file1.read())-1].split(',')
    file1.close()
    for it in  range(len(tm)):
        tm[it]=float(tm[it])

    file2=open('file2.txt','w')
    for tl in range(len(rng)):
        file2.write(str(rng[tl])+'\n')
    file2.close()

    file2=open('file2.txt','r')
    h=file2.read()
    rng=h[:len(h)-1].split('\n')
    file2.close()
    for it in  range(len(rng)):
        rng[it]=(rng[it][1:len(rng[it])-1].split(','))
        for ji in range(len(rng[it])):
            rng[it][ji]=int(rng[it][ji].replace("'",''))
    time.sleep(1.2)
#"""

