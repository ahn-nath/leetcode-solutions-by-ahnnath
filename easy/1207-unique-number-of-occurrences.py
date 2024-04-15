from collections import Counter
from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    # count elements
    c = Counter(arr)

    # if each count is unique, the counts list should have the same lenght
    # as the number of elements when we compare them
    return len(c.keys()) == len(set(c.values()))


if __name__ == '__main__':
    uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3])  # True
    uniqueOccurrences(arr=[1, 2])  # False
    uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])  # True
    uniqueOccurrences(arr=[1, 2, 2, 3, 3, 3])  # False
