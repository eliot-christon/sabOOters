"""Tests for the Card module."""

from src.core.cards.card import Card


def test_card_initialization() -> None:
    """Test the initialization of a Card instance."""
    card = Card("TestCard")
    assert card.name == "TestCard"


def test_card_equality() -> None:
    """Test the equality comparison of Card instances."""
    card1 = Card("TestCard")
    card2 = Card("TestCard")
    card3 = Card("AnotherCard")
    assert card1 == card2
    assert card1 != card3
