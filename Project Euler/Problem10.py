#2 milyonun altındaki asal sayıların toplamı


def asal_check(x):
    if x == 2:
        return True
    elif x == 1:
        return False
    elif x % 2 == 0:
        return False
    else:
        for i in range(3,int(x**0.5)+1):
            if x % i == 0:
                return False
        return True


toplam = 0
for i in range(1,2000000):
    if asal_check(i):
        toplam +=i

print(toplam)

