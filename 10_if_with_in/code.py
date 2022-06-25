number = 7
user_decision = input("Would you like to play a guessing game (Y/n): ")

if (user_decision in ("Y", "y")):
    guess = int(input("Enter a guessing number: "))

    if guess != number:
        print("You got the number wrong :-(. Try again!")
    else:
        print("Woot woot. Correct!")
