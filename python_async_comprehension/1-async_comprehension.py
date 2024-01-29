#!/usr/bin/env python3
"""Write a coroutinet that takes no arguments """
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """"   function async_comprehension   """
    Final = [y async for y in async_generator()]
    return Final
