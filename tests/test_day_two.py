from pathlib import Path

from aoc_2022.day_two import game, strategy_part_one, strategy_part_two


def test_example() -> None:
    assert (
        game(
            """
    A Y
    B X
    C Z
    """,
            strategy_part_one,
        )
        == 15
    )


def test_part_one() -> None:
    puzzle_input_path = Path(__file__).parent / "./day_two_puzzle.input"
    with open(puzzle_input_path, "r", newline="\n") as f:
        assert game(f.read(), strategy_part_one) == 13446


def test_example_version_two() -> None:
    assert (
        game(
            """
    A Y
    B X
    C Z
    """,
            strategy_part_two,
        )
        == 12
    )


def test_part_two() -> None:
    puzzle_input_path = Path(__file__).parent / "./day_two_puzzle.input"
    with open(puzzle_input_path, "r", newline="\n") as f:
        assert game(f.read(), strategy_part_two) == 13509
