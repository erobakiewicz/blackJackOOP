import random
from typing import List, overload, Union, Optional, cast, Callable, Iterable

from cards.card import Card, card, BlackJackCard, card21
from cards.utils import Suit


class Deck21(list):
    def __init__(
        self, decks: int = 6, factory: Callable[[int, Suit], BlackJackCard] = card21
    ) -> None:
        super().__init__()
        for i in range(decks):
            self.extend(
                factory(r + 1, s) for r in range(13) for s in cast(Iterable[Suit], Suit)
            )
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()


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


class DeckShoe(list):
    def __init__(self, decks: int = 6) -> None:
        super().__init__(
            card(r + 1, s) for r in range(13) for s in iter(Suit) for d in range(decks)
        )
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()


class Hand:
    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card: Card = dealer_card
        self.cards: List[Card] = list(cards)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.dealer_card}{self.cards}"

    def append_cards(self, card: Card):
        self.cards.append(card)

    def hard_total(self) -> int:
        return sum(c.hard for c in self.cards)

    def soft_total(self) -> int:
        return sum(c.soft for c in self.cards)


class HandOverload:
    @overload
    def __init__(self, arg1: "HandOverload") -> None:
        ...

    @overload
    def __init__(self, arg1: Card, arg2: Card, arg3: Card) -> None:
        ...

    def __init__(
        self,
        arg1: Union[Card, "HandOverload"],
        arg2: Optional[Card] = None,
        arg3: Optional[Card] = None,
    ) -> None:
        self.dealer_card: Card
        self.cards: Card

        if isinstance(arg1, HandOverload) and not arg2 and not arg3:
            # Clone existing hand
            self.dealer_card = arg1.dealer_card
            self.cards = arg1.cards
        elif (
            isinstance(arg1, Card) and isinstance(arg2, Card) and isinstance(arg3, Card)
        ):
            # build resh hand
            self.dealer_card = cast(Card, arg1)
            self.cards = [arg2, arg3]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {self.dealer_card!r}, *{self.cards}"


class HandOverloadSplit:
    @overload
    def __init__(self, arg1: "HandOverloadSplit") -> None:
        ...

    @overload
    def __init__(self, arg1: "HandOverloadSplit", arg2: Card, *, split: int) -> None:
        ...

    @overload
    def __init__(self, arg1: Card, arg2: Card, arg3: Card) -> None:
        ...

    def __init__(
        self,
        arg1: Union["HandOverloadSplit", Card],
        arg2: Optional[Card] = None,
        arg3: Optional[Card] = None,
        split: Optional[int] = None,
    ):
        self.dealer_card: Card
        self.cards: List[Card]

        if isinstance(arg1, HandOverloadSplit):
            # Clone existing hand
            self.dealer_card = arg1.dealer_card
            self.cards = arg1.cards
        elif (
            isinstance(arg1, HandOverloadSplit)
            and isinstance(arg2, Card)
            and "split" is not None
        ):
            # split existing hand
            self.dealer_card = arg1.dealer_card
            self.cards = [arg1.cards[split], arg2]
        elif (
            isinstance(arg1, Card) and isinstance(arg2, Card) and isinstance(arg3, Card)
        ):
            # build new hand
            self.dealer_card = arg1
            self.cards = [arg2, arg3]

        else:
            raise TypeError("Invalid constructor")

    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))


class HandProperty:
    def __init__(self, dealer_card: BlackJackCard, *cards: BlackJackCard) -> None:
        self._cards: List[BlackJackCard] = list(cards)
        self.dealer_card: BlackJackCard = dealer_card

    def __str__(self) -> str:
        return ", ".join(map(str, self.card))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({self.dealer_card!r}, "
            f"{', '.join(map(repr, self.card))})"
        )

    @property
    def card(self) -> List[BlackJackCard]:
        return self._cards

    @card.setter
    def card(self, aCard: BlackJackCard) -> None:
        raise NotImplemented

    @card.deleter
    def card(self, aCard: BlackJackCard) -> None:
        raise NotImplemented

    def split(self, deck: Deck21) -> "Hand":
        assert self._cards[0].rank == self._cards[1].rank
        c1 = self._cards[-1]
        del self.card
        self.card = deck.pop()
        h_new = self.__class__(self.dealer_card, c1, deck.pop())
        return h_new
