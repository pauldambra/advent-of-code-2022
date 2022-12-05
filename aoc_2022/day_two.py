from typing import List, Callable, Tuple


def score_for_selection(selection: str) -> int:
    if selection == "X" or selection == "A":
        return 1
    elif selection == "Y" or selection == "B":
        return 2
    elif selection == "Z" or selection == "C":
        return 3
    else:
        raise ValueError("Invalid selection")


class RockPapersScissors:
    def __init__(self, choose_your_move: Callable[[str, str], Tuple[str, str]]):
        self.choose_your_move = choose_your_move

    def play_game(self, turns: List[List[str]]) -> int:
        rounds = []
        for moves in turns:
            them = moves[0]
            strategy = moves[1]

            them, you = self.choose_your_move(them, strategy)

            round_score = self._score_round(them, you)
            rounds.append(round_score)

        return sum(rounds)

    @staticmethod
    def _score_round(them: str, you: str) -> int:
        selection_score = score_for_selection(you)

        if you == them:
            outcome_score = 3
        elif you == "A" and them == "C":
            outcome_score = 6
        elif you == "C" and them == "B":
            outcome_score = 6
        elif you == "B" and them == "A":
            outcome_score = 6
        else:
            outcome_score = 0

        return selection_score + outcome_score


def game(strategy_guide: str, strategy: Callable[[str, str], Tuple[str, str]]) -> int:
    """
    Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

    Rock > Scissors > Paper > Rock

    A for Rock, B for Paper, and C for Scissors
    X for Rock, Y for Paper, and Z for Scissors

    X > C
    Z > B
    Y > A

    The score for a single round is the score for the shape you selected
    (1 for Rock, 2 for Paper, and 3 for Scissors)

    plus the score for the outcome of the round
    (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    turns = []
    for line in [l.strip() for l in strategy_guide.splitlines() if l.strip()]:
        moves = line.split(" ")
        turns.append([moves[0], moves[1]])

    return RockPapersScissors(strategy).play_game(turns)


def strategy_part_one(them: str, strategy: str) -> (str, str):
    if strategy == "X":
        you = "A"
    elif strategy == "Y":
        you = "B"
    elif strategy == "Z":
        you = "C"
    else:
        raise ValueError("Invalid strategy")
    return them, you


def strategy_part_two(them: str, strategy: str) -> (str, str):
    if strategy == "Y":
        you = them
    elif strategy == "Z":
        if them == "A":
            you = "B"
        elif them == "B":
            you = "C"
        elif them == "C":
            you = "A"
        else:
            raise ValueError("Invalid strategy")
    elif strategy == "X":
        if them == "A":
            you = "C"
        elif them == "B":
            you = "A"
        elif them == "C":
            you = "B"
        else:
            raise ValueError("Invalid strategy")
    else:
        raise ValueError("Invalid strategy")

    return them, you
