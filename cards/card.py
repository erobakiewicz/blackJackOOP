import random
from typing import Any, cast, Callable, Iterable

from cards.utils import Suit


class BlackJackCard:
    """Abstract superclass"""

    __slots__ = ("rank", "suit", "hard", "soft")

    def __init__(self, rank: str, suit: "Suit", hard: int, soft: int) -> None:
        self.soft = soft
        self.hard = hard
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(rank={self.rank}, suit={self.suit}, hard={self.hard}, soft={self.soft}"

    def __str__(self) -> str:
        return f"{self.rank} {self.suit}"

    def __eq__(self, other: Any) -> bool:
        try:
            return self.rank <= cast(BlackJackCard, other).rank
        except AttributeError:
            return NotImplemented


class Ace21Card(BlackJackCard):
    __slots__ = ("rank", "suit", "hard", "soft")

    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__("A", suit, 1, 11)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (rank=1, suit={self.suit!r}"


class Face21Card(BlackJackCard):
    __slots__ = ("rank", "suit", "hard", "soft")

    def __init__(self, rank: int, suit: Suit) -> None:
        rank_str = {11: "J", 12: "Q", 13: "K"}[rank]
        super().__init__(rank_str, suit, 10, 10)

    def __repr__(self) -> str:
        rank_num = {"J": 1, "Q": 12, "K": 13}[self.rank]
        return f"{self.__class__.__name__} (rank={rank_num}, suit={self.suit!r}"


class Number21Card(BlackJackCard):
    __slots__ = ("rank", "suit", "hard", "soft")

    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__(str(rank), suit, rank, rank)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (rank={self.rank}, suit={self.suit!r}"


def card21(rank: int, suit: Suit) -> BlackJackCard:
    if rank == 1:
        return Ace21Card(rank, suit)
    elif 2 <= rank < 11:
        return Number21Card(rank, suit)
    elif 11 <= rank <= 14:
        return Face21Card(rank, suit)
    else:
        raise TypeError


class Card:
    def __init__(self, rank: str, suit: Suit, hard: int, soft: int) -> None:
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return f"Card {self.rank}, {self.suit}"


class NumberCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__("A", suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        rank_str = {11: "J", 12: "Q", 13: "K"}[rank]
        super().__init__(rank_str, suit, 10, 10)


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
