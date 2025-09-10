"""
This module contains the Round class, which manages the state and progression of a game round.
"""

from src.core.board import Board
from src.core.cards.build_deck import build_deck
from src.core.cards.roles import get_random_roles
from src.core.player import Player


class Round:
    """
    Represents a game round, managing the round number and turn order.
    """

    def __init__(self, players: list[Player]) -> None:
        """
        Initializes a Round with a list of players and sets the round number to 1.
        """
        self.__players = players
        self.__current_turn_index = 0
        self.__board = Board()
        self.__deck = build_deck()

        self.__assign_player_roles()
        self.__deal_hands()

    @property
    def current_player(self) -> Player:
        """Returns the player whose turn it is currently."""
        return self.__players[self.__current_turn_index % len(self.__players)]

    def __deal_hands(self, hand_size: int = 6) -> None:
        """Deals a specified number of cards to each player at the start of the round.
        Args:
            hand_size (int): The number of cards to deal to each player.
        """
        for player in self.__players:
            player.empty_hand()
            for _ in range(hand_size):
                player.draw(self.__deck)

    def __assign_player_roles(self) -> None:
        """Assigns roles to players at the start of the round."""
        random_roles = get_random_roles(len(self.__players))
        for i, player in enumerate(self.__players):
            player.role = random_roles[i]
