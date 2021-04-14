import unittest
import main


class TestCard(unittest.TestCase):

    card = main.Card('6', '♠')

    def test_str(self):
        self.assertEqual(str(self.card), '6♠')

    def test_get_int_value(self):

        self.assertEqual(self.card.get_int_value(), 6)


class TestDeck(unittest.TestCase):

    deck = main.Deck()

    def test_draw_returns_card(self):
        self.assertIsInstance(self.deck.draw(), main.Card)


class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = main.Hand()
        self.hand.hand = [main.Card('2', '♠'), main.Card('3', '♠'), main.Card('4', '♠')]
        self.deck = main.Deck()

    def test_print_hand(self):
        self.assertEqual(self.hand.print_hand(), '2♠, 3♠, 4♠')

    def test_draw_length(self):     # ISSUE: Requires internal Deck
        # self.hand.draw()
        # self.assertEqual(len(self.hand), 4)
        pass

    def test_draw_is_card(self):    # ISSUE: Requires internal Deck
        # deck = main.Deck()
        # self.hand.draw()
        # self.assertIsInstance(self.hand[3], main.Card)
        pass

    def test_hand_values(self):
        self.assertEqual(self.hand.hand_values(), ['2', '3', '4'])

    def test_hand_total(self):
        self.assertEqual(self.hand.hand_total(), 9)

    def test_hand_total_with_picture_card(self):
        self.hand.hand = [main.Card('J', '♦')]
        self.assertEqual(self.hand.hand_total(), 10)

    def test_hand_total_with_ace_as_eleven(self):
        self.hand.hand = [main.Card('A', '♥')]
        self.assertEqual(self.hand.hand_total(), 11)

    def test_hand_total_with_ace_as_one(self):
        self.hand.hand =[main.Card('10', '♥'), main.Card('2', '♥'), main.Card('A', '♥')]
        self.assertEqual(self.hand.hand_total(), 13)

    def test_clear_hand(self):
        self.hand.clear_hand()
        self.assertEqual(self.hand.hand, [])


class TestPlayer(unittest.TestCase):

    def test_init_default_balance(self):
        player = main.Player('test')
        self.assertEqual(player.balance, 1000)

    def test_init_balance_value_given(self):
        player = main.Player('test2', 2)
        self.assertEqual(player.balance, 2)


class TestFileReadWrite(unittest.TestCase):

    def setUp(self):
        self.file = open('test_accounts.txt',  mode='w+')

    def test_write(self):
        self.file.write('test')

    def test_read(self):
        pass

    def tearDown(self):
        self.file.close()


if __name__ == "__main__":
    unittest.main()
