
#def max_price(prices):
#	min_price = float('inf')
#	max_profit = 0
#	for price in prices:
#		if price < min_price:
#			min_price = price
#		elif price - min_price > max_profit:
#			max_profit = price - min_price
#	return max_profit
#prices = [7, 1, 5, 3, 6, 4]
#print(max_price(prices))






nums = [-4, -1, 0, 3, 10]
n = len(nums)
result = [0]*n
left = 0
right = n - 1
indx = n - 1
while left <= right:
  if abs(nums[left]) > abs(nums[right]):
    result[indx] = nums[left] ** 2
    left += 1
  else:
    result[indx] = nums[right] ** 2
    right -= 1
  indx -= 1
print(result)






def high_avrg_ascii_word(str1):
  words = str1.split()
  max_word = ""
  max_value = 0

  for word in words:
    avg_ascii = sum(ord(c) for c in word) / len(word)
    if avg_ascii > max_value:
      max_value = avg_ascii
      max_word = word
  return max_word
str1 = "hello zoo sun"
print(high_avrg_ascii_word(str1))






#def roman_val(nums):
#	nums = {'I' : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : }
#	prev_val = 0
#	for i in nums:
#		if i < prev_val:
#			prev_val = i
		


def cap_small(str1):
	Capital = 0
	small = 0
	for i in str1:
		if ord(i) >= 65 and ord(i) <= 90:
			Capital += 1
		elif ord(i) >= 97 and ord(i) <= 122:
			small += 1
	return Capital, small
str1 = "HelloWorld"
print(cap_small(str1))
		
