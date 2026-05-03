#!/usr/bin/env python
"""Usage: python setup_day.py <day>"""
import sys
from pathlib import Path
from aocd.models import Puzzle

SOLUTION_TEMPLATE = '''\
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
'''

TEST_TEMPLATE = '''\
from pathlib import Path
from solution import parse_input, solve_part1, solve_part2


def test_example():
    raw = (Path(__file__).parent / "example.txt").read_text()
    data = parse_input(raw)
    assert solve_part1(data) == {answer_a}  # expected part 1
    # assert solve_part2(data) == ???        # fill in when known
'''


def setup(day: int, year: int = 2025) -> None:
    folder = Path(f"day-{day:02d}")
    folder.mkdir(exist_ok=True)

    puzzle = Puzzle(year=year, day=day)
    print(f"Puzzle: {puzzle.title}")

    input_path = folder / "input.txt"
    input_path.write_text(puzzle.input_data)
    print(f"  input.txt written ({len(puzzle.input_data)} chars)")

    examples = puzzle.examples
    example_path = folder / "example.txt"
    if examples:
        example_path.write_text(examples[0].input_data)
        answer_a = examples[0].answer_a
        print(f"  example.txt written — part 1 answer: {answer_a}")
    else:
        example_path.write_text("")
        answer_a = "???"
        print("  example.txt written (empty — none found automatically)")

    solution_path = folder / "solution.py"
    if not solution_path.exists():
        solution_path.write_text(SOLUTION_TEMPLATE)
        print("  solution.py created")
    else:
        print("  solution.py already exists, skipping")

    test_path = folder / "test_solution.py"
    if not test_path.exists():
        test_path.write_text(TEST_TEMPLATE.format(answer_a=answer_a))
        print("  test_solution.py created")
    else:
        print("  test_solution.py already exists, skipping")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python setup_day.py <day>")
        sys.exit(1)
    setup(int(sys.argv[1]))
