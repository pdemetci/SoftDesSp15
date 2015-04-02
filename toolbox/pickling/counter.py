""" A program that stores and updates a counter using a Python pickle file"""
<<<<<<< HEAD
=======

>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983
from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
<<<<<<< HEAD
	output = open(file_name, 'r+')
	if reset==True or not exists(file_name):  #If the counter hasn't been pickled before/ the file hasn't been created or it has been reset, counter =1 
		counter = 1
		dump(counter,output) #Serializing counter
	else:
		counter = load(output)+1 #If the counter has been pickled and being pickled again, counter +=1. load() deserializes
		dump(counter,open(file_name, 'r+')) #Serialzing the new value for counter.
	return counter
=======
	pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))