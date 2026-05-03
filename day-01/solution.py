import os
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


def fetch_input(day: int = 1, year: int = 2025) -> str:
    """Download the Advent of Code input for the given day/year."""
    try:
        from aocd import get_data
    except ImportError as exc:
        raise RuntimeError("The aocd package is required to download puzzle input.") from exc

    return get_data(day=day, year=year)


def ensure_input(input_path: Path, day: int = 1, year: int = 2025) -> str:
    """Return input text, downloading it if the local file is missing or empty."""
    if not input_path.exists() or not input_path.read_text().strip():
        raw = fetch_input(day=day, year=year)
        input_path.write_text(raw)
    return input_path.read_text()


def main() -> None:
    input_path = Path(__file__).parent / "input.txt"
    raw = ensure_input(input_path)
    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))


if __name__ == "__main__":
    main()
