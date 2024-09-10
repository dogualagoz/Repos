# 1'den 100'e kadar sayıların karelerinin toplamıyla toplamının karesinin farkı

#Önce 1'den 100'e kadarlık bir liste oluşturalım

liste = []
for i in range(1,101):
    liste.append(i)

# Sonra her sayının karesini alıp toplayalım.
kare_toplami = 0
toplamin_karesi = 0
for i in range(1,len(liste)):
    kare_toplami = kare_toplami + liste[i]**2
    toplamin_karesi = toplamin_karesi +liste[i]

sonuc = toplamin_karesi**2 - kare_toplami
print(sonuc)
print(sonuc)
# commit deneme

