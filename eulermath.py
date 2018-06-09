def generate_fibonacci_number(self):
    """Generates the specified number in the fibonacci sequence up.  Recursive
    implementation, not efficient.

    self -: The number position in the sequence to generate.

    """

    if self == 0: return 0
    elif self == 1: return 1
    else: return generate_fibonacci_number(self - 1) + generate_fibonacci_number(self - 2)

def get_list_of_prime_numbers(limit):
    """Returns a list of prime numbers up to a specified limit which is sent as
    an argument.  This is a Sieve of Eratosthenes implementation and is not an
    efficient method.

    limit -: This the integer value you would like to calculate prime numbers
    up to.  It is inclusive.

    """
    if limit < 2: return []
    if limit == 2: return [2]
    prime_candidates = range(2, limit, 2)

    for i in prime_candidates:
        for j in prime_candidates:
            if i != j and j % i == 0:
                prime_candidates.remove(j)
    return prime_candidates

def primes(n):
    """
    returns a list of prime numbers from 2 to n
    """
    if n < 2:  return []
    if n == 2: return [2]
    # create a list of odd numbers from 3 to n
    nums = list(range(3, n + 1, 2))
    nums_len = (n // 2) - 1 + (n % 2)
    idx = 0
    idx_sqrtn = (int(n**0.5) - 3) // 2
    while idx <= idx_sqrtn:
        nums_idx = (idx << 1) + 3
        for j in range(idx * (nums_idx + 3) + 3, nums_len, nums_idx):
            # if not a prime replace with zero
            nums[j] = 0
        idx += 1
        while idx <= idx_sqrtn:
            if nums[idx] != 0:
                break
            idx += 1
    # remove all the zero entries
    return [2] + [x for x in nums if x != 0]

def get_prime_factors(number_to_factorise):
	"""Writes out the prime factors of a given number.

	number_to_factorise -: This is an integer value that the prime factors will
    be calculated for.

    """

	prime = 2
	while prime * prime <= number_to_factorise:
		if number_to_factorise % prime == 0:
			print number_to_factorise
			number_to_factorise /= prime
		else:
			prime += 1
	print prime

def is_even(number_to_test):
	"""Returns a boolean indicating whether a given number is true or false.
    Returns True if the number is even and False if the number is odd.

	number_to_test -: This is a number to test to see whether it is even or odd.

    """

	is_even = False
	if number_to_test % 2 == 0:
		is_even = True
	return is_even

def is_palindromic_number(number):
	"""Returns a boolean indicating whether a given number is a palindrome.
    Returns True if the number is a palindrome and False if a number if number
    is not.

	number -: An integer value.

    """

	is_palindromic = False
	string_temp = str(number)
	if string_temp == string_temp[::-1]:
		is_palindromic = True
	return is_palindromic

def is_prime(self):
    """Returns a boolean value indicating whether the number is prime or not.
    Returns True if the number is prime, returns False if the number is not
    prime.  Brute force method.  Considers 1 to not be prime.

    self -: The integer number to test.

    """

    is_prime = True
    root = self**0.5

    if self < 2:
        is_prime = False
    elif self == 2:
        is_prime = True #Try pass
    else:
        i = 3
        while i <= root:
            if self % i == 0:
                is_prime = False
            i += 2

    return is_prime
