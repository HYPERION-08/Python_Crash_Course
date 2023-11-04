
# ------------------ Part 1 ----------------------------
# create a greeting
# create a wordlist
# randomly choose a word from the list you have created
# ask the user to guess a letter
# make the program take the input for the user and make it lowercase
# check if the letter is in the word
# ------------------------------------------------------


# ------------------ Part 2 ----------------------------
# create an empty list
# for each letter in the secret_word add a '_' that will be
#       printed to the console
# Example : bug = "_","_","_"

# loop through each of the letters in the chosen word
# if the letter is in the word replace the "_" with the letter
# it should look like this "_",u,"_".
# -------------------------------------------------------

import random
print("welcome to hangman")
words = ["bug","bounty","random","hacker"]
# the random word
secret_word = random.choice(words)
display_word = []
# guessing the letter and making it lowercase


for letter in secret_word:
    display_word += "_"
print(display_word)

guess = input("Guess a letter : ").lower()

for letter in secret_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
