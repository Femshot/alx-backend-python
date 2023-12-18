#!/usr/bin/env python3
""" Defines an asynchronous function wait_random"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay between 0 and max_delay

    Args:
        max_delay(int): upper limit of delay range

    Return: delay number
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
