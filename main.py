from random import randint


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value}{self.suit}'

    # Returns integer value of card
    def get_value(self):
        if self.value == 'A':
            return 1
        if self.value in ('J', 'Q', 'K'):
            return 10
        else:
            return int(self.value)


class Deck:
    def __init__(self):
        self.deck = []
        suits = ['♠', '♥', '♦', '♣']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def draw(self):
        card = self.deck[randint(0, len(self.deck)-1)]
        self.deck.remove(card)
        return card


class Hand:
    def __init__(self):
        self.hand = []

    def print_hand(self):
        return ', '.join(map(lambda card: str(card), self.hand))

    def clear_hand(self):
        self.hand = []


class Player(Hand):

    def __init__(self, name, balance=1000):
        Hand.__init__(self)
        self.name = name
        self.balance = balance

    def place_bet(self):
        pass


def play():
    player.hand.append(d.draw())
    player.hand.append(d.draw())
    print(f'Your cards: {player.print_hand()}')


if __name__ == '__main__':
    player = Player('player')
    d = Deck()
    print(f"{player.name}'s balance: {player.balance}")
    play()
