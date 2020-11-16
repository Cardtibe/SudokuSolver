


gb=[0,0,0,0,0,0,6,1,9,
    0,2,3,0,9,0,0,0,0,
    0,0,0,1,4,0,0,2,0,
    0,0,9,0,0,0,0,0,0,
    7,0,8,0,0,3,0,0,0,
    0,0,0,0,0,5,3,4,0,
    0,0,0,0,0,0,4,6,7,
    8,3,0,0,0,0,0,0,0,
    0,0,0,6,1,2,0,0,0,]


for ctd in range(0,81):
    #eğer doluysa kare geç
    if gb[ctd]!=0:
        continue
    #yatay dikey listesini sıfırla
    ytol=[1,2,3,4,5,6,7,8,9]
    dkol=[1,2,3,4,5,6,7,8,9]

    #yatay dikey bul
    dk=int(ctd%9+1)
    if ctd<9:
        yt=1
    else:
        yt=int((ctd-dk+1)/9)
    #yatay olasılıkları
    for i in range(0,9):
        try:
            ytol.remove(gb[(ctd-dk+1)+i])
        except:
            boos=0
    #dikey olasılıkları
    for i in range(1,10):
        try:
            dkol.remove(ctd%9*i)
        except:
            boos=0
    #alan olasılık bul
    def alol():
        alol = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            if int(yt/3)==1 and int(dk/3)==1:
                print("alan1")

    alol()
    print(alol)
for i in range(0,81):
    #ekrana sonucu yazdır    
    if int(i%9+1)==9:
        print(gb[i])
    else:
        print(gb[i],end="")





