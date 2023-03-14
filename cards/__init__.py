from typing import Tuple
from enum import Enum


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hand, self.soft = self._points()

    def __str__(self):
        return f"Card {self.rank}, {self.suit}"

    def __repr__(self):
        return f"Card {self.rank}, {self.suit}"

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)


def get_card(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure!!!")


def get_card_tuple_mapping(rank: int, suit: Suit) -> Card:
    class_, rank_str = {
        1: (AceCard, "A"),
        11: (FaceCard, "J"),
        12: (FaceCard, "Q"),
        13: (FaceCard, "K"),
    }.get(rank, (Card, str(rank)))
    return class_(rank_str, suit)


def get_deck():
    return [get_card(rank, suit) for rank in range(1, 14) for suit in iter(Suit)]


class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11


class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10
