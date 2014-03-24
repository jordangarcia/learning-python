from math import floor, sqrt

def is_prime(num):
	vals = []
	for x in range(2, int(floor(sqrt(num)) + 1)):
		if num % x == 0:
			return False
	return True

class Primes:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def next(self):
		ret = 1
		while True:
			if self.current > self.high:
				raise StopIteration
			elif is_prime(self.current):
				ret = self.current
				break
			else:
				self.current += 1

		self.current += 1
		return ret
