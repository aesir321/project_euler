from eulermath import is_prime, get_list_of_prime_numbers, primes
import time

limit = input("What is the limit you want to calculate primes to:")
t0 = time.time()
sum = 0
for i in primes(limit):
    sum += i
t1 = time.time()

print "The sum of the primes up to", limit, "is:",sum
print t1-t0