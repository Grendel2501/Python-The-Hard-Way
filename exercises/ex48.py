# Game Lexicon Scanner
# Game Lexicon:

directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stopWords = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = [0,1,2,3,4,5,6,7,8,9]

lexicon = ["north", "south", "east", "west", "down", "up", "left", "right", "back","go", "stop", "kill", "eat","door", "bear", "princess", "cabinet",0,1,2,3,4,5,6,7,8,9]
sentence = []

# Get input from some source
from sys import argv

# Set input to imported content
data = argv

stuff = raw_input('> ')
words = stuff.split()

# loop through words & Tuple assignments
def scan ():
	for word in lexicon:
		if word in lexicon:
			try:
	        	return word
			except ValueError:
	        	return None
