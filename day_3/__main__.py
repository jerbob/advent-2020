"""Submission for both parts of advent of code, day 3."""

from aocd import submit, get_data

from day_3 import Row


lines = get_data(day=3).split("\n")

trees: int = sum(
    Row(string=line).get_square(index * 3)
    for index, line in enumerate(lines)
)

submit(trees, part="a")
