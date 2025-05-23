def automorphic(num):
	squared = num ** 2
	return str(squared).endswith(str(num))
print(automorphic(5))

def findWords(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = []

    for word in words:
        lower_word = set(word.lower())
        if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
            result.append(word)

    return result


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(findWords(["omk"]))

def decode(s):
	stack = []
	num_stack = []
	curr_str = ""
	num = 0
	for char in s:
		if char.isdigit():
			num = num * 10 + int(char)
		
		elif char == "[":
			stack.append(curr_str)
			num_stack.append(num)
			curr_str = ""
			num = 0

		elif char == "]":
			prev_str, curr_str = stack.pop(), num_stack.pop()
			curr_str = prev_str * curr_str + prev_str
		else:
			curr_str += char
			
	return curr_str
print(decode("3[a]2[bc]"))
print(decode("3[a2[c]]"))
			

def letterCombinations(digits):
    if not digits:
        return []

    digit_to_letters = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = [""]

    for digit in digits:
        new_result = []
        for combination in result:
            for letter in digit_to_letters[digit]:
                new_result.append(combination + letter)
        result = new_result

    return result

print(letterCombinations("23"))

def even_num(lst):
	lst = []
	for i in lst:
		if i not in lst and i % 2 == 0:
			lst.append(i)
		else:
			lst = i
	return lst
print(even_num([3, 2, 6, 4, 1, 8]))

