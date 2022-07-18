"""
	P04-07: Interested word counter
"""


keyword: str = input()
sentence: str = input()
first_char = keyword[0]
num_word: int = sum(sentence[i: i + len(
    keyword)] == keyword for i in range(len(sentence)))


print(num_word)
