#4 Milyondan küçük Fibonacci sayılarından çift olanların toplamı


#ilk Fibonacci listemizi oluşturalım
fibonacci  = [1,2]
i = 2

while True:
    if fibonacci[i-1] + fibonacci[i-2] < 4000000:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        i+=1
    else:
        break

#Çift olanları ayıralım
sum = 0
for i in fibonacci:
    if i % 2 == 0:
        sum +=i

print(sum)