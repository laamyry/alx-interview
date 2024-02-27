#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """makeChange"""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        for _ in range(total // coin):
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1
