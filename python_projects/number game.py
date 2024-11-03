import random
randnumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randnumber):
    userGuess = int(input("Enter your guess: \t"))
    guesses += 1
    if userGuess ==randnumber:
        print("you guessed it right...\n")

    else:
        if (userGuess>randnumber):
            print("you guessed it wrong. Enter the smaller number")

        else:
            print("you guessed it wrong. Enter the larger number")

print(f"You guessed the number in {guesses} guesses. ")    

with open('highscore.txt','r') as f:
    highscore = int(f.read())

if (guesses<highscore):
    print("You have just broken the high score...")

    with open('highscore.txt','w') as f:
        f.write(guesses)    



    

