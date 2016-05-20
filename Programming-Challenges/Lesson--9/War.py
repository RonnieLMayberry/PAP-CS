'''
Created on Mar 12, 2015

@author: mayberryr
'''
# War
# Simulates the card game War.

import cards, games

class W_Card(cards.Card):
    """ A War Card. """
    ACE_VALUE = 13
    
    @property
    def value(self):
        if self.is_face_up:
            v = W_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
            return v

        
class W_Game(object):
    """ A War Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)

        self.dealer = W_Dealer("Dealer")

        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
           
    def play(self):
        self.deck.populate()
        self.deck.shuffle()
        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first 

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()                    
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tWelcome to the game of War!\n")
    
    names = []
    number = 2
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
    
    game = W_Game(names)
    
    again = None
    while again!= "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")
        
main()
input("\n\nPress the enter key to exit.")
