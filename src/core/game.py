"""
This module contains the Game class, which manages the overall game state and progression.
The game is managed through a state machine that transitions between different phases of the game.
"""

from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.player import Player
    from src.core.round import Round


class GameState(Enum):
    """Enumeration of possible game states."""

    NAMING_PLAYERS = auto()
    ROUND_BEGIN = auto()
    PLAYER_TURN_BEGIN = auto()
    CHOSE_ACTION = auto()
    CHOSE_CARDS = auto()
    CHOSE_PLAYER = auto()
    PLAYER_TURN_END = auto()
    ROUND_END = auto()
    GAME_END = auto()


"""
Transitions between states:
NAMING_PLAYERS -> ROUND_BEGIN if enough players have joined and names are correctly set
ROUND_BEGIN -> PLAYER_TURN_BEGIN after initializing the round
PLAYER_TURN_BEGIN -> CHOSE_ACTION
CHOSE_ACTION -> CHOSE_CARDS if valid action chosen
CHOSE_CARDS -> CHOSE_PLAYER if action requires target player
CHOSE_CARDS -> PLAYER_TURN_END if valid card selection
CHOSE_PLAYER -> PLAYER_TURN_END after selecting target player
PLAYER_TURN_END -> ROUND_END if round-ending condition met
PLAYER_TURN_END -> PLAYER_TURN_BEGIN for next player otherwise
ROUND_END -> GAME_END if game-ending condition met
ROUND_END -> ROUND_BEGIN for next round otherwise

Possible transition inputs:
- Player names
- Chosen action
- Selected cards
- Target player

Between each state, the game checks for valid transitions and updates the game state accordingly.
Each next step will be triggered by the api call from the client.
Each state will have its own handler function to manage the specific logic and transitions.
"""


class Game:
    """
    Represents the overall game, managing players, rounds, and game state.
    """

    def __init__(self) -> None:
        """
        Initializes a Game with an empty list of players and sets the initial game state.
        """
        self.__players: list[Player] = []
        self.__current_round: Round | None = None
        self.__state: GameState = GameState.NAMING_PLAYERS

    @property
    def players(self) -> list[Player]:
        """Returns the list of players in the game."""
        return self.__players

    @property
    def current_round(self) -> Round | None:
        """Returns the current round of the game."""
        return self.__current_round

    @property
    def state(self) -> GameState:
        """Returns the current state of the game."""
        return self.__state
