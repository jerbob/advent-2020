"""Submission for both parts of advent of code, day 1."""

from itertools import permutations

from aocd import submit, get_data


expenses = [int(expense) for expense in get_data(day=1).split("\n")]

expense_pairs = permutations(expenses, 2)
for first, second in expense_pairs:
    if first + second == 2020:
        submit(first * second, part="a")

expense_triples = permutations(expenses, 3)
for first, second, third in expense_triples:
    if first + second + third == 2020:
        submit(first * second * third, part="b")
