'''
program: generator.py
author: ry 10/05/2020
pages 150-153

app generates and displays sentences using simple grammar and vocab. words are chosen at random.
'''

#import statement for the random module
import random

#global vars and cosnts 
#vocab: words in 4 diff parts of speech
articles = ('A', 'THE', 'AN')
nouns = ('BOY', 'GIRL', 'BAT', 'BALL', 'HAT', 'BOTTLE', 'HAM', 'POTATO')
verbs = ('HIT', 'HIT', 'LIKED', 'THREW', 'PASSED', 'ATE', 'DUMPED', 'POOPED')
prepositions = ('WITH', 'BY', 'ABOVE', 'WITHOUT', 'INTO')

def sentence():
	'''builds and returns a sentence.'''
	return nounPhrase() + " " + verbPhrase()

def nounPhrase():
	'''builds and returns a noun phrase'''
	return random.choice(articles) + ' ' + random.choice(nouns)

def verbPhrase():
	'''builds and returns a verb phrase'''
	return random.choice(verbs) + ' ' + nounPhrase() + ' ' + prepositionalPhrase()

def prepositionalPhrase():
	'''builds and returns a perpositional phrase'''
	return random.choice(prepositions) + ' ' + nounPhrase() 

def main():
	'''allows the user to input the number of sentences to generate'''
	#input phase
	number = int(input('enter the numer of sentences: '))

	#processing and output phases
	for x in range(number):
		print(sentence()) 
# global entry point to main() for program execution 
main()