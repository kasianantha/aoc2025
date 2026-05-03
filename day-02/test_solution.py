from pathlib import Path
from solution import parse_input, solve_part1, solve_part2


def test_example():
    raw = (Path(__file__).parent / "example.txt").read_text()
    data = parse_input(raw)
    assert solve_part1(data) == 1227775554  # expected part 1
    # assert solve_part2(data) == ???        # fill in when known
