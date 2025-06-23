def ispower(n):
  if n <= 0:
    return False
  while n % 4 == 0:
    n //= 4
  return n == 1
print(ispower(16))


def permut(s1, s2):
  from itertools import permutations
  permit = ["".join(x) for x in permutations(s1, len(s1))]
  return any(x in s2 for x in permit)
print(permut("ab", "eidbaooo"))


def trailingzero(n):
  count = 0
  while n >= 5:
    n //= 5
    count += n
  return count
print(trailingzero(5))


def replace_elements(arr):
    max_so_far = -1
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_so_far
        max_so_far = max(max_so_far, current)
    return arr
print(replace_elements([17,18,5,4,6,1]))


def unique_morse(words):
    morse_code = [
        ".-","-...","-.-.","-..",".","..-.","--.","....","..",
        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
        "...","-","..-","...-",".--","-..-","-.--","--.."
    ]
    
    seen = set()
    for word in words:
        transformed = ''.join(morse_code[ord(c) - ord('a')] for c in word)
        seen.add(transformed)
    
    return len(seen)
words = ["gin", "zen", "gig", "msg"]
print(unique_morse(words))
			