import math


# n*(n+1)/2 nin sonucu n. üçgensel sayı olur
#bolen sayısı 500den fazla olan ilk üçgensel sayıyı yazdır
def bolen_sayisi(x):
    sayac = 0
    for i in range(1,x+1):
        if x%i == 0:
            sayac += 1
        else:
            continue
    return sayac

print(bolen_sayisi(10))            

n = 1
while True:
    number = 0
    for i in range(1,n+1):
        if bolen_sayisi(number)>500:
            print(int(number))
            break
    n+=1    
        