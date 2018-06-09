limit = 1000000
i = 1
final_sequence = []
j_used = 0
while i < limit:
    sequence = []
    j = i
    while j != 1:
        if j % 2 == 0:
            j = j / 2
            sequence.append(j)
        else:
            j = 3 * j + 1
            sequence.append(j)
    if len(sequence) > len(final_sequence):
        final_sequence = sequence
        j_used = i
    i += 1

print j_used
