print('hangman!')

import random
from word import words

def get_word():
	random_word = random.choices(words)
	return random_word[0].upper()

# get_word()
print(get_word())

class Word():
	def __init__(self, chosen_word):
		self.letter = letter
		self.guessed = False
		self.remaining_guesses = 8
		self.letters_used = letters_used
		self.chosen_word = chosen_word

			# print({self.random_word})




# print(words)
# print(random.choices(words))

















# while True:
#   print("Guess a letter", end=": ")
#   user_input = input()
#   if(user_input == "q"):
#     print("bye!")
#     break
#   else:
#     print("you guessed:", user_input)







# def play(word):
#     word_completion = "__" * len(word)
#     guessed = False
#     guessed_letters = []
#     # guessed_words = []
#     remaining_guesses = 8
# print("Let's play Hangman!")
# print("\n")

# while not guessed and tries > 0:


# print(word_list)



