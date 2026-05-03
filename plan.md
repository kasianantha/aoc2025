# Advent of Code 2025 Framework

## Purpose
This repository is a workspace for solving Advent of Code 2025 puzzles. The goal is to give a simple, restart-safe structure so your dad can tackle each day’s problem in order and keep progress tracked.

## How this repo is organized
- `plan.md` — high-level workflow and status tracking
- `day-XX/` — one folder per AoC day (e.g. `day-01`, `day-02`)
- `day-XX/input.txt` — puzzle input for that day
- `day-XX/example.txt` — optional sample input from the prompt
- `day-XX/solution.py` — Python solution code for that day
- `day-XX/test_solution.py` — simple tests for sample output
- `requirements.txt` — Python dependencies, if any

## Daily workflow
1. Create a new folder for the day: `day-XX`
2. Save the real puzzle input in `day-XX/input.txt`
3. Add sample input to `day-XX/example.txt` if the prompt includes one
4. Create `day-XX/solution.py` and implement:
   - `parse_input()`
   - `solve_part1()`
   - `solve_part2()`
   - a `__main__` block to print both answers
5. Create `day-XX/test_solution.py` to verify the sample input and expected output
6. Run the tests and confirm the sample cases pass
7. Run `day-XX/solution.py` on the real input
8. Record the real answers in the day folder or a progress note
9. Update `plan.md` with the current day and status
10. Repeat for the next day

## Recommended content for each day folder
- `solution.py` should include:
  - a `parse_input()` function
  - a `solve_part1()` function
  - a `solve_part2()` function
  - a main guard that prints both answers
- `test_solution.py` should:
  - load the sample input
  - assert the expected results for part 1 and part 2

## Example file structure
- `day-01/`
  - `input.txt`
  - `example.txt`
  - `solution.py`
  - `test_solution.py`
- `day-02/`
  - `input.txt`
  - `solution.py`
  - `test_solution.py`

## Progress tracking
Update this file with:
- current day being solved
- status for each day: `not started`, `in progress`, `done`
- notes for puzzle details, approach, or edge cases

### Current status
- Day 01: in progress
- Day 02: not started
- Day 03: not started

## Notes for restart safety
- Reopen `plan.md` after restarting VS Code
- Use the day folders as checkpoints
- Add brief comments about what still needs work

## Next actions
- Create the first day folder and add the puzzle input
- Add a starter `solution.py` template for the first day
- Add a `README` or `TODO` later if desired
