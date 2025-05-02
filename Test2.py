#1
def sum_two(nums, target):
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]
nums = [2, 7, 11, 15]
target = 9
print(sum_two(nums, target))


#2
def is_valid(s):
	while "()" in s or "{}" in s or "[]" in s:
		s = s.replace("()", "").replace("[]", "").replace("{}", "")
	return s == ""
s = "()"
print(is_valid(s))


#3
def campare_triplet(a, b):
	alice, bob = 0, 0
	for i in range(3):
		if a[i] > b[i]:
			alice += 1
		elif a[i] < b[i]:
			bob += 1
	return [alice, bob]
a = [5, 6, 7]
b = [3, 6, 10]
print(campare_triplet(a, b))


#4
def excel_column(columntitle):
  result = 0
  for char in columntitle:
    result = result * 26 + (ord(char) - ord('A') + 1)
  return result
print(excel_column("AA"))


#5
def convert_militarytime(s):
  hour, minutes, seconds_am_pm = s[:-2].split(":")
  am_pm = s[-2:]
  hour = int(hour)
  if am_pm == "AM":
    hour = 0 if hour == 12 else hour
  else:
    hour = hour if hour == 12 else hour + 12
  return f"{hour:02}:{minutes}:{seconds_am_pm}"
print(convert_militarytime("12:01:00AM"))