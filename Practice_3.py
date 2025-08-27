#This is code for the hangman game.
import random

words= ["mathematics","beautiful","exploration","embroidery","friendship"]
word= random.choice(words)
guessed=""
tries = 5

print("Welcome to the Hangman game!")

while tries>0:
    display="" 
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "__"
        print("word: " ,display )

