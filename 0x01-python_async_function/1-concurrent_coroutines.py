#!/usr/bin/env python3
"""COnatains the coroutine wait_n"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes a coroutine n times"""
    results = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))

    return sorted(results)
