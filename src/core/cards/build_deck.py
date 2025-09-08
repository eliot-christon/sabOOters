"""
This file contains the function to build the deck of cards for the game.
"""

from json import load
from pathlib import Path
from random import shuffle

from src.core.cards.action_card import ActionCard
from src.core.cards.card import Card
from src.core.cards.path_card import PathCard

card_data = load(Path.open("src/core/cards/cards_data.json"))


def build_deck(cards_to_remove: int = 10) -> list[Card]:
    """Builds and returns a shuffled deck of cards for the game.
    Args:
        cards_to_remove (int): The number of random cards to remove from the deck.
    Returns:
        list[Card]: A shuffled list of Card objects representing the deck.
    """
    deck: list[Card] = []

    # Create PathCards
    for card_name, card_info in card_data["path_card"].items():
        number_of_copies = card_info.get("number", 1)
        for _ in range(number_of_copies):
            path_card = PathCard.from_dict(
                name=card_name, connections_dict=card_info["connections"]
            )
            deck.append(path_card)

    def no_action() -> None:
        """A placeholder function for ActionCard actions that do nothing."""

    # Create ActionCards
    for card_name, number_of_copies in card_data["action_card"].items():
        for _ in range(number_of_copies):
            action_card = ActionCard(name=card_name, action=no_action)
            deck.append(action_card)

    shuffle(deck)
    return deck[cards_to_remove:]  # Remove a number of random cards to adjust deck size
