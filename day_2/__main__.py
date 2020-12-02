"""Submission for both parts of advent of code, day 2."""

import re

from aocd import submit, get_data


PASSWORD_ENTRY = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

count: int = 0
for entry in get_data(day=2).split("\n"):
    lower, upper, letter, password = PASSWORD_ENTRY.match(entry).groups()
    count += int(lower) <= password.count(letter) <= int(upper)

submit(count, day=2, part="a")


count = 0
for entry in get_data(day=2).split("\n"):
    lower, upper, letter, password = PASSWORD_ENTRY.match(entry).groups()
    lower, upper = int(lower) - 1, int(upper) - 1
    count += (password[lower] == letter) ^ (password[upper] == letter)

submit(count, day=2, part="b")
