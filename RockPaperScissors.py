import random

def run_game():
    while True:
        print("Do you want to start the Game?")
        start = input("Type [Y]es or [N]o: ")

        if start.lower() == "y":
            choice = input("Choose your Weapon:  [R]ock  [P]aper [S]cissors\n").lower()
            weapons = ['r', 'p', 's']
            weapons_full = ['Rock', 'Paper', 'Scissors']
            rand_ind = random.randint(0,2)
            opp_choice = weapons[rand_ind]
            print("Computer chose: ", weapons_full[rand_ind])

            if choice in "rps":
                if (choice == 'r' and opp_choice == 'p') or (choice == 'p' and opp_choice == 's') or (choice == 's' and opp_choice == 'r'):
                    print('Computer Wins!')
                elif choice == opp_choice:
                    print("It is a Tie")
                else:
                    print("you win!")
                print()
            else:
                print(choice, 'is not a Weapon!!!')
                print()
        elif start.lower() == 'n':
            print("Signing off!")
            break
        else:
            print("Warning!!! Type either 'y' or 'n'")

run_game()