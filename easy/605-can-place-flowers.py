from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # index to track position
    i = 0
    # variable to track planted flowers
    planted = 0
    # flowerbed size
    flowerbed_size = len(flowerbed)
    while planted != n and i < flowerbed_size:
        if flowerbed[i] != 1:
            # check if adjacent positions are empty
            left_side_is_empty = True if (i - 1 < 0) or (flowerbed[i - 1] == 0) else False
            right_side_is_empty = True if (i + 1 >= flowerbed_size) or (flowerbed[i + 1] == 0) else False

            # if both sides are empty, we can plant a flower and mark it
            if left_side_is_empty and right_side_is_empty:
                # record planted flower and mark it in the array
                planted += 1
                flowerbed[i] = 1

        # continue
        i += 1
    # out
    return planted >= n


if __name__ == '__main__':
    # examples
    # canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)  # True
    canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2)  # False
