from dataclasses import InitVar, dataclass
from itertools import cycle, repeat, islice
from typing import Iterable


@dataclass
class Row:
    string: InitVar[str]
    squares: Iterable[bool] = repeat(True)

    def __post_init__(self, string: str):
        self.squares = cycle(square == "#" for square in string)

    def get_square(self, index: int) -> bool:
        return next(islice(self.squares, index, None))
