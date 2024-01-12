#!/usr/bin/python3
''' Lockboxes'''


def canUnlockAll(boxes):
    '''canUnlockAll'''
    total_boxes = len(boxes)
    keys = [0]
    counter = 0
    index = 0

    while index < len(keys):
        setkey = keys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in keys:
                keys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
