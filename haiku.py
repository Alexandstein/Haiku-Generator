import sys
import random

class HaikuGenerator:
	'''
	The object which generates haikus.
	
	Members:
		(list of string lists) __dictionary:
			A list of collections of words organized by how many syllables it contains. 
			The index of 'dictionary' is how many syllables the words in the sublist 
			contains.
		(list of ints) format:
			A list keeping track of the syllable format of haiku. (5, 7, 5)
	Functions:
		(Constructor) __init__
		(list of strings) getWordsBySyllables
		(string) writeLine
		(string) generate
	'''
	
	def __init__(self, dictionaryFile):
		'''
		Constructor for Haiku 
		args:
			(string) dictionaryFile
				The filename of a file containing words for our generator to use.
		'''
		self.format = [5,7,5]							#Format of the haiku syllables
		self.__dictionary = [[],[],[],[],[],[],[]]		#Create a list of 7 empty lists
														#Words will be arrange by syllables
														#in here
		
		try:
			f = open(dictionaryFile, 'r')				#Opens the file
			
			for line in f:								#Iterate over lines in the file
				line = line.split(',')						#Turn lines into lists of word, syllable pairs
				self.__dictionary[int(line[1]) - 1].append(line[0])	#append the word to a list
			
		except IOError:									#Something has gone wrong!
			sys.exit("Dictionary input is not a valid file!")	#Not a valid file, exit
			
	def getWordsBySyllables(self, syllableCount):
		'''
		Get a list of words by syllable number.
		args:
			(int) syllableCount:
				The number of syllables of the list of words you would like to retrieve.
		return:
			A list of words with number of syllables 'syllableCount'.
		'''
		return self.__dictionary[syllableCount - 1];
		
	def writeLine(self, syllableCount):
		'''
		Generates a line with the given number of syllables.
		args:
			(int) syllableCount:
			Amount of syllables the outputted line will have.
		return:
			A single haiku line containing the desired syllable count.
		'''
		
		remainingSyllables = syllableCount			#Keep track of remaining space.
		outputString = ''							#Empty string to create line
		while remainingSyllables != 0:
			#Choose a random int between 1 and however many syllables are remaining, 
			#select a word of that length and then append it to the string
			syllables = random.randint(1, remainingSyllables)
			newWord = random.choice(self.getWordsBySyllables(syllables))
			
			outputString += newWord + ' '			#Append and...
			remainingSyllables -= syllables			#Subtract syllabes of added word from 
													#remaining syllable counter
		return outputString.strip()					#Get rid of extra whitespace
		
	def generate(self):
		'''
		Issues the command to generate a full haiku and returns the string.
		args:
			(void)
		return:
			String containing the haiku.
		'''
		outputHaiku = ''
		for lineSyllables in self.format:					#Run through format (5,7,5)...
			outputHaiku += self.writeLine(lineSyllables) + '\n' #and append the new lines
		return outputHaiku.strip()							#Get rid of extra whitespace
	
#################################################
#					MAIN						#
#################################################
if __name__ == '__main__':
	haiku = HaikuGenerator('dictionary.dict')
	print haiku.generate()