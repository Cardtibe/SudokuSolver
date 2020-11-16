import random
"""
gb=[0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0]
Kolay yerleştirmek için boş kopya
"""
gb=[4,0,0,0,9,5,0,0,0,
    1,0,0,6,0,0,8,5,2,
    2,0,0,0,0,0,0,0,7,
    0,9,0,0,0,1,0,2,0,
    0,8,0,0,0,2,9,4,0,
    0,0,0,0,5,3,0,0,0,
    9,0,3,0,0,0,0,0,0,
    0,0,0,4,0,0,1,7,9,
    0,0,6,1,0,0,2,0,0]
gbr=[]
#X in yatay değerini bulur
def ytbul(x):
    if dkbul(x)==9:
        yt=((x-9)/9)+1
    else:
        yt=(x-(dkbul(x)%9))/9+1
    return int(yt)
#X in dikey değerini bulur
def dkbul(x):
    dk=x%9
    return dk
#9 luk alanı bulur
def albul(x):
    al=int(dkbul(x)/3+1)**2+int((ytbul(x)-1)/3)+1
    return al
#Yatay olasılıkları bulur
def ytol(x):
    ytol=[1,2,3,4,5,6,7,8,9]
    for i in range(int(ytbul(x)*9-9),int(ytbul(x)*9)):
        if gb[i]==0:
            continue
        else:
            ytol.remove(gb[i])
    return ytol
#Dikey olasılıkları bulur
def dkol(x):
    dkol=[1,2,3,4,5,6,7,8,9]
    for i in range(dkbul(x)+1,82,9):
        i-=1
        if gb[i]==0:
            continue
        else:
            dkol.remove(gb[i])
    return dkol
#Alanın olasılıkları bulur
def alol(x):
    alol=[1,2,3,4,5,6,7,8,9]
    m=albul(x)
    for i in range(0,81):
        if gb[i]==0:
            continue
        if m==albul(i):
            alol.remove(gb[i])
    return alol
#Değişkene verilen değerli listesiyi yazar
def yaz(l):
    sk=0
    print("|",end="")
    for i in range(0,81):
        if sk==1:
            print("|",end="")
            sk=0
        print(l[i],end=" ")
        if i%9==8:
            print("")
        if (i+1)/3==int((i+1)/3):
            if i % 27 == 26:
                print("--------------------")
                sk=1
            else:
                print("|",end="")
#Olabileceklerin 3 listesinin ortak elemanı 1 tane ise yerleştirir(Kesin o sayı oraya gideceği için)
a=0
while a<500:
    a+=1
    print(a)
    for i in range(0,81):
        thol=[]
        if gb[i]!=0:
            continue
        thol=list(set(dkol(i)).intersection(list(set(alol(i)).intersection(ytol(i)))))
        if len(thol)==1:
            gb[i]=thol[0]
gbr=gb
#Olabilecek olasılıkları hesaplayıp, o olasılıklar arasından rastgele yerleştirerek bulur.
#Üstte kesin olanları yerleştirdi şimdi eğer çözemediyse kesinleri kullanarak rastgele yerleştiriyor(Tabiki kesinlerin yerleştirilmiş haline)
x=0
while 0 in gbr:
    gbr = gb
    x+=1
    print("Deneme: ",x)
    for i in range(0,81):
        sll=[]
        if gbr[i]!=0:
            continue
        sll=list(set(dkol(i)).intersection(list(set(alol(i)).intersection(ytol(i)))))
        r=random.randint(0,len(sll))
        try:
            gb[i] = sll[r-1]
        except:
            break
#gbr listesini yazdırır
yaz(gbr)
sss=input("")
