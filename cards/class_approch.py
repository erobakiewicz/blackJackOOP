import random

from cards.utils import Suit


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


def card(rank: int, suit: Suit) -> Card:
    """

    :param rank:
    :param suit:
    :return:
    """
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit, rank, rank)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit)
    raise Exception("Design Failure")


class Deck:
    def __init__(self) -> None:
        self._cards = [card(r + 1, s) for r in range(13) for s in iter(Suit)]
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()


class DeckList(list):
    def __init__(self) -> None:
        super().__init__(card(r + 1, s) for r in range(13) for s in iter(Suit))
        random.shuffle(self)
