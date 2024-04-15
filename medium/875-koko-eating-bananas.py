from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if sum((pile + mid - 1) // mid for pile in piles) > h:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    minEatingSpeed(piles=[3, 6, 7, 11], h=8)  # 4
    minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5)
