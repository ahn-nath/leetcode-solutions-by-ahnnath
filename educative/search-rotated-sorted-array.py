def binary_search_rotated(nums, target):
    # determine the first and second halves of the rotated array
    left = 0
    right = len(nums) - 1
    mid_index = None

    while left < right:
        # if the next item is NOT less than left, then the array was rotated at that point
        if nums[left] > nums[left + 1]:
            mid_index = left + 1
            break

        # if the item before is NOT less than rifht, then the array was rotated at that point
        if nums[right] < nums[right - 1]:
            mid_index = right
            break

        left += 1
        right -= 1

    # we assume that the array will always have a mid-index to determine the halves
    first_halve = nums[0: mid_index]
    second_halve = nums[mid_index:]

    # use to track halve number and update the index value if needed
    halve_number = 1
    # perform binary search in each
    for halve in [first_halve, second_halve]:
        start = 0
        end = len(halve) - 1
        middle = (start + end) // 2

        while start <= end:
            if target == halve[middle]:
                if halve_number == 2:
                    middle = middle + len(first_halve)

                return middle

            if target > halve[middle]:
                start = middle + 1

            elif target < halve[middle]:
                end = middle - 1

            middle = (start + end) // 2

        halve_number += 1

    # out when we cannot find the target value in our array
    return -1


if __name__ == '__main__':
    binary_search_rotated(nums=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=1)
