"""This module defines the base class for path cards in the game."""

from core.cards.card import Card


class CardConnections:
    """Enum-like class for card connections."""

    TOP = int
    RIGHT = int
    BOTTOM = int
    LEFT = int


class PathCard(Card):
    """Card representing the path taken by miners exploring the mine.
    These cards can be placed on the game board."""

    def __init__(self, name: str, connections: CardConnections) -> None:
        """Initializes a PathCard with a name and its connections."""
        self._connections = connections
        super().__init__(name)

    def flip(self) -> None:
        """Flips the card 180 degrees."""
        self._connections = CardConnections(
            top=self._connections.BOTTOM,
            right=self._connections.LEFT,
            bottom=self._connections.TOP,
            left=self._connections.RIGHT,
        )
