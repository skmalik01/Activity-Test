#def time_in_words(h, m):
#	words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "tweleve", "thirteen"
#		"fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive", "twentysix", "twentyseven", twentyeight", "twentynine"]
#	if m == 0:
#		return f"{words[h]} o clock"
#	elif h == 15:
#		return f"{words[h] quater o clock"
#	elif h == 25:
#		return f"{words[h] quarter

def sum_of_arr(arr, k):
	count = 0
	n = len(arr)
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] + arr[j]) % k == 0:
				count += 1
	return count
arr = [1, 2, 3, 4, 5, 6]
k = 5
print(sum_of_arr(arr, k)) 



def sort_by_freq(inp):
	freq = {}
	output = []	
	for i in inp:
		if i not in freq:
			freq[i] = 1
		else:
			freq[i] += 1
	result = sorted(freq.items(), key=lambda freq : freq[1], reverse=True)
	s = dict(result)
	for j, k in s.items():
		for m in range(k):
			output.append(j)
	return output
inp = [4, 4, 1, 2, 2, 2, 3]
print(sort_by_freq(inp))



n = 6
for i in range(n + 1):
	space = (n - i) // 1
	print(space * " " + "#" * i)

def climb_stairs(n):
	count = 0
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		climb_stairs(n - 1)
		count += 1
	return count
n = 3
print(climb_stairs(n))

