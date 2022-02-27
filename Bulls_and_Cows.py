import random

number = []
attempts = 0

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

        choice = input("Please enter a 4 digit number: ")
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
        print("Cows: ",cows)
    except:
        MakeNumber()
        PlayGame()
    if bulls != 4:
        PlayGame()
    if bulls == 4:
        if attempts == 1:
            print("You won after 1 attempt!!")
            again = input("Play again (y/n)").lower()
            if again == "y":
                MakeNumber()
            else:
                quit()
        else:
            print("You won after " + str(attempts) + " attempts!!")
            again = input("Play again (y/n)").lower()
            if again == "y":
                MakeNumber()
            else:
                quit()


MakeNumber()
PlayGame()
