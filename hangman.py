#Hangman game using python/Prolog.

import random
words = ['rainbow', 'love', 'hi']
word = random.choice(words)
print("Guess the characters of the word")
guesses = ''
turns = 10
while turns > 0:
 failed = 0
 for char in word:
  if char in guesses:
   print(char, end=" ")
  else:
   print("_")
   failed += 1

 if failed == 0:
  print("\nYou Win")
  print("\nThe word is: ", word)
  break

 guess = input("\nguess a character:")
 guesses += guess
 if guess not in word:
  turns -= 1
  print("Wrong")
  print("You have", + turns, 'more guesses')
  if turns == 0:
   print("You Loose")