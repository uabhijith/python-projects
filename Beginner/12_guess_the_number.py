from random import randint

answer = randint(1, 100)
print("Welcome to the Number Guessing game!\n I'm thinking a number between 1 and 100")


def difficulty():
    lev = input("Choose a difficulty. Type 'easy' or 'hard' :").lower()
    if lev == "hard":
        return 5
    elif lev == "easy":
        return 10


def value_checking(unum, rnum):
    if unum == rnum:
        print("correct guess")
    elif unum > rnum:
        print("guess is too high")
    else:
        print("guess is too low")


def enter_number():
    return int(input("Enter your guess:"))


level = difficulty()
flag = 0
while flag == 0:
    print(f"Guesses left:{level}")
    # print(answer)
    usnum = enter_number()
    value_checking(unum=usnum, rnum=answer)
    level -= 1
    if level == 0 or usnum == answer:
        print("Game over")
        flag = 1
