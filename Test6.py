def Reorder(num):
  if num == 1:
    return True
  n = str(num)
  from itertools import permutations
  a = list(int(("".join(x))) for x in permutations(n))
  if all(x % 2 == 0 for x in a):
    return True
  else:
    return False
print(Reorder(1))
print(Reorder(10))
print(Reorder(46))


def check_palindrome(s):
  for i in range(len(s)):
    temp = s[:i] + s[i + 1::]
    if temp == temp[::-1]:
      return True
  return s == s[::-1]

print(check_palindrome("abca"))
print(check_palindrome("racecar"))
print(check_palindrome("abc"))


def can_construct(ransomNote, magazine):
	if len(ransomNote) > len(magazine):
		return False
	flip1 = set(ransomNote)
	flip2 = set(magazine)
	alt1 = flip1 == flip2 or flip2.isubset(flip1) or flip1[:] == flip2[::-1]
	if alt1:
		return True
	return False
print(can_construct("aabbcc", "abcabc"))


from datetime import datetime

def min_days_between_dates(date_list):
    dates = [datetime.strptime(date, "%d-%m-%Y") for date in date_list]
    dates.sort()
    min_diff = min((dates[i] - dates[i-1]).days for i in range(1, len(dates)))
    return min_diff
date_list = ["12-05-2022", "15-05-2022", "20-06-2022"]
print(min_days_between_dates(date_list))


def sum_of_numbers(s):
    total = 0
    num = ""

    for ch in s:
        if ch.isdigit():
            num += ch
        else:
            if num:
                total += int(num)
                num = ""

    if num:
        total += int(num)

    return total
print(sum_of_numbers("abc12xy34"))
print(sum_of_numbers("a1b2c3"))
print(sum_of_numbers("100apples20bananas"))
		
			