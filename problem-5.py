#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number_to_test = 20 #Number has to at least be as a big as the largest number.
i = 2 #Everything is evenly divisible by 1.
is_evenly_divisible = False
		
while is_evenly_divisible == False:
	while i <= 20:
		if number_to_test % i != 0:
			i = 2
			number_to_test += 20
		else:
			if i == 20: #All numbers were divisible
				is_evenly_divisible = True
				break #Breaks out of the smallest enclosing for or while loop
			i += 1
			continue #Continues the next iteration of the for or while loop			
	
print "The smallest number evenly divisible by numbers 1 to 20 is:",number_to_test
