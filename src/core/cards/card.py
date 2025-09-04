"""This module defines the base class for cards in the game."""


class Card:
    """Base class for all cards in the game."""

    def __init__(self, name: str) -> None:
        """Initializes a Card with a name."""
        self._name = name

    def __eq__(self, other: "Card") -> bool:
        """Checks equality between two Card instances."""
        if not isinstance(other, Card):
            return False
        if self is other:
            return True
        return self._name == other._name

    def __hash__(self) -> int:
        """Returns the hash of the Card instance."""
        return hash(self._name)

    @property
    def name(self) -> str:
        """Returns the name of the card."""
        return self._name
