import random

words =  ['tree', 'mango', 'coding', 'human', 'python', 'coffee',
         'hangman', 'amazon', 'help', 'football', 'cricket', 
         'direction', 'dress', 'apology', 'driver', 'ship', 
         'pilot', 'reinforce', 'available', 'exercise', 
         'interrupt','domestic', 'attraction','forestry',
         'corpse', 'wing', 'compose', 'common', 'referee',
         'draft', 'file', 'guess', 'benefit', 'confuse', 
         'certain']
guess = words[random.randint(0, len(words)-1)].upper()
display = []
for x in guess:
    display.append("_")
print("*** GAME STARTED ****")
print("")
print("Guess the word ! ", end=" ")
indexes = []
limbs = 6
userWon = False
userLost = False
guessedLetters = []

def start(word, indexes, display, limbs, userWon, userLost, guessedLetters):
    chance = False  # to stop recursion
    wrong_guess = False
    word_found = ""  # change it to True or False based on word found in the word array
    if userLost == False:
        if len(indexes) > 0:  # check on recursion if user entered any correct letter
            for val in indexes:
                # loop to change "_" with the correct letter in array
                display[val] = word[val]
        if len(guessedLetters) > 0:
            # display how many limbs left
            print("You have ", limbs, " chances left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        for dash in display:
            # print the display of "_" or the correct letter in the array
            print(dash, end=" ")
        print("")
        print("")
        user_guessed = input(
            "Guess by entering a letter or the complete word to win!: ").upper()
        userWon, wrong_guess, word_found = true_or_false(word, indexes, user_guessed,  )
        userLost, chance = new_func(limbs, guessedLetters, wrong_guess, word_found, user_guessed)
        chances_(word, indexes, display, limbs, userWon, userLost, guessedLetters, chance)

def true_or_false(word, indexes, user_guessed, userWon):
    if len(user_guessed) == 1:  # if user entered only a letter
        word_found = False
        for i in range(len(word)):  # to get the index of word array
            if(word[i] == user_guessed):  # match every single letter
                if i in indexes:  # if user already guessed correct letter
                    print("You already guessed the letter ", word[i])
                    chance = True
                    word_found = True
                    break
                else:
                    indexes.append(i)
                    print("Nice guess it was ", word[i])
                    word_found = True
    elif len(user_guessed) > 1:  # if used tried to guess by a word
        userWon, wrong_guess = win_or_lose(word, user_guessed)
    return wrong_guess,word_found

def win_or_lose(word, user_guessed):
    if(word == user_guessed):
        print("Woah luck is on your side, You won !")
        print("The correct word was ", word)
        userWon = True
    else:
        wrong_guess = True
    return userWon,wrong_guess

def chances_(word, indexes, display, limbs, userWon, userLost, guessedLetters, chance):
    if chance == True:
        start(word, indexes, display, limbs,
                  userWon, userLost, guessedLetters)
        chance = False  # to stop recursion :X aryan
    elif len(indexes) > 0 and userWon == False and userLost == False and chance == False:
        if len(indexes) == len(word):  # if user guessed all letters
            print("Woah, You won ! :)")
            print("The correct word was ", word)
        else:
            start(word, indexes, display, limbs,
                      userWon, userLost, guessedLetters)
    elif userLost == True:  # all limbs are 0 so user lost
        print("You have ", limbs, " chances left")
        print("Sorry, You lost :(")
        print("The correct word was ", word)

def new_func(limbs, guessedLetters, wrong_guess, word_found, user_guessed):
    if user_guessed in guessedLetters:  # if user guessed wrong again with the same word/letter
        print("You already tried ", user_guessed)
        chance = True
    elif wrong_guess == True or word_found == False:  # when user guessed wrong reduce limbs
        guessedLetters.append(user_guessed)
        print("Eh, Wrong guess")
        limbs -= 1
        if limbs == 0:
            userLost = True
        else:  # when limbs are not 0 user can still play with chance = true
            chance = True
    return userLost,chance


start(guess, indexes, display, limbs, userWon, userLost, guessedLetters)