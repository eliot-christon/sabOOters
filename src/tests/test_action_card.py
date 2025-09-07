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


def test_action_card_properties() -> None:
    """Test that ActionCard properties are set correctly."""

    def sample_action() -> None:
        """A sample action function for testing."""

    action_card = ActionCard(name="SampleActionCard", action=sample_action)
    assert action_card.name == "SampleActionCard", "ActionCard name property is incorrect."
