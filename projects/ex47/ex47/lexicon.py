# Game Lexicon Scanner

directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stopWords = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = [0,1,2,3,4,5,6,7,8,9]

lexicon = ["north", "south", "east", "west", "down", "up", "left", "right", "back","go", "stop", "kill", "eat","door", "bear", "princess", "cabinet",0,1,2,3,4,5,6,7,8,9]
dicts = ["directions","verbs","stopWords","nouns","numbers"]
sentence = []

# loop through words & tuple assignments
def scan (test):
	if test in directions:
		return [('direction', 'north')]
	else:
		return "No Match"
