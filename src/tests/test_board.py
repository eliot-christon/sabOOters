"""Tests for the Board module."""

from pytest import raises

from src.core.board import Board
from src.core.cards.path_card import PathCard


def test_board_initialization() -> None:
    """Test the initialization of a Board instance."""
    board = Board()
    assert board.rows == 5
    assert board.columns == 7


def test_board_expand() -> None:
    """Test the expand method of a Board instance."""
    board = Board()
    original_rows = board.rows
    original_columns = board.columns

    board.expand("UP")
    assert board.rows == original_rows + 1
    assert board.columns == original_columns
    assert board.start_position == (3, 0)

    board.expand("DOWN")
    assert board.rows == original_rows + 2
    assert board.columns == original_columns
    assert board.start_position == (3, 0)

    board.expand("LEFT")
    assert board.rows == original_rows + 2
    assert board.columns == original_columns + 1
    assert board.start_position == (3, 1)

    board.expand("RIGHT")
    assert board.rows == original_rows + 2
    assert board.columns == original_columns + 2
    assert board.start_position == (3, 1)


def test_board_invalid_expand() -> None:
    """Test the expand method with an invalid direction."""
    board = Board()
    with raises(ValueError):
        board.expand("INVALID")


def test_board_place_card() -> None:
    """Test placing a PathCard on the Board."""
    board = Board()
    path_card = PathCard.from_dict("TestPathCard", {"UP": 0, "RIGHT": 0, "DOWN": 0, "LEFT": 1})
    row, col = 2, 1
    result, _ = board.place_card(row, col, path_card)
    assert result is True
    assert board.get_card(row, col) == path_card

    path_card_invalid = PathCard.from_dict(
        "InvalidPathCard", {"UP": -1, "RIGHT": 0, "DOWN": 0, "LEFT": 0}
    )
    result, _ = board.place_card(row, col, path_card_invalid)
    assert result is False

    result, _ = board.place_card(0, 0, path_card_invalid)
    assert result is False

    result, _ = board.place_card(2, 0, path_card_invalid)
    assert result is False

    result, _ = board.place_card(3, 0, path_card_invalid)
    assert result is True
