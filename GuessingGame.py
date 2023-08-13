import random

def run_game(rem_attempts = 5, random_number = random.randint(1,21)):

    while True:
        guess = int(input('enter a number between 1 and 20: '))
        rem_attempts -= 1

        if guess<random_number:
            print("Oops! A bit Higher.")
        elif guess>random_number:
            print('Oh no! A little Lower.')

        print("")

        print("remainig attempts: ",rem_attempts, "\n")

        if guess == random_number:
            print("Congratulations! Your Guess is Correct.")
            break
        if rem_attempts == 0:
            print("You ran out of moves. Better Luck next time!")
            break

        

def main():
    while True:
        print("Do you want to Start the Game?")
        start = input("Type Yes or NO\n")

        if start.lower() == 'yes':
            run_game()
        elif start.lower() == 'no':
            print("Signing off!")
            break
        else:
            print("Warning!!! Type Yes or NO")

        print("**************************************************")


print("Can you guess the number in 5 moves?")
main()