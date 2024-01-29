#!/usr/bin/env python3
"""write an async routine called wait_n"""

import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Function that returns list of all the delays"""
    l: typing.List[float] = []
    for _ in range(n):
        task = await wait_random(max_delay)
        l.append(task)
    return sorted(l)