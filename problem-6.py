#imports
from math import sqrt

n = 1
sum_of_squares = 0
square_of_sums = 0

while n <= 100:
	sum_of_squares += n**2
	square_of_sums += n
	n += 1

square_of_sums = square_of_sums**2
difference = square_of_sums - sum_of_squares
print("The difference of the square of sums and the sum of squares is:",difference)		
