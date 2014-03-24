# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import floor, sqrt
from prime_iterator import Primes

def factor(num):
	factors = []

	while True:
		for p in Primes(2, num):
			if num % p == 0:
				print p
				num = num / p
				factors.append(p)
				print num, factors
				break

		if num == 1:
			return factors

print factor(600851475143)
