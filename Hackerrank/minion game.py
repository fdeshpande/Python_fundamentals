# Minion Game!!!!!!!!!!!!!!!

def calculate_score(string, substring):
    score = string.count(substring)
    return score

def player_turn(player, string):
    if player == 'stuart':
        valid_starting_chars = 'bcdfghjklmnpqrstvwxyz'
        player_prompt = "Stuart, enter a substring starting with a consonant: "
    elif player == 'kevin':
        valid_starting_chars = 'aeiou'
        player_prompt = "Kevin, enter a substring starting with a vowel: "
    else:
        return 0

    while True:
        user_input = input(player_prompt).lower()
        if user_input.startswith(tuple(valid_starting_chars)):
            return calculate_score(string, user_input)
        else:
            print("Invalid input! Try again.")

# Game logic
input_string = "banana"
p1_score = player_turn('stuart', input_string)
print("Stuart", p1_score)

p2_score = player_turn('kevin', input_string)
print("Kevin", p2_score)
