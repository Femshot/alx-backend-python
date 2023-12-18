#!/usr/bin/env python3
"""Module containing the function measure_time"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the time it takes to call a specific coroutine"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time() - start

    return end/n
