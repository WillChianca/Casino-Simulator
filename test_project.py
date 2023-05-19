import project

dollars = 100
bet = 50

def test_table_text():
    global dollars
    global bet

    assert project.table_text(dollars, bet, 'Hi') == '''\033[34;1m+-----------------------------+
| Hi                          |
+=============================+
|                             |
| »»» Total money:    $100.00 |
|                             |
| »»» Bet:            $50.00  |
|                             |
+-----------------------------+\033[m
'''

    assert project.table_text(dollars, bet, 'WELCOME TO CS CASINO') == '''\033[34;1m+-----------------------------+
| WELCOME TO CS CASINO        |
+=============================+
|                             |
| »»» Total money:    $100.00 |
|                             |
| »»» Bet:            $50.00  |
|                             |
+-----------------------------+\033[m
'''


def test_total_dollar():
    global dollars
    assert project.total_dollar(dollars) == 100.0

    new_dollars = 50
    assert project.total_dollar(new_dollars) == 50.0


def test_is_correct():
    global dollars
    global bet

    assert project.is_correct(dollars, bet) == True


def test_first_game():
    # The test of the first game is never going to work properly because it's a game
    # And games work with random things, so the output can never be the same always
    ''


def test_second_game():
    # The test of the second game is never going to work properly because it's a game
    # And games work with random things, so the output can never be the same always.
    # But here is a test that can or can not work

    '''
    global dollars
    global bet

    assert project.second_game(dollars, bet) == 50

    new_bet = 100
    assert project.second_game(dollars, new_bet) == 0.0'''

