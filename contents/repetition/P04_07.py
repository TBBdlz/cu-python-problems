"""
	P04-07: Interested word counter
"""

keyword: str = input()
sentence: str = input()
first_char = keyword[0]
num_word: int = 0

for i in range(len(sentence)):
    if first_char == sentence[i]:
        if sentence[i:i+len(keyword)] == keyword:
            num_word += 1

print(num_word)
