import abc

from cards.hand import Hand


class GameStrategy:
    """Stateless class which contains only methods for game strategy."""

    def insurance(self, hand: Hand) -> bool:
        return False

    def split(self, hand: Hand) -> bool:
        return False

    def double(self, hand: Hand) -> bool:
        return False

    def hit(self, hand: Hand) -> bool:
        return sum(c.hard for c in hand.cards) <= 17


class BettingStrategy(metaclass=abc.ABCMeta):
    """Abstract class - ensures that any implementation of concrete class that inherits from this one
    has to have all marked as 'abstract' methods implemented.

    """

    @abc.abstractmethod
    def bet(self) -> int:
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass
