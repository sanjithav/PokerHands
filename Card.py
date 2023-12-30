################################################################################
#                                                                              #
#                                 Card Class                                   #
#                                                                              #
################################################################################

""" This class implements playing cards.  A card is
    specified with a string RS of two characters, where R denotes the
    rank and S the suit.  For example, "AH" denotes the Ace of
    Hearts, "4S" denotes the 4 of Spades.  Legal ranks and suits are
    defined by the constants CARDRANKS and CARDSUITS.  Note that we use
    "T" to designate a 10, so as to use only two characters for the 
    specifier. 

    The class defines the following methods:

    Card( RS ):  creates a new Card object of rank R and suit S;
    c.__str__(): generate the print representation of Card c;
    c.getRank(): return the rank of card c;
    c.getSuit(): return the suit of card c;
    comparisons <, >, <=, >=, == between two Card objects.

"""

# These two lists define the specifiers for rank and suits for generating
# new Card objects.  Notice that Ace is high in this enumeration, but can
# also be low.  For example, legal straights are (A, 2, 3, 4, 5) or 
# (T, J, Q, K, A).  Some code must take this into account. 
CARDRANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDSUITS = ['S', 'D', 'H', 'C']

# These are used to convert from rank/suit specification to the print names.
RANKNAMES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITNAMES = ['Spades', 'Diamonds', 'Hearts', 'Clubs']

# The following are useful auxiliary functions used in defining Card and elsewhere.

def isRank( r ):
    """ Recognizer for legal ranks. """
    return r.upper() in CARDRANKS

def isSuit( s ):
    """ Recognizer for legal suits. """
    return s.upper() in CARDSUITS

def isLegalCardSpecifier( s ):
    """ Recognizer for legal Card specifiers. """
    return type(s) == str and len(s) == 2 and isRank( s[0] ) and isSuit( s[1] )

def rankName ( r ):
    """ Converts a rank specifier into a rank name. """
    if isRank( r ):
        index = CARDRANKS.index( r.upper() )
        return RANKNAMES[index]
    else:
        print("Illegal rank designation:", r)

def suitName ( s ):
    """ Converts a suit specifier into a suit name. """
    if isSuit( s ):
        index = CARDSUITS.index( s.upper() )
        return SUITNAMES[index]
    else:
        print("Illegal suit designation:", r)

class Card:
    """ Define a Card object with suit and rank. """

    def __init__(self, rankAndSuit):
        """Create a Card object with the given rank and suit. Parameter
           rankAndSuit is a Card specifier, a string RS of length 2, where
           R is rank and S the suit. """
        if not isLegalCardSpecifier( rankAndSuit ):
            # We don't create a Card object if the spec is not legal.
            print ("Not a legal card specification:", rankAndSuit)
        else:
            self.__rank = rankAndSuit[0].upper()
            self.__suit = rankAndSuit[1].upper()

    def __str__(self):
        """Return a string that is the print representation
        of this Card's value."""
        return rankName( self.__rank ) + " of " + suitName( self.__suit )

    def getRank(self):
        """Return Card's rank."""
        return self.__rank

    def getSuit(self):
        """Return Card's suit."""
        return self.__suit

    # The following three methods allow comparisons between Card objects, using
    # the conventional comparators.  Comparison ignores suit; Ace is considered high. 

    def __lt__(self, other):
        """Adding this function allows comparing Cards using
        conventional syntax. e.g., c1 < c2."""
        return ( CARDRANKS.index(self.__rank) < CARDRANKS.index(other.getRank() ))

    def __eq__(self, other):
        return ( CARDRANKS.index(self.__rank) == CARDRANKS.index(other.getRank() ))

    def __le__(self, other):
        return ( CARDRANKS.index(self.__rank) <= CARDRANKS.index(other.getRank() ))

