from random import randint


class Deck:
    def __init__(self):
        pass


class Hand:
    def __init__(self):
        self.hand = []

    def clear_hand(self):
        self.hand = []


class Player(Hand):

    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance

    def add_balance(self, amount):
        self.balance += amount

    def remove_balance(self, amount):
        self.balance -= amount


def place_bet():
    pass


def play():
    pass
    player_cards = []
    dealer_cards = []


if __name__ == '__main__':
    player = Player('player')
    print(f"{player.name}'s balance: {player.balance}")
