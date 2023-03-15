from typing import Tuple

from cards.utils import Suit


class CardMethods:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hand, self.soft = self._points()

    def __str__(self):
        return f"Card {self.rank}, {self.suit}"

    def __repr__(self):
        return f"Card {self.rank}, {self.suit}"

    def _points(self) -> Tuple[int, int]:
        """
        
        :return:
        """
        return int(self.rank), int(self.rank)


def get_card(rank: int, suit: Suit) -> CardMethods:
    """

    :param rank:
    :param suit:
    :return:
    """
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return CardMethods(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure!!!")


def get_card_tuple_mapping(rank: int, suit: Suit) -> CardMethods:
    """

    :param rank:
    :param suit:
    :return:
    """
    class_, rank_str = {
        1: (AceCard, "A"),
        11: (FaceCard, "J"),
        12: (FaceCard, "Q"),
        13: (FaceCard, "K"),
    }.get(rank, (CardMethods, str(rank)))
    return class_(rank_str, suit)


def get_card_partial_mapping(rank: int, suit: Suit) -> CardMethods:
    """

    :param rank:
    :param suit:
    :return:
    """
    class_rank = {
        1: lambda suit: AceCard("A", suit),
        11: lambda suit: FaceCard("J", suit),
        12: lambda suit: FaceCard("Q", suit),
        13: lambda suit: FaceCard("K", suit),
    }.get(rank, lambda suit: CardMethods(str(rank), suit))
    return class_rank(suit)


def get_deck():
    """

    :return:
    """
    return [get_card(rank, suit) for rank in range(1, 14) for suit in iter(Suit)]


class AceCard(CardMethods):
    def _points(self) -> Tuple[int, int]:
        """

        :return:
        """
        return 1, 11


class FaceCard(CardMethods):
    def _points(self) -> Tuple[int, int]:
        """

        :return:
        """
        return 10, 10
