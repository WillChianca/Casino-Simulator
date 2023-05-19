# CS Casino

#### Video Demo:  <https://youtu.be/FMCg8dLcpYk>
# Description:

For my final project of the course CS50P, I chose to make a simple game called **"CS Casino"**, in which the game simulates a real casino game, in the "casino" you can choose between the first and the second.

#### Project structure:
+ project.py
+ test_project.py
+ requirements.txt
+ README.md

#### Usage:
+ `python project.py`

## Explaining the game

The **first game**, work as a guesser, the computer choose a number and you have to try to guess this number (a total of 4 tries), and if you guess the number right the money that you bet it's multiplied by 1,75.


For the **second game** works like a slot machine, that is choosen 3 random emoji and if this 3 emoji is equals so than you win, and the money is multiplied by 5 (because it´s really hard to win).

All the project is in only one file `project.py`, and there are all the function, for the `test_project.py`. I couldn't test 2 functions, all 2 games function, because games work with randomness and there is no way that we can know for sure what it going to be the output.

In the end you will receive a table with you total money and get asked if you want to continue playing:

    +----------------------------+
    | YOUR TOTAL MONEY           |
    +============================+
    |                            |
    | »»» Total money:    $51.75 |
    |                            |
    +----------------------------+

    Want to continue? [Yes or No]:

# Design and libraries

For the design I choose to put some collors, because it was just black and white, and was just ugly, the pip installation libraries:
+ `cowsay`
+ `tabulate`

The libraries is also just to have a better design and to add some irony to the game.

To simulate a menu of the casino, I ended up installing the `tabulate` library to make the game more beautiful, organized and better structured.

    +-----------------------------+
    | WELCOME TO CS CASINO        |
    +=============================+
    |                             |
    | »»» Total money:    $100.00 |
    |                             |
    | »»» Bet:            $50.00  |
    |                             |
    +-----------------------------+

And like a normal game we need to add some irony and playing with the user, so that why I imported the `cowsay` library, to say when the user win money or lose.

    Guess a number between 1 and 10: 6
     »» You are wrong... You have a total of 0 tries...
    _______________________
     | WHAT A SHAME! |
    =======================
                            \
                             \
                              \
                               .--.
                              |o_o |
                              |:_/ |
                             //   \ \
                            (|     | )
                           /'\_   _/`\
                           \___)=(___/


or the user win:

    Guess a number between 1 and 10: 8
    ________________________
      | YOU ARE RIGHT! |
    ========================
                           \
                            \
                             \
                              \
                               ("`-'  '-/") .___..--' ' "`-._
                                ` *_ *  )    `-.   (      ) .`-.__. `)
                                 (_Y_.) ' ._   )   `._` ;  `` -. .-'
                              _.. `--'_..-_/   /--' _ .' ,4
                             ( i l ),-''  ( l i),'  ( ( ! .-'


# Functions

The project have a total of six projects including main, these are:

+ ### `is_correct(dollars, bet)`
This function receive 2 variables, and is used to check if the bet is bigger than the dollar, and if it is, the user is prompt with the massage:

 `You don't have that much money to bet, try again...`

 if it doesn't we receive a Boolean value and continue.

 + ### `table_text(dollars, bet, phrase, bet_show=True)`

 Return a blue table that the header is the `phrase` and the value of the `dollars` and `bet` bellow, in case the `bet_show` is equals to `False` the function returns a table with only the `dollars`.

    bet_show = True
    +-----------------------------+
    | WELCOME TO CS CASINO        |
    +=============================+
    |                             |
    | »»» Total money:    $100.00 |
    |                             |
    | »»» Bet:            $50.00  |
    |                             |
    +-----------------------------+

and

    bet_show=False
    +----------------------------+
    | WELCOME TO CS CASINO       |
    +============================+
    |                            |
    | »»» Total money:    $51.75 |
    |                            |
    +----------------------------+


 + ### `first_game(dollars, bet)`

 This function makes the first game, work as a guesser, the computer will choose a number and you have to try to guess this number (a total of 4 tries), and if you guess the number right the money that you bet it's multiplied by 1,75.

 + ### `second_game(dollars, bet)`

 This function calls the secong game that works like a slot machine, that is choosen 3 random emoji and if this 3 emoji is equals so than you win, and the money is multiplied by 5 (because it´s really hard to win).

  + ### `total_dollar(dollars)`

  Return the dollars left, and is used to check the actual dollars, to see `if dollars == 0`, we need to break, and stop the game.


#### Student: Wilton Machado