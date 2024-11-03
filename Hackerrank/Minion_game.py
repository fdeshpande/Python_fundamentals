import random
import time
print("# WELCOME TO THE MINION GAME #")
Player_1 =input("Enter player 1 name : ")
Player_2 =input("Enter player 2 name : ")
print()
print()
print("Now its time to toss...............")
print()

choice = input(f"{Player_1} , enter your choice choose 'h' for 'head' and 't' for 'tail' : ")
choice_ = input(f"{Player_2} , enter your choice choose 'h' for 'head' and 't' for 'tail' : ")
print()
print()
score_for_player1=0
score_for_player2 = 0
def for_player2():
    play_again = "yes"
    while play_again == 'yes':
        string = 'BANANAS ON BANANA TREE'
        print("Read below instructions.................[^_^]")
        print()
        print("You are seeing one string here , You have to make the substring from the given string .\t\n Then according to occurance of your substring your score will be counted . \t\n Who will score maximum he/she will be the WINNER.... (^_^)(o_o) ")
        print()
        time.sleep(5)
        print("Your string is : ", string)
        print()
        time.sleep(2)
        s = input("Enter your substring here by giving space only you can write another after one : ")
        print()
        print("Press Enter.......")
        time.sleep(1)
        print("Wait to see your scores ...........(o_o)")
        print("Calculating............")
        time.sleep(3)
        s1 = s.split(" ")
        c = 0
        for i in s1:
            c = c + string.count(i)
        score_for_player2 = c
        print(f"Your score : {score_for_player2}")
        return score_for_player2

def for_player1():
    play_again = "yes"
    while play_again == 'yes':
        string = 'BANANAS ON BANANA TREE'
        print("Read below instructions.................[^_^]")
        print()
        print("You are seeing one string here , You have to make the substring from the given string .\t\n Then according to occurance of your substring your score will be counted . \t\n Who will score maximum he/she will be the WINNER.... (^_^)(o_o) ")
        print()
        time.sleep(5)
        print("Your string is : ", string)
        print()
        time.sleep(2)
        s = input("Enter your substring here by giving space only you can write another after one : ")
        print()
        print("Press Enter.......")
        time.sleep(1)
        print("Wait to see your scores ...........(o_o)")
        print("Calculating............")
        time.sleep(3)
        s1 = s.split(" ")
        c = 0
        for i in s1:
            c = c + string.count(i)
        score_for_player1 = c
        print(f"Your score : {score_for_player1}")
        return score_for_player1


if choice == 'h':
    print(f"{Player_1} won toss , choosed head . \n{Player_1} will play first .")
    print(f"{Player_2} will play after {Player_1}")
    print()
    print(f"{Player_1}'s Turn :")
    time.sleep(2)
    for_player1()

elif choice_ == 'h':
    print(f"{Player_2} won toss , choosed head . \n {Player_2} will play first .")
    print(f"{Player_1} will play after {Player_2}")
    print()
    print(f"{Player_2}'s Turn :")
    for_player2()
    time.sleep(2)
    for_player2()

elif choice == choice_:
    print("Invalid Choice")
    print()
    print()
time.sleep(2)

if score_for_player1 > score_for_player2:
    print(f"{Player_1}, You are the winner")
elif score_for_player1 < score_for_player2:
    print(f"{Player_2}, You are the winner")
elif score_for_player1 == score_for_player2:
    print(f"Play Again , its Tie")
























