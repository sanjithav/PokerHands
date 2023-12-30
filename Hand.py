# File: Hand.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# Unique Number: XXXXX
# 
# Date Created: 11/1/2023
# Description of Program: this file is able to deal cards and check their validity for different poker hands. 


""" This file includes a class Hand which implements a hand of five playing
    cards, where cards are defined in the Card class.   

    The Hand class defines the following methods:

    Hand( source, fromDeck ):  creates a new hand object of 5 Cards. This happens
         in one of two ways depending on the value of fromDeck: 
         (1) if fromDeck is True, deal 5 cards from an existing deck
             passed as source, 
         (2) if fromDeck is not True, create the cards from a list of 5 card 
             specifiers passed as source, e.g., ("2S", "9S", "TC", "AH", "4D") 
             will create a hand containing the 2 of Spades, 9 of Spades, 10 of Clubs, 
             Ace of Hearts, and 4 of Diamonds.  Generating a single card from a 
             spec is implemented in the Card class.  You need to check that this
             list is legal (contains exactly 5 legal card specifiers, all distinct).
    h.__str__(): generate the print representation of Hand h, using the
         str function on each of the individual Cards it contains (see the Deck
         class for a model for this);
    h.getCard( i ): recall that h is a hand of 5 Cards.  This provides a 
         way of getting the ith card from the hand, for example, to iterate 
         through the hand in a loop. 

    This file also contains a number of other functions (outside the class), mainly
    to allow evaluating a hand in the sense of playing Poker.  You can have as many
    functions as you need, but you must have the function evaluateHand( hand ). 
    Given a hand, it prints the hand and then the "evaluation" of the hand in 
    the sense of a Poker hand.  This is described in detail in the assignment description.   

"""

################################################################################
#                                                                              #
#                                 Hand Class                                   #
#                                                                              #
################################################################################

# I don't need to import Card, since Deck already does.
from Deck import *

def isLegalCardList( l ):
    """ Check that list l contains 5 legal card specifiers, 
        all distinct. You can assume that it's a list. """
    # You'll need to fill this in
    if(len(l)==5):
        for i in range(5):
            if(l[0]==l[i] and i!=0):
                return False
            if(l[1]==l[i] and i!=1):
                return False
            if(l[2]==l[i] and i!=2):
                return False
            if(l[3]==l[i] and i!=3):
                return False            
            if(l[4]==l[i] and i!=4):
                return False
        return True
    else:
        return False
    pass  

class Hand:

    def __init__(self, source, fromDeck = True):
        """ A hand is simply a list of 5 cards, dealt from the deck
            or given as a list of five card specifiers.  If fromDeck
            is True, expect to deal from a deck passed as source. 
            If False, expect source to be a list of five Card specifiers.
            Create the hand from the specified cards.
        """
        if fromDeck:
            if ( len(source) < 5 ):
                print ( "Not enough cards left!" )
                return None
            self.__cards = []
            for i in range(5):
                card = source.deal()              # deal next card
                self.__cards.append(card)         # append it to the hand
        elif not isLegalCardList( source ):
            print("Illegal card list provided.")
        else:
            self.__cards = []
            for i in range(5):
                card= Card(source[i])
                self.__cards.append(card)
            # fill in this code, to generate a hand from
            # a list of Card specifiers.  You can assume that
            # source is a list,

    def __str__(self):
        """ Generates the print image of the Hand. """
        result=""
        for i in self.__cards:
            result+=rankName(i.getRank())+" of "+suitName(i.getSuit())+"\n"
        return result

    def getCard( self, i ):
        if 0<=i<=4:
            return self.__cards[i]
        else:
            return None
        """ Get the ith card from the hand, where 
            i in [0..4]. Return None if i is not
            legal. """
        
            
################################################################################
#                                                                              #
#                                Evaluate Hand                                 #
#                                                                              #
################################################################################

