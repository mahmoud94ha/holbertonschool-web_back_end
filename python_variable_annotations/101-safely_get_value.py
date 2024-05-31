#!/usr/bin/env python3
"""
Type-annotated function safely_get_value
"""
from typing import Sequence, Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, R]:
    """
    Type-annotated function safely_get_value
    """
    if key in dct:
        return dct[key]
    else:
        return default
