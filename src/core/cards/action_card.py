"""This module defines the base class for action cards in the game."""

from src.core.cards.card import Card


class ActionCard(Card):
    """Card representing an action that can be performed by players.
    These cards can be played during a player's turn."""

    def __init__(self, name: str, action: callable) -> None:
        """Initializes an ActionCard with a name and its associated action."""
        self._action = action
        self._offensive = False
        self.__defensive = False
        super().__init__(name)

    @property
    def is_offensive(self) -> bool:
        """Returns True if the action card is offensive, False otherwise."""
        return self.__offensive

    @property
    def is_defensive(self) -> bool:
        """Returns True if the action card is defensive, False otherwise."""
        return self.__defensive

    def make_defensive(self) -> None:
        """Sets the action card as defensive."""
        self.__defensive = True
        self.__offensive = False

    def make_offensive(self) -> None:
        """Sets the action card as offensive."""
        self.__offensive = True
        self.__defensive = False

    def make_neutral(self) -> None:
        """Sets the action card as neutral (neither offensive nor defensive)."""
        self.__defensive = False
        self.__offensive = False

    def perform_action(self, *args: any, **kwargs: any) -> None:
        """Performs the action associated with the card."""
        self._action(*args, **kwargs)
