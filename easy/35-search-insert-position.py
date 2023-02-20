from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    # if present, return index
    # index = nums.index(target)
    if target in nums:
        print(nums.index(target))
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        print(nums.index(target))
        return nums.index(target)


if __name__ == '__main__':
    searchInsert(nums=[1, 3, 5, 6], target=5)
    searchInsert(nums=[1, 3, 5, 6], target=2)
    searchInsert(nums=[1, 3, 5, 6], target=7)
