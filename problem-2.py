even_sum = 0
current_number = 2
previous_number = 1

while current_number < 4000000:
    if not (current_number % 2):
        even_sum += current_number
    temp = previous_number
    previous_number = current_number
    current_number += temp

print even_sum

