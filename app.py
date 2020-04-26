print('hangman!')

import random
from wordbank import word_bank

word = random.choice(word_bank)
blank = ""
for char in word:
  blank += "_ "
print(blank)
guessed_letters = []
remaining_guesses = 8


class Word():
  def __init__(self, word):
    self.word = word
    self.blank = ["_" for char in word]
    self.wrong = []
  def print_word(self):
    print(" ".join(self.blank))
  def check(self, letter):
    if letter in self.wrong:
      print("already guessed, try again")
      return
    if char in self.word:
      if char not in self.blank:
        for i, val in enumerate(self.word):
          if val == char:
            self.blank[i] = char
            self.print_word()
            print(f"{char} is a correct guess!")
      else:
        remaining_guesses -= 1
        self.wrong.append(char)
        print(self.wrong)
        print(f"{char} is incorrect, you have {remaining_guesses} remaining")

start = input("Let's play hangman! (type 'y' to play)")
if start == "y":
  print(f"let's do it! you have {remaining_guesses} tries")


word = Word(word)
# print(word.__dict__)







# class Letter():
#   def __init__(self, character):
#     self.character = character
#     self.guess = False

#   def guessed(self, guess):
#     self.guess = True


  # def display(self):
  #   blank = ""
  #   for char in self.word:
  #     blank += "_ "
  #   print(blank)






# import random
# from wordbank import word_bank
# print(random.choice(word_bank))

# class Word():
#   def __init__(self, word):
#     self.word = word

#   def display_word(self):
#     show_word = ""
#     for char in self.word:
#       show_word += "_ "
#     print(show_word)

# # word = show_word
# # word.display_word()






# remaining_guesses = 8
# letters_used = []
# chosen_word = []



# def get_word():
#   random_word = random.choice(word_bank)
#   print(random_word)

# get_word()

# class Word():
#   def __init__(self, word):
#     self.wod = word

#   def display_word(self):
#     show_word = ""
#     for char in self.word:
#       show_word += "_ "
#     print(show_word)

# word = Word('bruna')
# word.display_word()








# def push_word():
#   word_push = get_word(random_word)
#   print(random_word)

# push_word()



# class Word():
#   def __init__(self, word):
#     self.word = word

#   def game_word(self):


# const gameWord = chosen_word.push(get_word())





# LETTER //////
# class Letter():
#   def __init__(self, char):
#     self.char = char
#     self.guess = False

#     def mark_guessed(self, guess):
#       self.guess = True



# STATUS_PLAYING = "playing"

# class Word():
# 	def __init__(self, chosen_word):
# 		self.chosen_word = chosen_word
# 		self.remaining_guesses = 8
# 		self.hidden_word = ['_'] * len(chosen_word)
# 		self.guesses = {}
# 		self.status = STATUS_PLAYING

# 	def guess(self, character):
# 		if character not in self.word



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



