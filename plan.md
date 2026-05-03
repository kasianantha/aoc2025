# Advent of Code 2025

## Repo layout
- `plan.md` — this file; workflow reference and progress tracker
- `setup_day.py` — scaffold script (see below)
- `day-XX/input.txt` — real puzzle input (downloaded via aocd)
- `day-XX/example.txt` — example input (downloaded via aocd)
- `day-XX/solution.py` — solution with `parse_input`, `solve_part1`, `solve_part2`
- `day-XX/test_solution.py` — pytest tests against the example

## Starting a new day

```bash
python setup_day.py <N>
```

This creates `day-0N/` and downloads `input.txt` and `example.txt` via the
`aocd` library (requires an AoC session cookie — see aocd docs if not set up).
It also drops in a `solution.py` template and a `test_solution.py` pre-filled
with the Part 1 example answer where aocd can find it. Safe to re-run — existing
files are never overwritten.

## Daily workflow
1. Run `python setup_day.py <N>`
2. Read the puzzle on adventofcode.com
3. Implement `solve_part1()` in `day-0N/solution.py`
4. Run `pytest day-0N/` — confirm the example passes
5. Run `python day-0N/solution.py` — get the real answer
6. Implement `solve_part2()` and repeat steps 4–5
7. Update the progress table below

## Progress

| Day | Puzzle | Part 1 | Part 2 |
|-----|--------|--------|--------|
| 01  | Secret Entrance | in progress | not started |
| 02  | Gift Shop | not started | not started |
