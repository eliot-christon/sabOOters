"""Tests for the Round module."""

from src.core.cards.path_card import PathCard
from src.core.player import Player
from src.core.round import Round

card = PathCard.from_dict(
    name="Straight", connections_dict={"UP": 1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}
)
players = [
    Player("Alice", "Red", [card], []),
    Player("Bob", "Blue", [card], []),
    Player("Charlie", "Green", [card], []),
]


def test_round_initialization() -> None:
    """Test the initialization of a Round instance."""
    game_round = Round(players)
    assert game_round.current_player == players[0]
    assert len(players[0].hand) == 6
    assert len(players[1].hand) == 6
    assert len(players[2].hand) == 6
