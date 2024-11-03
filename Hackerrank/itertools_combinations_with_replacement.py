inp_ = input()
inp = inp_.strip()

current_char = inp[0]
count = 1

for char in inp[1:]:
    if char == current_char:
        count += 1
    else:
        print(f"({count}, {current_char})", end=' ')
        current_char = char
        count = 1

print(f"({count}, {current_char})")