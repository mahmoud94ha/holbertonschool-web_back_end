#!/usr/bin/env python3
""" function to_kv """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function to_kv """
    return (k, float(v**2))
