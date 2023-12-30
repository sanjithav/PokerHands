################################################################################
#                                                                              #
#                                 Deck Class                                   #
#                                                                              #
################################################################################

""" This class implements a deck of 52 playing cards, where cards are 
    defined in the Card class.   A deck is just a list of Card objects, one 
    for each legal combination of rank and suit. 

    The class defines the following methods:

    Deck( ):  creates a new Deck object of 52 Cards;
    d.__str__(): generate the print representation of Deck d, using the
         str function on each of the individual Cards it contains;
    d.shuffle(): replace d by a random permutation of d (the works since
         d is represented as a mutable list of Cards;
    d.deal(): remove a Card from the front of the deck and return it;
    d.len(): return the number of Cards remaining in deck d.
    comparisons <, >, <=, >=, == between two Card objects.

"""

import random
from Card import *

class Deck:
    """Definition of the Deck class.  Each Deck is just 
       a list of cards, one for each legal rank and suit
       combination.

    """

    def __init__(self):
        """Return a new deck of Cards, one from each rank/suit combination. """
        self.__cards = []
        for S in CARDSUITS:
            for R in CARDRANKS:
                # Create the card specifier string
                rankAndSuit = R + S
                # Create the Card object
                c = Card( rankAndSuit )
                self.__cards.append(c)

    def __len__(self):
        """Returns the number of cards left in the deck."""
        return len(self.__cards)

    def __str__(self):
        """ Generates the print image of the Deck.  Notice this
            is just the concatenation of the print images of the
            Cards in the deck. """
        result = ""
        for c in self.__cards:
            result = result + str(c) + "\n"
        return result

    def shuffle(self):
        """Shuffle the cards, using the shuffle method from 
           the random library. """
        random.shuffle(self.__cards)

    def deal(self):
        """Remove and return the top card, or None
        if the deck is empty. Modifies the deck. """
        if len(self) == 0:
            print("Attempting to deal from an empty deck.")
            return None
        else:
            # Be sure to deal from the top of the deck.
            # People have gotten shot for dealing from
            # the bottom of the deck!
            return self.__cards.pop(0)

