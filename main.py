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


def read_accounts_file():
    users = {}
    with open('accounts.txt', mode='r') as file_read:
        for line in file_read:
            item = line.split()
            users[item[0]] = item[1]
    return users


def write_accounts_file():
    with open('accounts.txt', mode='w') as file_write:
        for k, v in accounts.items():
            file_write.write(k + ' ' + v)


def update_player_account():
    accounts[player.name] = str(player.balance)


def get_bet():
    user_in = int(input('Enter bet amount: '))
    if user_in > player.balance:
        print('Invalid input.')
        return get_bet()
    return int(user_in)


def dealer_turn():
    total = dealer.hand_total()
    print(f"\nDealer's cards: {dealer.print_hand()}")
    if total > 21:
        print('Dealer bust!')
    elif total < DEALER_STICK:
        print('Dealer draws...')
        dealer.draw()
        return dealer_turn()
    else:
        print('Dealer sticks.')
    return total


def hit_stick():
    total = player.hand_total()
    print(f'\nYour cards: {player.print_hand()}')
    print(f'Card total: {total}')
    if total > 21:
        print('Bust!')
        return total
    print(f"Dealer's card: {str(dealer.hand[0])}")
    user_in = input('Hit or Stick? (h/s): ')
    if user_in == 'h':
        player.draw()
        return hit_stick()
    elif user_in == 's':
        return total
    else:
        print('Invalid input.')
        hit_stick()


def play():
    print(f"\nYour balance: {player.balance}")
    bet = get_bet()
    player.draw()
    dealer.draw()
    player.draw()
    dealer.draw()
    player_result = hit_stick()
    print('-' * 30)
    dealer_result = dealer_turn()
    print(f'\nYour cards: {player.print_hand()} | total = {player_result}')
    print(f"Dealer's cards: {dealer.print_hand()} | total = {dealer_result}\n")
    if player_result <= 21 < dealer_result or dealer_result < player_result <= 21:
        print('You win!')
        player.balance += bet
        print(f'+ {bet}')
    elif dealer_result == player_result or dealer_result > 22 < player_result:
        print("It's a tie!")
    else:
        print('You lose.')
        player.balance -= bet
        print(f'- {bet}')
    user_in = input('\nPlay again? (y/n): ')
    if user_in == 'y':
        player.clear_hand()
        dealer.clear_hand()
        global d
        d = Deck()    # Resetting deck by creating new object - is this bad practice?
        play()
    elif user_in == 'n':
        return


DEALER_STICK = 18   # The lowest value that the dealer will 'stick' at


if __name__ == '__main__':
    accounts = read_accounts_file()
    # select_account()
    # login()
    player = Player('test', int(accounts['test']))
    dealer = Hand()
    d = Deck()
    play()
    update_player_account()
    write_accounts_file()
