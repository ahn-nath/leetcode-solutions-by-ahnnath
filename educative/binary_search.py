def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    middle = (start + end) // 2

    while start <= end:
        if target == nums[middle]:
            return middle

        if target > middle:
            start = middle + 1

        elif target < middle:
            end = middle - 1

        middle = (start + end) // 2

    return -1


if __name__ == '__main__':
    # binary_search(nums=[1, 2, 3, 4, 5], target=3)  # 2
    # binary_search(nums=[-3, 0, 2, 6, 12], target=6)  # 3
    binary_search(nums=[1, 5, 23, 111], target=35)  # -1
