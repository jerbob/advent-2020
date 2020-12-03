"""Submission for both parts of advent of code, day 3."""

import math

from aocd import submit, get_data

from day_3 import Row


lines = get_data(day=3).split("\n")


def get_trees(width: int, height: int) -> int:
    """Given a slope, return the number of trees encountered."""
    return sum(
        not row % height and Row(string=line).is_tree(row * width)
        for row, line in enumerate(lines)
    )


trees = get_trees(3, 1)
print(trees)

trees *= math.prod(
    get_trees(*slope)
    for slope in (
        (1, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
)
print(trees)
