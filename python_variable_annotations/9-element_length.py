#!/usr/bin/env python3
"""These function’s parameters should
return values with the appropriate types"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                   typing.List[typing.Tuple[typing.Sequence, int]]:
    """Function that returns element length"""
    return [(i, len(i)) for i in lst]
