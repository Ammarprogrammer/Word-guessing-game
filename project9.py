import random

easy_words = ['apple' , 'chair' , 'tiger' , 'book' , 'water' , 'moon' , 'dog' , 'car' , 'ball' , 'fish']
medium_words = ['camel' , 'pencil' , 'window' , 'forest' , 'laptop' , 'garden' , 'silver' , 'desert' , 'planet' , 'bridge']
hard_words = ['whisper' , 'pyramid' , 'volcano' , 'lantern' , 'magnet' , 'galaxy' , 'oxygen' , 'eclipse' , 'journey' , 'thunder']

print("welcome to the password guessing game")
print("Chose a difficulty level: easy , medium , hard")

level = input("chose a difficulty level: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Choice, Defaulting to easy level")
    secret = random.choice(easy_words)

attempt = 0
print("\n Guess the password")

while True:
    guess = input("Enter your guess: ").lower()
    attempt +=1

    if guess == secret:
        print(f'Congratulation! You guessed it in {attempt} attempts')
        break 

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint: " , hint)

print("Game Over")                
