import random

def gameWin(comp , you):

    if comp == you:
        return None

    if comp == 'Snake':
        if you == 'Water':
            return False  
        elif you == 'Gun':
            return True
         

    if comp == 'Water':
        if you == 'Gun':
            return False   
        elif you == 'Snake':
            return True 

    if comp == 'Gun':
        if you == 'Snake':
            return False    
    elif you == 'Water':
        return True
         

you = input("Your turn : choose Snake(s) or Water(w) or Gun(g) ? :\t")
print(" Computer's turn : choose Snake(s) or Water(w) or Gun(g) ? :\t")
randnum = random.randint(1,3)
if randnum == 1:
    comp = 'Snake'
elif randnum == 2:
    comp = 'Water'
elif randnum == 3:
    comp = 'Gun'        


print(f" you choosed : {you}")
print(f" computer choosed : {comp}")

a = gameWin(comp , you)

if a == None:
    print("Game has been Tie!!!!")

elif a == False:
    print("Oops !!!!! you lose !!!!")

elif a == True:
    print("Hey !! you Win")  

    
