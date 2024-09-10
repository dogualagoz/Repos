#10001. asal sayı bulma
import math
def asal_check(x):
    asal_mi = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            asal_mi = False
            continue
    if x == 1:
        return False
    return asal_mi

sayac = 0
sayi = 2
while True:
    if asal_check(sayi):
        sayac += 1
    if sayac == 10001:
        print(sayi)
        print(sayac)
        break

    sayi += 1

