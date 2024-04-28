import randomNumber

# Global Constant
START_RANGE = 1
END_RANGE = 100

def TheGame():
    Therandnumber = randomNumber.generateRandom(START_RANGE,END_RANGE)
    print("Guess a number between 1 & 100. \n")
    Guesses = 0

    while True :
        Guesses +=1
        guess = int(input(f"guess #{Guesses}:"))


        if guess > Therandnumber:
            print('  "Too high. Try again."')
        elif guess < Therandnumber:
            print('  "Too low. Try again."')
        else:
            print("  correct!\n")
            print(f"Congratulations! you Win in {Guesses} guesses.")

            break
        # end if
    # End while

    # Validating if user want to play again or not
    Playagain = input("would you like to play again? (y/n): ").lower()
    while Playagain != 'y' and Playagain !='n':
        print("please enter 'y' to play again or 'n' to exit")
        Playagain = input("would you like to play again? (y/n): ").lower()
    # end while 

    if Playagain == "y":
        return True
    else:
        return False
    # end if
#end method

def main():
    while TheGame():
        pass
# end method

# call method 
main()