kok=2
us=-0.5
interasyon=int(input("iterasyon sayisi: "))
for i in range(0,interasyon):
    pay=(4*(2.71**(us*kok))-kok)
    payda=(4*(2.71**(us*kok))(-1/2)-1)
    kok=kok-(pay/payda)
print(kok)

print(4*(2**(us*0.01778))-0.1778)