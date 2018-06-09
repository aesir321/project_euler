result = 0
for i in xrange(1,1000):
    if i % 3 == 0 and i % 5 == 0:
        result += i
        continue
    if i % 3 == 0:
        result += i
    if i % 5 == 0:
        result += i
        
print "The result is:",result
    