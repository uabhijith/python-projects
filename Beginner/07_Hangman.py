import random
word_list=["advark","baboon","camel"]
chosen_word=random.choice(word_list)
word_len=len(chosen_word)
lives=6
stages=["0 life left","1 life left","2 life left","3 life left","4 life left","5 life left"]
print(f"the solution is {chosen_word}")
display=[]
for _ in range(word_len):
    display+="_"
print(display)
print("you have 6 life!")
eog=False
while not eog:
    guess=input("Guess a letter").lower()
    if guess in display:
        print(f"you already guessed the {guess} letter")
    for position in range(word_len):
        letter=chosen_word[position]
        if letter== guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word")
        lives-=1
        if lives==0:
            eog=True
            print("You lose")

    print(display)
    if "_" not in display:
        eog=True
        print("you won")

    print(stages[lives])