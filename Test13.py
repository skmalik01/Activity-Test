def numberofburger(tomatoslices, cheeseslices):
	if tomatoslices % 2 != 0:
		return []
	jumbo = (tomatoslices - 2 * cheeseslices) // 2
	small = cheeseslices - jumbo
	if jumbo < 0 or small < 0:
		return []
	return [jumbo, small]
tomatoslices = 16
cheeseslices = 7
print(numberofburger(tomatoslices, cheeseslices))


def max_sum(arr):
	n = len(arr)
	dp0 = arr[0]
	dp1 = 0
	max_sum = 0
	for i in range(n):
		dp0 = max(dp0, dp1 + arr[i])
		dp1 = max(arr[i], dp0)
		max_sum = max(max_sum, dp0, dp1)
	return max_sum
arr = [1, -2, 0, 3]
print(max_sum(arr))
		

			
		