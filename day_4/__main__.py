"""Submission for both parts of advent of code, day 4."""

import re
from contextlib import suppress
from typing import Optional

from aocd import get_data, submit
from pydantic import BaseModel, ValidationError, conint, constr, validator

# Get rid of newlines that aren't preceded by another
lines = re.sub(r"(?<=[^\n])\n", " ", get_data()).split("\n")

MEASUREMENT = re.compile(r"(\d+)(in|cm)")


class Passport(BaseModel):
    byr: conint(ge=1920, le=2002)
    iyr: conint(ge=2010, le=2020)
    eyr: conint(ge=2020, le=2030)
    hgt: constr(regex=MEASUREMENT.pattern)
    hcl: constr(regex=r"#[0-9a-f]{6}")
    ecl: constr(regex=r"amb|blu|brn|gry|grn|hzl|oth")
    pid: constr(regex=r"^[0-9]{9}$")
    cid: Optional[str]

    @validator("hgt")
    def validate_height(cls, value: str):
        size, unit = MEASUREMENT.match(value).groups()
        if unit == "cm" and 150 <= int(size) <= 193:
            return value
        if unit == "in" and 59 <= int(size) <= 76:
            return value
        raise ValueError


passports: int = 0
for line in lines:
    with suppress(ValidationError):
        passport = Passport(**dict(pair.split(":") for pair in line.split()))
        passports += 1

submit(passports, part="b")
