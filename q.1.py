secretword = "secretword"
lettersGuess = " "
failureCount=6
while failureCount > 0:
    guess = input("enter a letter :")
    if guess is secretword:
        print(f"count! one or more {guess} in the secretword !")
    else:
        failureCount -=1
        print(f"incorrect! no more {guess} in the secretword!{failureCount}turn(s) left !")
    lettersGuess= lettersGuess + guess
    wronglettercount=0
    for letter in secretword:
        if letter in lettersGuess:
            print(f"{letter}",end="")
        else:
            print("_",end="")
            wronglettercount+=1
    if wronglettercount==0:
        print(f"congrats! THe secretword was:{secretword}.you won!")
        break
else:
    print("sorry , you didn't win it this time, try again")
    
    
    