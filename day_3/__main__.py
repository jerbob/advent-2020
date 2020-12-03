"""Submission for both parts of advent of code, day 3."""

import math
from itertools import cycle, islice

from aocd import submit, get_data


lines = get_data(day=3).split("\n")


def tree_exists(squares: str, index: int) -> bool:
    """Check if a tree exists in the provided index."""
    trees = cycle(square == "#" for square in squares)
    return next(islice(trees, index, index + 1))


def get_trees(width: int, height: int) -> int:
    """Given a slope, return the number of trees encountered."""
    return sum(
        not row % height and tree_exists(line, row // height * width)
        for row, line in enumerate(lines)
    )


trees = get_trees(3, 1)
submit(trees, part="a")

trees *= math.prod(
    get_trees(*slope)
    for slope in (
        (1, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
)
submit(trees, part="b")
