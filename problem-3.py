#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from eulermath import *
    
number_to_find_factors = int(raw_input("Please enter a number to find its prime factors: "))
prime_factors = get_prime_factors(number_to_find_factors)
print prime_factors