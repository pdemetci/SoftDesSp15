""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def read_book(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	book = open(file_name, 'r')
	return book
	# header=" " # Will need to change based on the book used.
	# def strip_header():
def strip_punctuation():

	words=[]
	for word in f:
		if word not in string.whitespace and word not in string.punctuation: 
			f=''
			for i in range(len(word)):
				if word[i: i+1] != '\n' and word[i] not in string.punctuation:
					f+=word[i:i+1]
			words.append(f)
			
def separate_words():
	all_words=[]
	for x in words:
		a= x.split()
		for i in a:
			i_lower=i.lower()
			all_words.append(i_lower)
	return all_words
	
def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	freq_dict={}
	for word in word_list:
		freq_dict[word]=0
	for word in word_list:
		freq_dict[word]+=1
	freq_dict_sorted = sorted(freq_dict.items(), key=lambda item: item[1])[::-1]
	print freq_dict_sorted[1:n]

get_word_list('Zarathustra.txt')
get_top_n_words(get_word_list('Zarathustra.txt'), 200)