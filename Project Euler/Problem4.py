# 3 basamaklı sayıların çarpımından oluşan en büyük palindrome sayısı
# Palindrome sayısı tersten ve düzden okunuşu aynı olan sayılar
987789

def check_palindrome(x):
    str_x = str(x)
    ters_x = str_x[::-1]
    if str_x == ters_x:
        return True
    else:
        return False

max_palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        if check_palindrome(i*j) and i*j > max_palindrome:
            a = i
            b = j
            max_palindrome = i*j
print(max_palindrome,a,b)
print("sonuc")