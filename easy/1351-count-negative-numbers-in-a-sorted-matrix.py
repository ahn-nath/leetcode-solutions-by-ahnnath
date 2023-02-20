from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    negatives = 0
    # iterate over each array
    for arr in grid:
        # check element of the array
        for element in arr:
            # if negative, count it
            if element < 0:
                negatives += 1
    # out
    return negatives


if __name__ == '__main__':
    countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])  # 8
    countNegatives(grid=[[3, 2], [1, 0]])  # 0
