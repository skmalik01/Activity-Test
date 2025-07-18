def odd_frequency(num):
	result = 0
	for i in num:
		result ^= i
	return result
print(odd_frequency([4, 5, 6, 4, 6, 6, 5, 4, 4]))

def remove_duplicate(input):
  from collections import Counter
  all_values = [item for sublist in input.values() for item in sublist]
  value_count = Counter(all_values)

  result = {}
  for key, val_list in input.items():
    unique_val = [val for val in val_list if value_count[val] == 1]
    result[key] = unique_val
  return result
input = {'Ravi': [2, 3], 'Sita': [3, 4, 5]}
print(remove_duplicate(input))

def max_budget(arr1, k):
  arr1.sort()
  count = 0
  for price in arr1:
    if price <= k:
      k -= price
      count += 1
    else:
      break
  return count
print(max_budget([15, 20, 10, 5, 100, 30], 60))

def split_str_with_vowels(str1):
  import re
  result = list(filter(None, re.split(r'[aeiouAEIOU]', str1)))
  return result
print(split_str_with_vowels('CodeWithMe'))

def row_count(matrix):
  from collections import Counter
  row_length = [len(row) for row in matrix]
  length_freq = dict(Counter(row_length))
  return length_freq 
matrix = [[[1, 2], [3, 4, 5], [6], [7, 8], [9, 10, 11], [12]]]
print(row_count(matrix))
	