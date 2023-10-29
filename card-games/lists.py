"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    number = [number, number + 1, number + 2]

    return number


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    round_1_2 = rounds_1 + rounds_2

    return round_1_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True

    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    #fail
    """
    if ((hand[0] + hand[-1]) / 2) == card_average(hand):
        return True

    if (hand[int(len(hand)/2-0.5)]) == card_average(hand):
        return True
    """
    #fail
    #ennek a feladatnak a tesztje valami döbbenetesen haszontalan abban hogy rájöjjek mi a baj, azt se tudom melyik része jó melyik nem

    two_card = (hand[0] + hand[-1]) / 2 # egyenlő a kártya első és utolsó lapjának összegének felével, vagyis az átlagával
    if two_card == card_average(hand): # ha az előző sorban lévő szám egyenlő a pontos átlaggal amit az előző function számol ki
        return True # térjen vissza igazra

    mid_card = len(hand) // 2 # a kártyák számának a fele, lefelé kerekítve az páratlan kártyaszám esetén a középső kártya a medián kéne legyen, 3 lap esetén 1 lesz és a 0, 1, 2 indexek közül az 1 a középső, 5 lap esetén, 2, és a 0, 1, 2, 3, 4 indexek közül a 2 az

    if hand[mid_card] == card_average(hand): # ha a középső kártya a sorban egyenlő a tényleges átlaggal
        return True # térjen vissza igazra

    return False # egyébként hamis

#már megcsináltam, de benne hagyom a kommenteket, egy szenvedés volt, mert egyszerűen nem tudtam MI és HOL hibázik, hány rossz, hány stimmel, nem tudom olvasni a teszteredményt egyszerűen :-( kellenének a részeredmények  hogy melyikek stimmelnek a feladaton belül
# az utolsó dolog amit igazítanom kellett hogy sokáig len(hand) // 2 + 1 volt hogy tényleges mediánt keressek de mivel 0tól kezdődik az index nekem 1-el kissebb szám kell

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd = []
    even = []
    hand_o = []
    hand_e = []
    odd.extend(range(1, len(hand), 2))
    even.extend(range(0, len(hand), 2))

    #c = 0

    for c in odd:
        hand_o.append(hand[c])
        #c += 1

    #c = 0

    for c in even:
        hand_e.append(hand[c]) # biztos nagyon ronda és felesleges dolgok vannak benne és forral kéne ha kell-e egyáltalán ilyen bele de így sikerült
        #c += 1

    if card_average(hand_o) == card_average(hand_e):
        return True

    return False





def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] += hand [-1]

    return hand
