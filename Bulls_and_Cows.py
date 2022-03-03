
import random
print("""
Bulls and Cows
Version 1.0 (2022)
***********************
Instructions:

The computer has selected a 4-digit number.
Enter a 4-digit number who's digits do not repeat.
A Cow indicates that a digit of your selected number exists in the pre-selected number.
A Bull indicates that a digit of your selected number is in the correct position of the pre-selected number.
Objective: Guess the number by getting 4 Bulls.
***********************
""")
number = []
attempts = 0
def main():
    def MakeNumber():
        for i in range(4):
            x = random.randint(0,9)
            number.append(x)
        if len(number) > len(set(number)):
            number.clear()
            MakeNumber()

    def PlayGame():
        try:
            global attempts
            attempts += 1
            cows = 0
            bulls = 0
            choice = input("\nPlease enter a 4 digit number: ")
            if len(choice) != 4:
                PlayGame()
            guess = []
            for i in range(4):
                guess.append(int(choice[i]))
            for x in range(4):
                if guess[x] == number[x]:
                    bulls += 1
            for i in range(4):
                for j in range(4):
                    if guess[i] == number[j]:
                        cows += 1
            cows = str(int(cows) - int(bulls))
            print("Bulls: ", bulls)
            print("Cows: ", cows)
        except:
            MakeNumber()
            PlayGame()
        if bulls != 4:
            PlayGame()
        if bulls == 4:
            if attempts == 1:
                print("\nYou won after 1 attempt!!")
                again = input("Play again (y/n)").lower()
                if again == "y":
                    main()
                if again == "":
                    quit()
                else:
                    quit()
            else:
                print("You won after " + str(attempts) + " attempts!!")
                again = input("Play again (y/n)").lower()
                if again == "y":
                    main()
                else:
                    quit()


    MakeNumber()
    PlayGame()
main()
