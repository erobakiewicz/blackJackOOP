from enum import Enum


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


class Card:
    def __init__(self, rank: str, suit: Suit, hand: int, soft: int) -> None:
        self.rank = rank
        self.suit = suit
        self.hand = hand
        self.soft = soft


class NumberCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__("A", suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        rank_str = {11: "J", 12: "Q", 13: "K"}[rank]
        super().__init__(rank=rank_str, suit=suit, hand=10, soft=10)
