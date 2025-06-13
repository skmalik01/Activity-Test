def balancedStringSplit(s):
    count = 0
    balance = 0
    
    for char in s:
        balance += 1 if char == 'R' else -1
        if balance == 0:
            count += 1
    
    return count
print(balancedStringSplit("RLRRLLRLRL"))  
print(balancedStringSplit("RLRRRLLRLL"))

def countsubstring(s):
	n = len(s)
	count = 0
	for i in range(n):
		for j in range(i, n):
			if s[i] == s[j]:
				count += 1
	return count 
print(countsubstring("abcab"))
print(countsubstring("aaa"))  
	
def findlonely(nums):
	count = {}
	for num in nums:
		count[num] = count.get(num, 0) + 1
	lonely_num = [num for num in nums if count[num] == 1 and num - 1 not in count and num + 1 not in count]
	return lonely_num
print(findlonely([10,6,5,8]))
print(findlonely([1,3,5,3])) 

def add_num(a, b):
  	max = 0xF
  	mask = 0xF
  	while b != 0:
    		carry = (a & b)
    		a = (a ^ b) & mask
    		b = (carry << 1) & mask
  	return a if a <= max else ~(a ^ mask)
print(add_num(1, 2))
print(add_num(-2, 3))

def count_number_without_digit(n, d):
    d = str(d)
    return sum(1 for num in range(1, n + 1) if d not in str(num))

print(count_number_without_digit(20, 1))  
print(count_number_without_digit(100, 3)) 
