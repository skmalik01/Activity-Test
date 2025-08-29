def missing_num(l1):
	for i in range(min(l1),max(l1)):
		if i not in l1:
			return i
	else:
		return 0
print(missing_num([2, 3, 1, 5]))
		


def two_sum(nums, target):
	n = len(nums)
	result = []
	for i in range(n):
		for j in range(i + 1, n):
			if nums[i] + nums[j] == target:
				return [i, j]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))


def is_valid(s):
	while "()" in s or "{}" in s or "[]" in s:
		s = s.replace("()","")
		s = s.replace("{}","")
		s = s.replace("[]","")
	return True if not s else False
print(is_valid("()]{}"))