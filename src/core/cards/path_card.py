"""This module defines the base class for path cards in the game."""

from json import load
from pathlib import Path

from src.core.cards.card import Card

path_card_data = load(Path.open("src/core/cards/cards_data.json"))["path_card"]


class CardConnections:
    """Enum-like class for card connections."""

    def __init__(self, up: int = 0, right: int = 0, down: int = 0, left: int = 0) -> None:
        """Initializes CardConnections with connection values."""
        self.UP = up
        self.RIGHT = right
        self.DOWN = down
        self.LEFT = left

    @classmethod
    def from_dict(cls, data: dict) -> "CardConnections":
        """Creates a CardConnections instance from a dictionary."""
        connections = cls()
        connections.UP = data.get("UP", 0)
        connections.RIGHT = data.get("RIGHT", 0)
        connections.DOWN = data.get("DOWN", 0)
        connections.LEFT = data.get("LEFT", 0)
        return connections


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
            up=self._connections.DOWN,
            right=self._connections.LEFT,
            down=self._connections.UP,
            left=self._connections.RIGHT,
        )

    @property
    def connections(self) -> CardConnections:
        """Returns the connections of the path card."""
        return self._connections


class StartCard(PathCard):
    """Card representing the starting point of the miners' path."""

    def __init__(self) -> None:
        """Initializes a StartCard with predefined connections."""
        connections = CardConnections.from_dict(path_card_data["START"]["connections"])
        super().__init__("START", connections)
