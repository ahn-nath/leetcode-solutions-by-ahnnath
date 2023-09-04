from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    # find the greatest without extra candies
    original_greatest = max(candies)
    # result of evaluating each quantity after being altered
    result_altered = []

    # iterate each number of candies, add extra candies and compare with greatest
    for quantity in candies:
        # if greater of the same, append True
        if (quantity + extraCandies) >= original_greatest:
            result_altered.append(True)
        # if smaller, append False
        else:
            result_altered.append(False)

    # out
    result_altered


if __name__ == '__main__':
    kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3)  # [true,true,true,false,true]
    kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1)  # [true,false,false,false,false]
    kidsWithCandies(candies=[12, 1, 12], extraCandies=10)  # [true,false,true]
