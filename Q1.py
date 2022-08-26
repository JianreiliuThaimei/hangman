import random
from IMAGES import IMAGES

word_list=["india","nepal","bhutan","china","japan","taiwan","korea","thailand"]
chosen_word=random.choice(word_list)
word_lenght=len(chosen_word)

display=[]
for i in range(word_lenght):
    display=display+list("_")

lives=8
game_over=False
while not game_over:
    guess=input("enter a guess : ").lower()
    for i in range(word_lenght):
        letter=chosen_word[i]
        if letter==guess: 
            display[i]=letter

    if guess not in chosen_word:
        lives-=1
        for i in IMAGES:
            if letter!=guess and lives==8:
                print(IMAGES[0])
                break
            if letter!=guess and lives==7:    
                print(IMAGES[1])
                break
            if letter!=guess and lives==6: 
                print(IMAGES[2])
                break
            if letter!=guess and lives==5: 
                print(IMAGES[3])
                break
            if letter!=guess and lives==4: 
                print(IMAGES[4])
                break
            if letter!=guess and lives==3: 
                print(IMAGES[5])
                break
            if letter!=guess and lives==2: 
                print(IMAGES[6])
                break
            if letter!=guess and lives==1: 
                print(IMAGES[7])
                print("you lose")
                break        
    print(display)