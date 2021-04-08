from random import randint


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value}{self.suit}'

    # Returns integer value of card
    def get_int_value(self):
        if self.value == 'A':   # Optional value of 11 assigned in Hand.hand_total
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
                self.deck.append(Card(value, suit))

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

    def draw(self):
        self.hand.append(d.draw())

    def hand_values(self):
        return list(map(lambda card: card.value, self.hand ))

    def hand_total(self):
        total = sum(map(lambda card: card.get_int_value(), self.hand))
        if 'A' in self.hand_values() and total <= 11:
            total += 10
        return total


class Player(Hand):
    def __init__(self, name, balance=1000):
        Hand.__init__(self)
        self.name = name
        self.balance = balance


def get_bet():
    user_in = int(input('Enter bet amount: '))
    if user_in > player.balance:
        print('Invalid input.')
        return get_bet()
    return int(user_in)


def check_bust(total):
    return total > 21


def check_win(total):
    if total <= 21:
        return True


def hit_stick():
    print(f'Your cards: {player.print_hand()}')
    print(f'Card total: {player.hand_total()}')
    if check_bust(player.hand_total()):
        print('Bust!')
        return False
    if player.hand_total() == 21:
        return True
    user_in = input('Hit or Stick? (h/s): ')
    if user_in == 'h':
        player.draw()
        return hit_stick()
    elif user_in == 's':
        return check_win(player.hand_total())
    else:
        print('Invalid input.')
        hit_stick()


def play():
    print(f"Your balance: {player.balance}")
    bet = get_bet()
    player.draw()
    player.draw()
    if hit_stick():
        print('You win!')
        player.balance += bet
    else:
        print('You lose.')
        player.balance -= bet
    user_in = input('Play again? (y/n)')
    if user_in == 'y':
        player.clear_hand()
        dealer.clear_hand()
        global d
        d = Deck()
        play()
    elif user_in == 'n':
        return


if __name__ == '__main__':
    player = Player('player')
    dealer = Hand()
    d = Deck()
    play()
