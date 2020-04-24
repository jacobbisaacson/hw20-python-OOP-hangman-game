print('test')

def play(random_word):
	word_guessed = "_" * len(random_word)
	guessed = False
	guessed_letters = []
	guessed_words = []
	remaining_guesses = 8
	print('lets play!')
	print(remaining_guesses)
	print(word_guessed)
	print("\n")
	while not guessed and remaining_guesses > 0:
		guess = input('guess a letter: ').upper()
		if len(guess) == 1:
			if guess in guessed_letters:
				print("already guessed the letter", guess)
			elif guess not in random_word:
				print(guess, "is not in the word")
				remaining_guesses -= 1
				guessed_letters.append(guess)
			else:
				print('good guess!', guess, "is correct")
				guessed_letters.append(guess)
				word_in_list = list(word_guessed)
				index = [i for i, letter in enumerate(random_word) if letter == guess]
				for i in index:
					word_in_list[i] = guess
				word_guessed = "".join(word_in_list)
				if "_" not in word_guessed:
					guessed = True
		elif len(guess) == len(random_word):
			if guess in guessed_words:
				print("already guessed")
			elif guess != random_word:
				print(guess, "is incorrect")
				remaining_guesses -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				word_guessed = random_word
		else:
			print("not valid sorry")
		print(remaining_guesses)
		print(word_guessed)
		print("\n")
	if guessed:
		print("you win!")
	else:
		print('you lose')


def game():
	random_word = get_word()
	play(random_word)