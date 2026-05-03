from pathlib import Path
from typing import List


def parse_input(raw: str) -> List[str]:
    return raw.strip().splitlines()


def solve_part1(data: List[str]) -> int:
    # TODO: implement part 1
    return 0


def solve_part2(data: List[str]) -> int:
    # TODO: implement part 2
    return 0


if __name__ == "__main__":
    raw = (Path(__file__).parent / "input.txt").read_text()
    data = parse_input(raw)
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))
