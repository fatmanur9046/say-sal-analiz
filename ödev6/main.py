def f(x,y):
    return (x*y)*(1+x)


a=1
b=2
c=1
d=3
delta_x=(b-a)/3
delta_y=(d-c)/2
sonuc=0
sonuc+=((delta_x/2)*(delta_y/2))*(f(a,c)+f(b,c)+(2*((f(a+delta_x,c)+f(a+(2*delta_x),c))))+
           f(a,d)+f(b,d)+(2*((f(a+delta_x,d)+f(a+(2*delta_x),d))))+
           (2*((f(a,c+delta_y)+f(b,c+delta_y)+f(a+delta_x,c+delta_y)+f(a+(2*delta_x),c+delta_y)))))
print(sonuc)

