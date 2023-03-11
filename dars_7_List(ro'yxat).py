# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:14:14 2023

@author: admin
"""

mevalar=['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar)
narxlar=[1200,18000,10900,22000] # narxlar ro'yxati (sonlar)
sonlar=['bir','ikki',3,4,5] # sonlar va matnlar aralash ro'yxati
ismlar=[] # bo'sh ro'yxat
print(mevalar)
print(narxlar)
print(sonlar)
print(ismlar)
mevalar=['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar)
print('Birinchi meva:', mevalar[1])
print('Ikkinchi meva:', mevalar[0])


mevalar=['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar)
print('Birinchi meva:', mevalar[1].upper())
print('Ikkinchi meva:', mevalar[0].title())
narxlar=[1200,18000,10900,22000] # narxlar ro'yxati (sonlar)
print(narxlar[3] - narxlar[0])
mevalar=['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar
print(mevalar[-1])

narxlar=[1200,18000,10900,22000] # narxlar ro'yxati (sonlar)
narxlar[1]=25000
print(narxlar)
mevalar=['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar)
mevalar.append('banan')
narxlar=[1200,18000,10900,22000] # narxlar ro'yxati (sonlar)
narxlar.append(42000)
print(mevalar)
print(narxlar)
ismlar=[] # bo'sh ro'yxat yaratamiz!
ismlar.append('abbos')
ismlar.append('jalol')
ismlar.append('maftuna')
print(ismlar)
ismlar=['abbos', 'jalol', 'maftuna']
ismlar.insert(3,'gulshoda')
print(ismlar)
ismlar=['abbos', 'jalol', 'maftuna', 'gulshoda']
del ismlar[2]
print(ismlar)   
narxlar=[1200,18000,10900,22000] # narxlar ro'yxati (sonlar)
narxlar.remove(18000) 
print(narxlar)
bozorliklar= ['olma','anjir','shaftoli',"o'rik"] 
mahsulot=bozorliklar.pop(1)
print('Men bozordan',mahsulot,'oldim')
print('Olinmagan mahsulotlar:',bozorliklar )
Dostlar=['Abror','Jasur','Sardor','Gulmira']
Royxat=Dostlar.pop(3)
print('Men',Royxat.upper(),'ni tug\'ilgan kunimga chaqirmadim') 
print(Dostlar, 'ni chaqirdim.\nBir mazza qilib o\'tiraylik dedimdaaa.')
t_yil=int(input('Tug\'ilgan yilingizni kiriting:'))
yosh=2023-t_yil
print("Siz",str(yosh),"da siz")    
# do'stlarni yoshini aniqlaymiz!!!
print("Assalomu Alaykum, Qadirli yurtdoshlar!!!\nKeling do\'stlaringiz nechchi yoshdaligini aniqlaymiz!!!")
print("Do\'stlaringiz:")
dostlar=["Jamol","Sanjar","Islom"]

print(dostlar)
t_yil=int(input("Tug\'ilgan yilingizni kiriting:"))
yosh=2023-t_yil
print("Siz",str(yosh),"da siz!!!")
dostlar=[]
dostlar.append("Mirjalol")
dostlar.append("Davrbek")
dostlar.append("Bobur")
print(dostlar)
dostlar=['Mirjalol', 'Davrbek', 'Bobur']
dostlar.remove("Davrbek")
print(dostlar)
dostlar=['Mirjalol', 'Davrbek', 'Bobur']
dostlar.insert(3,"Davrbek")
print(dostlar)


