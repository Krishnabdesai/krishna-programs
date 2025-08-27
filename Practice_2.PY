#learning how to import time and random. we can also import mathematical functions
# This code is a simple Rock, Paper, Scissors game.
import random
import time
user= str(input("Choose Rock, Paper or Scissors: ").lower())
options=["rock","paper","scissors"]

print("Computer is chosing...")
time.sleep(2)  # Delays for 2 seconds

computer= random.choice(options).lower()
print(f"Computer chose: {computer}")

if user==computer:
    print("Tie!")
elif (user=="rock" and computer=="scissors"):
    print("You win!")
elif(user=="scissors" and computer=="paper"):
    print("You win!")
elif (user=="paper" and computer=="rock"):
    print("You win!")

else:
    print("You Lose!")
    