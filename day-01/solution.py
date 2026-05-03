from pathlib import Path
from typing import List


def parse_input(raw: str) -> List[str]:
    """Parse the puzzle input into a useful structure."""
    return raw.strip().splitlines()


def solve_part1(data: List[str]) -> int:
    """Solve part 1 of day 1."""
    # TODO: implement part 1 logic
    return 0


def solve_part2(data: List[str]) -> int:
    """Solve part 2 of day 1."""
    # TODO: implement part 2 logic
    return 0


def main() -> None:
    input_path = Path(__file__).parent / "input.txt"
    raw = input_path.read_text()
    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))


if __name__ == "__main__":
    main()
