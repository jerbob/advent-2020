from dataclasses import InitVar, dataclass
from itertools import cycle, repeat, islice
from typing import Iterable


@dataclass
class Row:
    string: InitVar[str]
    squares: Iterable[bool] = repeat(False)

    def __post_init__(self, string: str):
        self.squares = cycle(square == "#" for square in string)

    def is_tree(self, index: int) -> bool:
        return next(islice(self.squares, index, None))
