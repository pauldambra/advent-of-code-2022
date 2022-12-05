from pathlib import Path

from aoc_2022.day_one import calories


def test_one_item() -> None:
    assert calories("""
    1200""") == [1200]

def test_several_items() -> None:
    assert calories("""
1200
2400

1
2
3""") == [3600,6]

def test_part_one() -> None:
    puzzle_input_path = Path(__file__).parent / "./day_one_puzzle.input"
    with open(puzzle_input_path, "r", newline="\n") as f:
        assert max(calories(f.read())) == 66186

def test_part_two() -> None:
    puzzle_input_path = Path(__file__).parent / "./day_one_puzzle.input"
    with open(puzzle_input_path, "r", newline="\n") as f:
        top_three = sorted(calories(f.read()), reverse=True)[:3]
        assert top_three == [66186, 65638, 64980]
        assert sum(top_three) == 196804