# 1 den 20 ye kadar tüm sayılara kalansız bölünebilen sayı


# Önce 1'den 20 ye kadar bölünebilip bölünemediğini kontrol eden bir fonksiyon yazalım
def kontrol_et(x):
    for i in range(1,21):
        if x % i != 0:
            return False
    return True
# Sonra sonsuz bir döngü olalım aradığımız sayıyı bulunca döngü kırılsın
a = 1
while True:
    if kontrol_et(a):
        print(a)
        break
    a = a+1