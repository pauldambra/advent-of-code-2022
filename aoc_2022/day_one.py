from typing import List


def calories(inventory:str) -> List[int]:
    calories_by_elves = []

    current = 0
    for line in [l.strip() for l in inventory.splitlines()]:
        if not line:
            if current > 0:
                calories_by_elves.append(current)
                current = 0
        else:
            current += int(line)

    calories_by_elves.append(current)

    return calories_by_elves
