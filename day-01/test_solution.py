from pathlib import Path

from solution import parse_input, solve_part1, solve_part2


def test_example():
    example_path = Path(__file__).parent / "example.txt"
    raw = example_path.read_text()
    data = parse_input(raw)

    assert solve_part1(data) == 0  # TODO: replace with expected example answer for part 1
    assert solve_part2(data) == 0  # TODO: replace with expected example answer for part 2
