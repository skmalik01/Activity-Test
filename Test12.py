def text_editor(operations):
	stack = []
	for op in operations:
		if op.startswith("type"):
			_, char = op.split()
			stack.append(char)
		elif op == "undo" and stack:
			stack.pop()
		elif op == "undo" and op == "redo":
			stack.append(char)
	return "".join(stack)
operations = ["type a", "type b", "undo", "type c", "redo"]
print(text_editor(operations))



def word_wrapping(sentence, max_length):
	words = sentence.split()
	current_word = ""
	chunk = []
	for word in words:
		if current_word == "":
			current_word = word
		elif len(current_word) + 1 + len(word) <= max_length:
			current_word += " " + word
			chunk.append(current_word)
			
	if current_word:
		chunk.append(current_word)
	return chunk
sentence = "Hello! This is a sample input, which must be split correctly."
max_length = 20
print(word_wrapping(sentence, max_length))


def forum_threading(posts):
	children = {}
	roots = []
	for p in posts:
		parent = p.get("reply_to")
		if parent:
			children.setdefault(parent, []).append(p["post_id"])
		else:
			roots.append(p["post_id"])
	def build_thread(mid):
		thread = [mid]
		while children.get(mid):
			mid = children[mid][0]
			thread.append(mid)
		return thread
	return [build_thread(root) for root in roots]
posts = [
{"post_id": "A", "user": "tom", "reply_to": None},
{"post_id": "B", "user": "jerry", "reply_to": "A"},
{"post_id": "C", "user": "anna", "reply_to": None},
{"post_id": "D", "user": "tom", "reply_to": "C"},
{"post_id": "E", "user": "jerry", "reply_to": "B"}
]
print(forum_threading(posts))