# sabOOters

## Overview

sabOOters is a Python implementation of the classic Saboteur card game. This project revisits my first complete Python project, allowing me to measure my progress and improvements in software design and coding practices.

## Features

- Play the Saboteur card game in the console
- Modular code structure for cards, players, board, and game logic
- Extendable for custom rules and expansions
- Includes unit tests for core components

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eliot-christon/sabOOters.git
   cd sabOOters
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies using uv:
   ```bash
   uv pip install -r pyproject.toml
   ```

## Usage

To start the game, run the main script:

```bash
python main.py
```

## Project Structure

```
src/                   # Refactored core modules
  core/                # Board, game, player, round logic
  cards/               # Card definitions and deck builder
  tests/               # Unit tests
```

## Running Tests

To run unit tests:

```bash
pytest
```

## Credits

- Developed by Eliot Christon
- Inspired by the Saboteur card game

## License

This project is licensed under the Apache 2.0 License. See `LICENSE` for details.
