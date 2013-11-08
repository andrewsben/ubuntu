def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the Words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentance(sentance):
	"""Takes in a full sentance and returns the sorted words."""
	words = break_words(sentance)
	return sort_words(words)

def print_first_and_last(sentance):
	"""Prints the first and last words of the sentance."""
	words = break_words(sentance)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentance):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentance(sentance)
	print_first_word(words)
	print_last_word(words)