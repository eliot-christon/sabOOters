"""Tests for the PathCard module."""

from json import load
from pathlib import Path

from src.core.cards.path_card import CardConnections, GoalCard, PathCard, StartCard

path_card_data = load(Path.open("src/core/cards/cards_data.json"))["path_card"]


# %% Tests for PathCard and CardConnections


def test_path_card_connections() -> None:
    """Test the initialization of CardConnections."""
    connections = CardConnections.from_dict({"UP": 1, "RIGHT": 0, "DOWN": 1, "LEFT": 0})
    assert connections.UP == 1
    assert connections.RIGHT == 0
    assert connections.DOWN == 1
    assert connections.LEFT == 0


def test_path_card_initialization() -> None:
    """Test the initialization of a PathCard instance."""
    connections = CardConnections.from_dict({"UP": 1, "RIGHT": 0, "DOWN": 1, "LEFT": 0})
    path_card = PathCard("TestPathCard", connections)
    assert path_card.name == "TestPathCard"
    assert path_card.connections == connections


def test_path_card_flip() -> None:
    """Test the flip method of a PathCard instance."""
    connections = CardConnections.from_dict({"UP": 1, "RIGHT": 0, "DOWN": 1, "LEFT": 0})
    path_card = PathCard("TestPathCard", connections)
    path_card.flip()
    assert path_card.connections.UP == 1
    assert path_card.connections.RIGHT == 0
    assert path_card.connections.DOWN == 1
    assert path_card.connections.LEFT == 0


# %% Tests for StartCard


def test_start_card_initialization() -> None:
    """Test the initialization of a StartCard instance."""
    start_card = StartCard()
    assert start_card.name == "START"
    assert isinstance(start_card.connections, CardConnections)


def test_start_card_flip() -> None:
    """Test the flip method of a StartCard instance."""
    start_card = StartCard()
    original_connections = start_card.connections
    start_card.flip()
    assert start_card.connections.UP == original_connections.DOWN
    assert start_card.connections.RIGHT == original_connections.LEFT
    assert start_card.connections.DOWN == original_connections.UP
    assert start_card.connections.LEFT == original_connections.RIGHT


# %% Tests for GoalCard


def test_goal_card_initialization() -> None:
    """Test the initialization of a GoalCard instance."""
    goal_card = GoalCard(
        name="TestGoalCard",
        connections=CardConnections.from_dict({"UP": 1, "RIGHT": 1, "DOWN": 0, "LEFT": 0}),
    )
    assert isinstance(goal_card.connections, CardConnections)


def test_goal_card_reveal() -> None:
    """Test the reveal method of a GoalCard instance."""
    test_connections = CardConnections.from_dict({"UP": 0, "RIGHT": 0, "DOWN": 1, "LEFT": 1})
    goal_card = GoalCard(name="TestGoalCard", connections=test_connections)
    assert goal_card.connections == CardConnections.from_dict(path_card_data["GOAL"]["connections"])
    assert goal_card.name == "GOAL"
    assert goal_card.read_real_name() == "TestGoalCard"
    goal_card.reveal()
    assert goal_card.connections == test_connections
    assert goal_card.name == "TestGoalCard"
    assert goal_card.read_real_name() == "TestGoalCard"
