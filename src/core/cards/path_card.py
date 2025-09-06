"""This module defines the base class for path cards in the game."""

from json import load
from pathlib import Path
from random import shuffle

from src.core.cards.card import Card

path_card_data = load(Path.open("src/core/cards/cards_data.json"))["path_card"]


class CardConnections:
    """Enum-like class for card connections."""

    UP = int
    RIGHT = int
    DOWN = int
    LEFT = int

    def __repr__(self) -> str:
        """Returns a string representation of the CardConnections."""
        return (
            f"CardConnections(UP={self.UP}, RIGHT={self.RIGHT}, DOWN={self.DOWN}, LEFT={self.LEFT})"
        )

    def __eq__(self, other: "CardConnections") -> bool:
        """Checks equality between two CardConnections instances."""
        if not isinstance(other, CardConnections):
            return False
        if self is other:
            return True
        return (
            self.UP == other.UP
            and self.RIGHT == other.RIGHT
            and self.DOWN == other.DOWN
            and self.LEFT == other.LEFT
        )

    def __hash__(self) -> int:
        """Returns the hash of the CardConnections instance."""
        return hash((self.UP, self.RIGHT, self.DOWN, self.LEFT))

    @classmethod
    def from_dict(cls, data: dict[str:int]) -> "CardConnections":
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

    @classmethod
    def from_dict(cls, name: str, connections_dict: dict[str:int]) -> "PathCard":
        """Creates a PathCard instance from a dictionary of connections."""
        connections = CardConnections.from_dict(connections_dict)
        return cls(name, connections)

    def flip(self) -> None:
        """Flips the card 180 degrees."""
        self._connections = CardConnections.from_dict(
            {
                "UP": self._connections.DOWN,
                "RIGHT": self._connections.LEFT,
                "DOWN": self._connections.UP,
                "LEFT": self._connections.RIGHT,
            }
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


class GoalCard(PathCard):
    """Card representing a goal that miners can achieve."""

    def __init__(self, name: str, connections: CardConnections) -> None:
        """Initializes a GoalCard with a name and its connections.
        A goal card is initially face down (not visible).
        Its connections are revealed when the card is revealed,
        meanwhile it is accessible from all sides.
        """
        self.__is_visible = False
        self.__real_name = name
        self.__real_connections = connections
        hidden_connections = CardConnections.from_dict(path_card_data["GOAL"]["connections"])
        super().__init__("GOAL", hidden_connections)

    def reveal(self) -> None:
        """Reveals the goal card, making its real connections visible."""
        self.__is_visible = True
        self._name = self.__real_name
        self._connections = self.__real_connections

    @property
    def is_visible(self) -> bool:
        """Returns whether the goal card is visible."""
        return self.__is_visible

    def read_real_name(self) -> str:
        """Returns the real name of the goal card."""
        return self.__real_name


def get_3_goal_cards() -> list[GoalCard]:
    """Returns a shuffled list of the 3 goal cards."""
    goal_names = ["ST-UL", "ST-UR", "END"]
    shuffle(goal_names)
    return [GoalCard(name, CardConnections.from_dict(path_card_data[name])) for name in goal_names]
