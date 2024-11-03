'''The game function in the program lets a user play a game and returns 
the score as an integer . You need to read a file 'History.txt'
which is either blank or contain previous high score . 
we need to write a program to update the high score whether game breaks the high score.
'''
def game():
    return 2000

score = game()

with open('High_score.txt') as f:
    hyscore = int(f.read())

if hyscore == " ":
    with open('High_score.txt' ,'w') as f:
        f.write(str(score))    

if int(hyscore) < score:
    with open('High_score.txt' ,'w') as f:
        f.write(str(score))    