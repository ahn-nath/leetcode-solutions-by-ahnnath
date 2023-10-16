from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    current_sum = sum(nums[:k])
    max_sum = current_sum
    start = 0
    end = k
    while end < len(nums):
        current_sum = sum(nums[start:end])
        max_sum = max(max_sum, current_sum)
        start += 1
        end += 1

    print(max_sum / k)
    return max_sum / k


if __name__ == '__main__':
    findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)  # 12
