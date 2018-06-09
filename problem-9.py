#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 9 + 16 = 25

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def cvalue(a,b):
    temp = ((a**2 + b**2)**0.5)
    if not(temp) % int(temp) == 0:
        return False
    return temp

count = 1
for i in range(1,501):
    for j in range(1,251):
        a = count
        b = j
        c = cvalue(a,b)
        abc2 = a + b + c
        if abc2 == 1000:
            print a * b * c
    count += 1
