#!/usr/bin/env python3
"""write an async routine called wait_n"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns list of all the delays"""
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(delays)]
    return finish
