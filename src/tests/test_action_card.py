"""Tests for the ActionCard module."""

from src.core.cards.action_card import ActionCard

# %% Tests for ActionCard


def test_action_card_initialization() -> None:
    """Test that ActionCard cannot be instantiated directly."""
    try:
        ActionCard("TestActionCard")
        msg = "ActionCard should not be instantiated directly."
        raise AssertionError(msg)
    except TypeError:
        assert True
