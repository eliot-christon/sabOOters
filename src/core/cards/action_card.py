"""This module defines the base class for action cards in the game."""

from abc import ABC, abstractmethod

from src.core.cards.card import Card


class ActionCard(Card, ABC):
    """Card representing an action that can be performed by players.
    These cards can be played during a player's turn."""

    @abstractmethod
    def perform_action(self, round_number: int) -> None:
        """Performs the action associated with the card.

        Args:
            round_number (int): The current round number in the game.
        """
