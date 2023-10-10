from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    # create data structures to deal with the unique value and their counts
    max_operations_counter = 0
    unique_values = dict.fromkeys(nums, 0)
    for num in nums:
        unique_values[num] += 1

    # iterate over the list of unique values to check the number of pairs to be removed
    unique_keys = list(unique_values.keys())
    for num in unique_keys:
        # we get the number needed to reach k
        second_target_value = k - num
        # check if the second target value exist in list
        if second_target_value in unique_values:
            # we add the number of possible <<pairs>> to remove, considering that this corresponds to the smaller count
            if num == second_target_value:
                max_operations_counter += unique_values[num] // 2
            else:
                max_operations_counter += min(unique_values[num], unique_values[k-num])

            # we remove the num item that had its match from the list to prevent "double-checking" the same pair
            del unique_values[num]

    print(max_operations_counter)
    return max_operations_counter


if __name__ == '__main__':
    maxOperations(nums=[1, 2, 3, 4], k=5)  # 2
    maxOperations(nums=[3, 1, 3, 4, 3], k=6)  # 1
    maxOperations(nums=[6, 6, 6, 6, 6, 6, 6], k=12)  # 3
    maxOperations(nums=[3, 3, 3, 4, 4, 4, 4], k=7)  # 3
