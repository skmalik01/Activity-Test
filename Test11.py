def is_not_leap_year(year):
	result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
	if result != year:
		return True
	else:
		return False

print(is_not_leap_year(2023))

def count_divisible(n):
	count = 0
	for i in str(n):
		digits = int(i)
		if digits != 0 and n % digits == 0:
			count += 1
	return count
print(count_divisible(111))

def plus_one(digits, index=None):
	if index is None:
		index = len(digits) - 1
	if index < 0:
		return [1] + digits
	if digits[index] == 9:
		digits[index] = 0
		return plus_one(digits, index - 1)
	else:
		digits[index] += 1
		return digits
print(plus_one([9, 9, 9]))

def valid_parenthesis(n):
	result = []
	def inner(current, open_count, closed_count):
		if len(current) == 2 * n:
			result.append(current)
			return
		if open_count < n:
			inner(current + "(", open_count + 1, closed_count)
		if closed_count < open_count:
			inner(current + ")", open_count, closed_count + 1)
	inner("", 0, 0)
	return result

print(valid_parenthesis(2))

def automorphic(n):
	sqr = n * n
	return str(sqr).endswith(str(n))
print(automorphic(25))
