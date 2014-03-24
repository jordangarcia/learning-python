# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(num):
	chars = list(str(num))
	for i in range(0, int(len(chars) / 2)):
		if chars[i] != chars[len(chars) - i - 1]:
			return False
	return True

class ProductOf:
	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2 + 1

	def __iter__(self):
		return self

	def next(self):
		if self.n1 == 0:
			raise StopIteration
		elif self.n2 > 0:
			self.n2 -= 1
		elif self.n2 == 0:
			self.n1 -= 1
			self.n2 = self.n1
		return self.n1, self.n2, self.n1 * self.n2

largest = (0,0,0)
for n1, n2, product in ProductOf(999, 999):
	if is_palindromic(product) and product > largest[2]:
		largest = (n1, n2, product)

print largest
