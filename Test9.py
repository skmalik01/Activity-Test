def flatten_dict(d, parent_key=""):
	items = {}
	for k, v in d.items():
		new_key = parent_key + k
		if isinstance(v, dict):
			items.update(flatten_dict(v, new_key))

		else:
			items[new_key] = v
	return items
nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        }
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)


import re
def max_numeric(s):
  numbers = re.findall(r'\d+', s)
  int_num = [int(num) for num in numbers]
  return max(int_num)
s = "100klh564abc365bg"
print(max_numeric(s))

def pair_exists(arr, x):
	seen = set()
	for i in arr:
		if x - i in seen:
			return True
		seen.add(i)
	return False
arr = [1, 4, 45, 6, 10, 8]
x = 16
print(pair_exists(arr, x))

def goodies(a, n):
	total_goodies = sum(a)
	required = n * (n + 1) // 2
	return total_goodies == required
n = 5
a = [7, 4, 1, 1, 2]
print(goodies(a, n))

def distinct_substring(s, k):
	n = len(s)
	count = 0
	for i in range(n):
		char = {}
		for j in range(i, n):
			char[s[j]] = char.get(s[j], 0) + 1
			if len(char) == k:
				count += 1
			elif len(char) > k:
				break
	return count
print(distinct_substring("pqpqs", 2))
print(distinct_substring("aabab", 3))
print(distinct_substring("abcba", 2))
