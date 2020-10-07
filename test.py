tm=[0.002239511970149254]
rng=[[0,400]]
#"""
file1=open('file1.txt','w')
file1.write(str(tm))
file1.close()
file1=open('file1.txt','r')
tm=file1.read()[1:len(file1.read())-1].split(',')

file1.close()
for it in  range(len(tm)):
    tm[it]=float(tm[it])
print(tm)
file2=open('file2.txt','w')
for tl in range(len(rng)):
    file2.write(str(rng[tl])+'\n')
file2.close()

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
print(rng)
#print((rng[0][1:len(rng[0])-1].split(',')))

#"""    
#'''
for i in range(100):
    print('\n\n',tm,'\n',rng)
    sptc=int(input('sptc='))
    end2=int(input('end2='))
    s=sptc#int(input('s='))
    tmo=0
    tmno=0
    for i in range(len(rng)):
        print(rng[i][len(rng[i])-1])
        if s>=rng[i][0] and s<rng[i][1] and s!=(rng[i][len(rng[i])-1])-1:
            print('in',i)
            tmo=tm[i]
            tmno=i
            break

    
    if sptc>end2 and end2!=0 and tmo!=0:
        tem=[sptc,rng[tmno][1]]
        rng[tmno][1]=sptc
        s1=s-(end2-sptc)
        print((tmo*s),s1)
        tm.append((tmo*s)/s1)
        rng.append(tem)
    if sptc<end2 and end2!=0 and tmo!=0:
        s1=s+(end2-sptc)
        tm[tmno]=(tmo*s)/s1
        
        
    
    input('\n\n'+str(tm)+'\n'+str(rng))
    
#'''           
            
