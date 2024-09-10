# Pisagor Sorusu.
# a<b<c olacak
# a^2 + b^2 = c^2
# a+b+c = 1000
#a*b*c yi bul


for a in range(1,1001):
    for b in range(a,1001):
        c = (a**2 + b**2)**0.5
        if c.is_integer() and c<1000:
            if a+b+c == 1000:
                print(a*b*c)





