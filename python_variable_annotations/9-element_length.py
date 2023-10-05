#!/usr/bin/env python3
""" element_length Function """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length Function """
    return [(i, len(i)) for i in lst]
