# En büyük asal çarpanı kaçtır
import math
num = 600851475143

# Asal olup olmadığını kontrol eden bir fonksiyon yazalım.
def asal_check(x):
    asal_mi = True
    for i in range(2,int(math.sqrt(x) + 1)):
        if x % i == 0:
            asal_mi = False
            continue
    if x== 1:
        return False
    return asal_mi
# Burada asal çarpanların listesini tutuyoruz
carpanlar = []
for i in range(2,int(math.sqrt(num))):
    if num % i == 0 and asal_check(i):
        carpanlar.append(i)
    else:
        continue
# Burada da listenin son elemanı olan en büyük asal çarpanı yazdırıyoruz
son_eleman = len(carpanlar)
print(carpanlar[son_eleman-1])


