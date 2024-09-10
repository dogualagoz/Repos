# Bir zincir oluşturcaz
# Başlangıç sayısı çift ise ikiye bolcez tek ise üçle carpıp 1 eklicez
# Böylelikle 1 olana kadar sayımız devam edecek
# 13 ten başlayınca 13-40-20-10-5-16-8-4-2-1 şeklinde devam ediyor 10 adım sürüyor.
# Zincir başladıktan sonra sayılar 1 milyonu geçebilir problem yok
# Hangi 1 milyonun altındaki sayı en uzun zincire sahip






def terim_dongusu(x):
    sayac = 0
    while x!=1:
        if x%2 == 0:
            x = x/2
            sayac+=1
        else:
            x = 3*x+1
            sayac +=1
    return sayac+1

for i in range(1,1000001):
    

