#!/usr/bin/python3
'''Prime Game'''


def isWinner(num_rounds, nums):
    '''Finds the winner'''
    winner_counter = {'Maria': 0, 'Ben': 0}

    for m in range(num_rounds):
        round_winner = determine_round_winner(nums[m], num_rounds)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None


def determine_round_winner(n, num_rounds):
    '''Determines round winner'''
    number_list = [m for m in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for m in range(n):
        # Get current player
        current_player = players[m % 2]
        selected_indices = []
        prime = -1
        for idx, num in enumerate(number_list):
            # If a prime number is already picked, check if the current number is a multiple of the prime number
            if prime != -1:
                if num % prime == 0:
                    selected_indices.append(idx)
            # Otherwise, check if the current number is prime and pick it
            else:
                if is_prime(num):
                    selected_indices.append(idx)
                    prime = num
        # If failed to pick a number, the current player lost
        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            # Remove the selected numbers from the list
            for idx, val in enumerate(selected_indices):
                del number_list[val - idx]
    return None


def is_prime(n):
    '''Checks if a number is prime'''
    # 0, 1, and even numbers greater than 2 are NOT PRIME
    if n < 2 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Check divisibility by odd numbers up to the square root of n
        for m in range(3, int(n**(1/2))+1, 2):
            if n % m == 0:
                return False
        return True
