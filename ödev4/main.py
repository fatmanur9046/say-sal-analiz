kok=1
h=0.2
a=2.71
b=4*(2.71**(kok+h))
c=2.71**(kok+(2*h))
c2=2.71**(kok-(2*h))
b2=4*(2.71**(kok-h))
ileri=(1/(2*h))*(-3*a + b - c)
geri=(1/(2*(-h)))*((-3*a) + b2 - c2)
merkezi=(1/(2*h))*((a**(kok+h)) - (a**(kok-h)))
gercekdeger=2.71*kok
print(f"ileri: {ileri}")
print(f"geri:  {geri}")
print(f"merkezi:  {merkezi}")
print(f"gercekdeger:  {gercekdeger}")
print("gercek degere en yakin deger merkezi degerdir")

#3-a h=0.1 için
h1=0.1
kok1=1
ileri=(1/(2*h1))*(-3*(kok**3) + 4*((kok+h1)**3) - kok+((2*h1)**3))
geri=(1/(2*(-h1)))*(-3*(kok**3) + 4*((kok-h1)**3) - kok+((2*(-h1))**3) )
merkezi=(1/(2*h1))*(((kok+h1)**3) - ((kok-h1)**3))
gercekdeger=kok**3
print(f"hata1: {abs(ileri-gercekdeger)}")
print(f"hata2: {abs(geri-gercekdeger)}")
print(f"hata3: {abs(merkezi-gercekdeger)}")
#3-a h=0.2 için
h2=0.2
kok1=1
ileri=(1/(2*h2))*(-3*(kok**3) + 4*((kok+h2)**3) - kok+((2*h2)**3))
geri=(1/(2*(-h2)))*(-3*(kok**3) + 4*((kok-h2)**3) - kok+((2*(-h2))**3) )
merkezi=(1/(2*h2))*(((kok+h2)**3) - ((kok-h2)**3))
gercekdeger=kok**3
print(f"hata1: {abs(ileri-gercekdeger)}")
print(f"hata2: {abs(geri-gercekdeger)}")
print(f"hata3: {abs(merkezi-gercekdeger)}")

