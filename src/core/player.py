"""
This module contains player-related classes and functions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.core.cards.action_card import ActionCard
from src.core.cards.card import Card

if TYPE_CHECKING:
    from src.core.cards.roles import Role


class Player:
    """
    Represents a player in the game.
    """

    def __init__(self, name: str, role: Role, hand: list[Card], bench: list[Card]) -> None:
        """
        Initializes a Player with a name, role, hand of cards, and bench of cards.
        """
        self.__name = name
        self.__role = role
        self.__hand = hand
        self.__bench = bench
        self.__scores = list[int]()

    @property
    def name(self) -> str:
        """Returns the name of the player."""
        return self.__name

    @property
    def role(self) -> str:
        """Returns the role of the player."""
        return self.__role

    @role.setter
    def role(self, role: Role) -> None:
        """Sets the role of the player."""
        self.__role = role

    @property
    def hand(self) -> list[Card]:
        """Returns the player's hand of cards."""
        return self.__hand

    @property
    def bench(self) -> list[Card]:
        """Returns the player's bench of cards."""
        return self.__bench

    def __eq__(self, other: object) -> bool:
        """Checks equality between two Player instances."""
        if not isinstance(other, Player):
            return NotImplemented
        if self is other:
            return True
        return (
            self.__name == other.__name
            and self.__role == other.__role
            and self.__hand == other.__hand
            and self.__bench == other.__bench
            and self.__scores == other.__scores
        )

    def __hash__(self) -> int:
        """Returns the hash of the Player instance."""
        return hash(
            (
                self.__name,
                self.__role,
                tuple(self.__hand),
                tuple(self.__bench),
                tuple(self.__scores),
            )
        )

    def draw(self, deck: list[Card] | Card) -> None:
        """Draws a card or a list of cards from the deck to the player's hand."""
        if isinstance(deck, Card):
            self.__hand.append(deck)
        elif (
            isinstance(deck, list)
            and len(deck) > 0
            and all(isinstance(card, Card) for card in deck)
        ):
            card_drawn = deck.pop(0)
            self.__hand.append(card_drawn)
        else:
            msg = "Deck must be a Card or a non-empty list of Cards."
            raise ValueError(msg)

    def discard(self, card: Card) -> tuple[bool, str]:
        """
        Discards a card from the player's hand.
        Returns True if the card was successfully discarded, False otherwise.
        """
        if card in self.__hand:
            self.__hand.remove(card)
            return True, "The card has been discarded."
        return False, "The card is not in the player's hand."

    def empty_hand(self) -> None:
        """Empties the player's hand."""
        self.__hand.clear()

    def is_blocked(self) -> bool:
        """
        Checks if the player is blocked by any offensive action cards on their bench.
        Returns True if the player is blocked, False otherwise.
        """
        return any(isinstance(card, ActionCard) and card.is_offensive for card in self.__bench)
