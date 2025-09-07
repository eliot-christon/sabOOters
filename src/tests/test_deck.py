"""Tests for the build_deck function in build_deck.py."""

from src.core.cards.action_card import ActionCard
from src.core.cards.build_deck import build_deck
from src.core.cards.card import Card
from src.core.cards.path_card import PathCard


def test_build_deck() -> None:
    """Test that the deck is built correctly with the expected number of cards."""
    deck = build_deck()

    # Check that the deck is a list
    assert isinstance(deck, list), "Deck should be a list"

    # Check that all elements in the deck are instances of Card
    assert all(isinstance(card, Card) for card in deck), (
        "All elements in the deck should be instances of Card"
    )

    # Check for presence of PathCards and ActionCards
    path_cards = [card for card in deck if isinstance(card, PathCard)]
    action_cards = [card for card in deck if isinstance(card, ActionCard)]

    assert len(path_cards) > 0, "There should be at least one PathCard in the deck"
    assert len(action_cards) > 0, "There should be at least one ActionCard in the deck"

    # Check that the deck is shuffled (not in original order)
    original_deck = build_deck()  # Build another deck to compare order
    assert deck != original_deck, "Deck should be shuffled and not in original order"
