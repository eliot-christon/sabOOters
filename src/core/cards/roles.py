"""This module contains role-related classes, functions, and data."""

from json import load
from pathlib import Path
from random import shuffle

roles = load(Path.open("src/core/cards/cards_data.json"))["roles"]


class Role:
    """Class representing a player role in the game."""

    NAME: str
    DESCRIPTION: str
    TEAM: str

    def __repr__(self) -> str:
        """Returns a string representation of the Role."""
        return self.NAME

    def __eq__(self, other: object) -> bool:
        """Checks equality based on NAME and TEAM attributes."""
        if not isinstance(other, Role):
            return False
        if other is self:
            return True
        return self.NAME == other.NAME and self.TEAM == other.TEAM

    def __hash__(self) -> int:
        """Returns a hash based on NAME and TEAM attributes."""
        return hash((self.NAME, self.TEAM))


def get_all_roles() -> list[Role]:
    """Returns a list of all available role names."""
    all_roles = list[Role]()
    for role_name, role_info in roles.items():
        for _ in range(role_info.get("number", 1)):
            all_roles.append(Role())
            all_roles[-1].NAME = role_name
            all_roles[-1].DESCRIPTION = role_info.get("description")
            all_roles[-1].TEAM = role_info.get("team")
    return all_roles


def get_random_roles(num_players: int) -> list[Role]:
    """Returns a list of random role names for the specified number of players.
    Args:
        num_players (int): The number of players in the game.
    Returns:
        list[Role]: A list of Role objects representing the roles assigned to players.
    """
    available_roles = get_all_roles()
    shuffle(available_roles)
    return available_roles[:num_players]
