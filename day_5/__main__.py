"""Submission for both parts of advent of code, day 5."""

from itertools import count

from aocd import submit, get_data


lines = get_data().strip().split("\n")


def get_axis(string: str, upper: int, lower: int = 0) -> int:
    for letter in string:
        space = (upper - lower) // 2 + 1
        upper -= (letter in ("F", "L")) * space
        lower += (letter in ("B", "R")) * space
    return upper


def get_seat_id(string: str) -> int:
    row, column = string[:7], string[7:]
    return get_axis(row, 127) * 8 + get_axis(column, 7)


highest, *seats = sorted(map(get_seat_id, lines), reverse=True)
submit(highest, part="a")

for seat, target in zip(seats, count(highest - 1, -1)):
    if seat != target:
        submit(target, part="b")
        break
