import random as ran

number = ran.randint(1, 10)
guess = int(input("Please enter your guess: "))
YNPlayAgain = "N"
run_holder = True

if number == guess:
    print("You won do u want to play again?")
else:
    print("You lost do u want to play again?")
    print ("the Number was", number)

YNPlayAgain = str(input("Y/N "))

while run_holder == True:
    if YNPlayAgain == "Y":
        number = ran.randint(1, 10)
        guess = int(input("Please enter your guess: "))
        
        
        if number == guess:
            print("You won do u want to play again?")
        else:
            print("You lost do u want to play again?")
            print ("the Number was", number)
            
        YNPlayAgain = str(input("Y/N "))
    else:
        break