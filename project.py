from random import randint, choice
import sys
from time import sleep
import cowsay
from tabulate import tabulate


def main():
    try:
        dol = float(input('\nHow many dollars you want to add? $'))
        be = float(input('\nHow many you want to bet? $'))

        is_correct(dol, be)

        cont = ' '
        while True:
            # The if statement just because of the first loop, don't appear the bet twice
            if cont != ' ':
                be = float(input('\nHow many you want to bet? $'))

            # The if statement just to appear in the first loop
            if cont == ' ':
                print(table_text(dol, be, 'WELCOME TO CS CASINO'))

            # The user chooses a game
            gam = int(input('Choose a game [1 or 2]: '))
            if gam == 1:
                dol = first_game(dol, be)
            elif gam == 2:
                dol = second_game(dol, be)

            # If the user don't have any money left, stop
            if total_dollar(dol) == 0.0:
                break

            sleep(1)
            print(table_text(dol, be, 'YOUR TOTAL MONEY', bet_show=False))

            # Ask the user if they want to bet again
            cont = ' '
            while cont[0] not in 'yn':
                cont = str(input('Want to continue? [Yes or No]: ')).strip().lower()
            if cont[0] == 'n':
                break

        # The table of the results
        print(table_text(dol, be, 'THANKS FOR PLAYING IN THE CS CASINO', False))

    except Exception as e:
        # If there is any errors in the execution of the code
        sys.exit(f'Sorry, this went wrong: {e}')


# Initiate the class calling variables
def is_correct(dollars=100, bet=50):
    # A infinit loop to not catch any user errors
    while True:
        if dollars >= bet:
            return True
        else:
            # If the user put a bet bigger than the money add
            print("\n\033[31;1mYou don't have that much money to bet, try again...\033[m")
            sleep(1)
            bet = float(input('How many you want to bet? $'))


# Print a table with a phrase and your total money and maybe the bet
def table_text(dollars, bet, phrase, bet_show=True):
    sleep(0.5)
    print()

    menu = [
        [''],
        [f'{" »»» Total money:":<20} ${dollars:<20.2f}'],
        [''],
        [f'{" »»» Bet:":<20} ${bet:<20.2f}'],
        [''],
        ]
    # In case of not wanting to see the bet
    if not bet_show:
        for _ in range(2):
            menu.pop()

    headers = [f'{phrase:<23}']
    return f'\033[34;1m{tabulate(menu, headers, tablefmt="outline")}\033[m\n'


# The first game
def first_game(dollars, bet):
    # Get a random number
    number = randint(1, 10)

    # The user have a total chance of 4 guesses
    for tries in range(3, -1, -1):
        n = int(input('\nGuess a number between 1 and 10: '))

        # If the user gets right
        if number == n:
            cowsay.kitty("\033[32;1mYOU ARE RIGHT!\033[m")
            print()
            dollars += bet * 1.75
            break
        else:
            sleep(1)
            print(f'\033[31;{tries+2}m »» You are wrong... You have a total of {tries} tries...\033[m')

    # If the user guess all the tries wrong
    if number != n:
        cowsay.tux('\033[31:1mWHAT A SHAME!\033[m')
        print()
        # The user loose the money of the bet
        dollars -= bet

    return dollars


# Second game
def second_game(dollars, bet):
    things = ['🍒', '👾', '👽', '💲']

    # The user have a total of 6 tries of getting all the same emoji
    for t in range(6, 0, -1):
        # Append in a list, three emojis in a random way
        choose = [choice(things) for _ in range(3)]
        print()

        # To show the user all the 3 random emojis
        for i in range(len(choose)):
            print(f'  {choose[i]} ', end=' ')
            for _ in range(3):
                # To stop the dots after the last emoji
                if i == 2:
                    break
                print('.', end='')
            sleep(0.25)
        print()

        # If all the emojis is the same, you win and the dollar that you bet is multiplied by 5 (because it's hard to win)
        if choose[0] == choose[1] and choose[1] == choose[2]:
            cowsay.tux("\033[32;1mYOU WON!\033[m")
            dollars += bet * 5
            break

        else:
            # print the user the tries left
            print(f'\n »» You have {t - 1} tries left!')
            sleep(1.5)


    if choose[0] == choose[1] and choose[1] == choose[2]:
        pass

    else:
        # If the user don't win, he lost the money of the bet
        dollars -= bet

    return dollars


# Just to make sure that if the dollars is 0, the code should stop
def total_dollar(dollars):
    return dollars


if __name__ == '__main__':
    main()
