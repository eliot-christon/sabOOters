"""Tests for the Player module."""

from src.core.cards.action_card import ActionCard
from src.core.cards.path_card import PathCard
from src.core.player import Player


def test_player_initialization() -> None:
    """Test the initialization of a Player instance."""
    card = PathCard.from_dict(
        name="Straight", connections_dict={"UP": 1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}
    )
    player = Player("Alice", "Red", [card], [])
    assert player.name == "Alice"
    assert player.role == "Red"
    assert len(player.hand) == 1
    assert len(player.bench) == 0
    assert player.hand[0] is card


def test_player_equality() -> None:
    """Test the equality comparison of Player instances."""
    card1 = PathCard.from_dict(
        name="Straight", connections_dict={"UP": 1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}
    )
    card2 = PathCard.from_dict(
        name="Curve", connections_dict={"UP": 1, "DOWN": 0, "LEFT": 1, "RIGHT": 0}
    )
    player1 = Player("Bob", "Blue", [card1], [card2])
    player2 = Player("Bob", "Blue", [card1], [card2])
    player3 = Player("Charlie", "Green", [card1], [])
    assert player1 == player2
    assert player1 != player3


def test_player_blocked_status() -> None:
    """Test the is_blocked method of the Player class."""

    def no_action() -> None:
        pass

    offensive_card = ActionCard("Block", no_action)
    offensive_card.make_offensive()
    defensive_card = ActionCard("Shield", no_action)
    defensive_card.make_defensive()

    player_with_offensive = Player("Dave", "Yellow", [], [offensive_card])
    player_with_defensive = Player("Eve", "Purple", [], [defensive_card])
    player_with_both = Player("Frank", "Orange", [], [offensive_card, defensive_card])
    player_with_none = Player("Grace", "Pink", [], [])

    assert player_with_offensive.is_blocked() is True
    assert player_with_defensive.is_blocked() is False
    assert player_with_both.is_blocked() is True
    assert player_with_none.is_blocked() is False


def test_player_draw_card() -> None:
    """Test drawing a card to the player's hand."""
    card1 = PathCard.from_dict(
        name="Straight", connections_dict={"UP": 1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}
    )
    card2 = PathCard.from_dict(
        name="Curve", connections_dict={"UP": 1, "DOWN": 0, "LEFT": 1, "RIGHT": 0}
    )
    player = Player("Hannah", "Cyan", [card1], [])
    assert len(player.hand) == 1
    player.draw(card2)
    assert len(player.hand) == 2
    assert player.hand[1] is card2


def test_player_discard_card() -> None:
    """Test discarding a card from the player's hand."""
    card1 = PathCard.from_dict(
        name="Straight", connections_dict={"UP": 1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}
    )
    card2 = PathCard.from_dict(
        name="Curve", connections_dict={"UP": 1, "DOWN": 0, "LEFT": 1, "RIGHT": 0}
    )
    player = Player("Ivy", "Magenta", [card1, card2], [])
    assert len(player.hand) == 2
    success, _ = player.discard(card1)
    assert success
    assert len(player.hand) == 1
    assert player.hand[0] is card2
    success, _ = player.discard(card1)
    assert not success
    assert len(player.hand) == 1
