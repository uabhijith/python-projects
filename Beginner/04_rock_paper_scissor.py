#rock paper scissors
#rock wins against scissors
#scissors wins against paper
#paper wins against rock
import random
user=int(input("Enter your move 1:rock 2:paper 3:scissors:"))
game=["Rock","Paper","Scissor"]

if user<=3:
    cpu = random.randint(1, 3)
    print(f"Computer choose : {cpu}")
    print(f"\n{game[user-1]} ----- VS ----- {game[cpu-1]}")
    if user==cpu:
        print("its a draw!")
    elif user==1 and cpu==3 :
        print("you won!")
    elif user==2 and cpu == 1:
        print("you won!")
    elif user==3 and cpu==2:
        print("you won!")
    else :
        print("you lost!")
else :
    print("you choose an invalid number!!")