def processHand( hand ):
    myRanks=[0]*13
    mySuits=[0]*4
    for i in range(5):
        c=(hand.getCard(i)).getRank()
        if(c=="A"):
            myRanks[12]+=1
        elif(c=="K"):
            myRanks[11]+=1
        elif(c=="Q"):
            myRanks[10]+=1
        elif(c=="J"):
            myRanks[9]+=1
        elif(c=="T"):
            myRanks[8]+=1
        else:
            myRanks[int(c)-2]+=1

        s=(hand.getCard(i)).getSuit()
        if(s=="S"):
            mySuits[0]+=1
        elif(s=="D"):
            mySuits[1]+=1
        elif(s=="H"):
            mySuits[2]+=1
        elif(s=="C"):
            mySuits[3]+=1
    
    return myRanks, mySuits
    """ Given a poker hand, create and return two lists which
        record the ranks and suits in the hand. """

# You'll need to define all of the auxiliary functions called by
# evaluateHand.  Notice that these auxiliary functions don't all
# need both myRanks and mySuits, but I decided to pass them both
# just to make the interface more uniform.  You can change that 
# if you want to.

def hasPair( myRanks, mySuits ):
    if 2 in myRanks:
        return True
    else:
        return False
    
def hasTwoPair( myRanks, mySuits ):
    count=0
    for i in range(len(myRanks)-1):
        if 2 == myRanks[i]:
            count+=1
        if count>=2:            
            return True
    return False

def hasThreeOfAKind( myRanks, mySuits ):
    if 3 in myRanks:
        return True
    else:
        return False

def hasStraight( myRanks, mySuits ):
    index=0
    if myRanks[0]==1 and myRanks[1]==1 and myRanks[2]==1 and myRanks[3]==1 and myRanks[12]==1:
        return True
    
    if 1 in myRanks:
        firstIndex=myRanks.index(1)
    else:
        return False

    if(firstIndex>len(myRanks)-5):
        return False

    for i in range(5):
            if myRanks[firstIndex+i]!=1:
                return False
    return True
        
def hasFlush( myRanks, mySuits ):
    if(5 in mySuits):
        return True
    else:
        return False
    
def hasFullHouse( myRanks, mySuits ):
    if ((2 in myRanks) and (3 in myRanks)):
        return True
    else:
        return False

def hasFourOfAKind( myRanks, mySuits ):
    if 4 in myRanks:
        return True
    else:
        return False
    
def hasStraightFlush( myRanks, mySuits ):
    if hasStraight(myRanks, mySuits) and hasFlush(myRanks, mySuits):
        return True
    else:
        return False
    
def hasRoyalFlush( myRanks, mySuits ):
    if hasFlush(myRanks, mySuits) and myRanks[8]==1 and myRanks[9]==1 and myRanks[10]==1 and myRanks[11]==1 and myRanks[12]:
        return True
    else:
        return False


# Add other recognizers here; evaluateHand tells you which ones you
# need.  I suggest doing them in "reverse order" so you define the 
# lowest hands first. Hopefully, you'll see why as you code them!

def evaluateHand( hand ):
    myRanks, mySuits = processHand( hand )
    print( hand )
    if hasRoyalFlush( myRanks, mySuits ):
        print( "Royal Flush" )
    elif hasStraightFlush( myRanks, mySuits ):
        print( "Straight Flush" )
    elif hasFourOfAKind( myRanks, mySuits ):
        print( "Four of a kind" )
    elif hasFullHouse( myRanks, mySuits ):
        print( "Full House" )
    elif hasFlush( myRanks, mySuits ):
        print( "Flush" )
    elif hasStraight( myRanks, mySuits ):
        print( "Straight" )
    elif hasThreeOfAKind( myRanks, mySuits ):
        print( "Three of a kind" )
    elif hasTwoPair( myRanks, mySuits ):
        print( "Two pair" )
    elif hasPair( myRanks, mySuits ):
        print( "Pair" )
    else:
        print( "Nothing" )

# This is some test code.  You can modify this or write your
# own.  You certainly should test additional hands. You can run 
# this in interactive mode with:
# 
# from Hand import *
# TestCode()
#
# You can also run this in batch mode by uncommenting the call to:
# TestCode()
#
# and running:
# 
# python3 Hand.py              # or whatever the python command is
#                              # is on your system. 

def TestCode():
    print("\nGenerating and printing deck")
    d = Deck()
    print(d)
    print("\nShuffling deck and printing deck")
    d.shuffle()
    print(d)

    print("\nGenerating hand from deck")
    h = Hand(d, True)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["as", "ad", "ah", "ac", "2d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["AS", "2S", "3C", "4H", "5D"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["2s", "9S", "tc", "AH", "4d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

# TestCode()
