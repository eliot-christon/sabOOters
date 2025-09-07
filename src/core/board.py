"""
This module contains board-related classes and functions.
"""

from __future__ import annotations

from src.core.cards.path_card import PathCard, StartCard, get_3_goal_cards


class Board:
    """
    Represents the game board, which holds path cards played by players.
    """

    def __init__(self) -> None:
        """Initializes the board with a grid and places the start and goal cards."""
        self.__rows = 5
        self.__columns = 7
        self.__start_position = (2, 0)
        goal_cards = get_3_goal_cards()
        self.__grid = list[list[PathCard | None]]()
        self.__grid = [[None for _ in range(self.__columns)] for _ in range(self.__rows)]
        self.__grid[self.__start_position[0]][self.__start_position[1]] = StartCard()
        self.__grid[0][6] = goal_cards[0]
        self.__grid[2][6] = goal_cards[1]
        self.__grid[4][6] = goal_cards[2]

    @property
    def rows(self) -> int:
        """Returns the number of rows in the board."""
        return self.__rows

    @property
    def columns(self) -> int:
        """Returns the number of columns in the board."""
        return self.__columns

    @property
    def start_position(self) -> tuple[int, int]:
        """Returns the starting position on the board."""
        return self.__start_position

    def expand(self, direction: str) -> None:
        """Expands the board in the specified direction by adding a new row or column."""
        if direction == "UP":
            self.__grid.insert(0, [None for _ in range(self.__columns)])
            self.__rows += 1
            self.__start_position = (self.__start_position[0] + 1, self.__start_position[1])
        elif direction == "DOWN":
            self.__grid.append([None for _ in range(self.__columns)])
            self.__rows += 1
            self.__start_position = (self.__start_position[0], self.__start_position[1])
        elif direction == "LEFT":
            for row in self.__grid:
                row.insert(0, None)
            self.__columns += 1
            self.__start_position = (self.__start_position[0], self.__start_position[1] + 1)
        elif direction == "RIGHT":
            for row in self.__grid:
                row.append(None)
            self.__columns += 1
        else:
            msg = "Invalid direction. Use 'UP', 'DOWN', 'LEFT', or 'RIGHT'."
            raise ValueError(msg)

    def place_card(self, row: int, column: int, card: PathCard) -> tuple[bool, str]:
        """Places a path card on the board at the specified position if valid.

        Args:
            row (int): The row index where the card is to be placed.
            column (int): The column index where the card is to be placed.
            card (PathCard): The path card to be placed.

        Returns:
            tuple[bool, str]: A tuple containing a boolean indicating success and a message.
        """
        # expand the board if the position is out of current bounds
        if not (0 <= row < self.__rows and 0 <= column < self.__columns):
            if row == -1:
                self.expand("UP")
                row = 0
            elif row == self.__rows:
                self.expand("DOWN")
            if column == -1:
                self.expand("LEFT")
                column = 0
            elif column == self.__columns:
                self.expand("RIGHT")

        if self.__grid[row][column] is not None:
            return False, "Position already occupied."

        result, message = self.check_adjacent_connections(row, column, card)
        if not result:
            return False, message

        self.__grid[row][column] = card
        return True, "Card placed successfully."

    def check_adjacent_connections(self, row: int, column: int, card: PathCard) -> tuple[bool, str]:
        """Checks if the placed card connects properly with adjacent cards.

        Args:
            row (int): The row index where the card is placed.
            column (int): The column index where the card is placed.
            card (PathCard): The path card to be checked.

        Returns:
            tuple[bool, str]: A tuple containing a boolean
                              indicating if connections are valid and a message.
        """
        adjacent_positions = {
            "UP": (row - 1, column),
            "DOWN": (row + 1, column),
            "LEFT": (row, column - 1),
            "RIGHT": (row, column + 1),
        }

        # Map direction to (card side, adjacent card opposite side, error message)
        connection_map = {
            "UP": ("UP", "DOWN", "Connection mismatch with UP card."),
            "DOWN": ("DOWN", "UP", "Connection mismatch with DOWN card."),
            "LEFT": ("LEFT", "RIGHT", "Connection mismatch with LEFT card."),
            "RIGHT": ("RIGHT", "LEFT", "Connection mismatch with RIGHT card."),
        }

        count_adjacent = 0

        for direction, (adj_row, adj_col) in adjacent_positions.items():
            if 0 <= adj_row < self.__rows and 0 <= adj_col < self.__columns:
                adjacent_card = self.__grid[adj_row][adj_col]
                if adjacent_card is not None:
                    count_adjacent += 1
                    card_side, adj_side, error_msg = connection_map[direction]
                    if (getattr(card.connections, card_side) != 0) != (
                        getattr(adjacent_card.connections, adj_side) != 0
                    ):
                        return False, error_msg

        if count_adjacent == 0:
            return False, "Card must connect to at least one adjacent card."

        return True, "All connections are valid."

    def get_card(self, row: int, column: int) -> PathCard | None:
        """Returns the card at the specified position, or None if empty."""
        if 0 <= row < self.__rows and 0 <= column < self.__columns:
            return self.__grid[row][column]
        return None
