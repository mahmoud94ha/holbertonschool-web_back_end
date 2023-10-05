#!/usr/bin/env python3
""" function make_multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function make_multiplier """

    def multiplierFn(x: float) -> float:
        return x * multiplier

    return multiplierFn
