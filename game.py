from words import words
from random import choice

class Score:
	def __init__(self):
		self.score = 50
		self.filename = "score.txt"
		self.winMessage = ""
	def saveScore(self,score):
		with open(self.filename,"w") as f:
			if self.score > score:
				f.write(str(score))
				self.winMessage = f"You broke the highest score which was {self.score}. " 
			else:
				self.winMessage = f"You were unable to break the highest score which is {self.score}"
	def readScore(self):
		try:
			with open(self.filename,"r") as f:
				self.score =  int(f.read())
		except Exception as e:
			self.saveScore(0)

def getRandomWord():
	word = choice(words)
	while " " in word or "-" in word:
		word = choice(words)
	return word

randomWord = getRandomWord()
randomWord = "chilly"

originalWords = [i for i in randomWord]
userInputWords = ["_" for i in randomWord]
usedWords = set()

userAttempts = 0

while "_" in userInputWords:
	print(" ".join(userInputWords))
	print("Unmatched alphabets used - " + " ".join(usedWords))

	userInput = input("Enter the alphabet :- ")
	if userInput in originalWords:
		index = originalWords.index(userInput)
		userInputWords[index] = userInput
		originalWords[index] = "_"
	else:
		usedWords.add(userInput)
	userAttempts += 1

print("".join(userInputWords))

scoreManager = Score()
scoreManager.readScore()
scoreManager.saveScore(userAttempts)

print(f"Congratulations! You won the game in {userAttempts} attempts {scoreManager.winMessage} ")