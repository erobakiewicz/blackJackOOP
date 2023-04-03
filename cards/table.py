from cards.hand import Deck, Hand


class Table:
    def __init__(self) -> None:
        self.deck = Deck()

    def place_bet(self, amount: int) -> None:
        print(f"Bet {amount} placed")

    def get_hand(self) -> Hand:
        try:
            self.hand = Hand(self.deck.pop(), self.deck.pop(), self.deck.pop())
            self.hole_card = self.deck.pop()
        except IndexError:
            print("Out of cards, need to shuffle and try again!")
            self.deck = Deck()
            self.get_hand()
        print(f"Deal, {self.hand}")
        return self.hand

    def can_unsure(self, hand: Hand) -> bool:
        return hand.dealer_card.insure
