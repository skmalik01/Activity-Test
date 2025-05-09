from itertools import permutations

def check(s):
	return [" ".join(m) for m in permutations(s)]
s = "abc"
print(check(s))

def move_zero(nums):
  	count = 0
  	for num in nums:
    		if num != 0:
      			nums[count] = num
      			count += 1
  	for i in range(count, len(nums)):
    		nums[i] = 0

nums = [0, 1, 0, 3, 12]
move_zero(nums)
print(nums)

def check_toeplitz(matrix):
  	row, col = len(matrix), len(matrix[0])

  	for i in range(row - 1):
    		for j in range(col - 1):
      			if matrix[i][j] != matrix[i + 1][j + 1]:
        			return False
  	return True
matrix = [
  [1, 2, 3, 4],
  [5, 1, 2, 3],
  [9, 5, 1, 2]
]
print(check_toeplitz(matrix))


def arithmetic(arr):
	count = 0
	arr.sort()
	n = len(arr)
	diff = arr[1] - arr[0]
	for i in range(1, n):
		if arr[i] - arr[i - 1] != diff:
			return False
	return True
arr = [3, 5, 1]
print(arithmetic(arr))


def kthSmallest(matrix, k):
    	nums = []
    	for row in matrix:
        	for num in row:
            		nums.append(num)
    	nums.sort()
    	return nums[k - 1]

matrix = [
  [1, 5, 9],
  [10, 11, 13],
  [12, 13, 15]
]
k = 8
print(kthSmallest(matrix, k))