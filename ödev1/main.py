import math
taylor=1
terim=int(input("Terim sayisini giriniz: "))
for i in range(1,terim+1,2):
    faktoriyel=math.factorial(i+1)
    bol=((math.pi/5)**(i+1))
    taylor-=(bol/faktoriyel)
deger_gercek=math.cos(math.pi/5)
kesme_hatasi=deger_gercek-taylor

print(f"{deger_gercek} gercek degeri ")
print(f"{kesme_hatasi} kesme hatasi ")