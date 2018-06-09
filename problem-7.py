#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.

#What is the 10001st prime number?

from eulermath import is_prime
import time

number_prime_to_find = 10001
prime_count = 1
i = 3

t0 = time.time()
while True:
    if is_prime(i):
        prime_count += 1
        if prime_count == number_prime_to_find:
            break
    i += 2
t1= time.time()
print "The " + str(number_prime_to_find) + "th prime is",i
print t1-t0