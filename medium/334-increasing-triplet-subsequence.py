from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    # initial check to see if there are at least 3 distinctive number in array that could be compared
    if len(set(nums)) < 3:
        print("False EARLY ON")
        return False

    # have a while-loop iterate over elements to check conditions
    i = 0
    while True:
        # if there are NOT three "next" elements, return False
        if i + 2 > len(nums):  # maybe check this condition
            print(False)
            return False

        # if the current element is NOT smaller than the next
        if not nums[i] < nums[i + 1]:
            i += 1
            continue
        # if the element after the next is NOT smaller than the one that succeeds it
        if not nums[i + 1] < nums[i + 2]:
            i += 2
            continue

        # else, return True
        print(True)
        return True


def increasingTriplet(nums: List[int]) -> bool:
    # create set with unique values
    unique_val = set(nums)
    # check to see if there are at least 3 distinctive numbers in array that could be compared
    if len(unique_val) < 3:
        print("False EARLY ON")
        return False

    # sort result
    sorted_unique_val = sorted(unique_val)

    # get the index of each value in the original list
    original_indexes = []
    for val in sorted_unique_val:
        original_indexes.append(nums.index(val))

    counter = 0
    i = 1
    while counter < 2 and i < len(original_indexes):
        candidate_index = original_indexes[i]

        """
        if max(original_indexes[i:]) > candidate_index:
            counter += 1
            prev_index = candidate_index
        i += 1
        """
        counter = 0
        if min(original_indexes[:i]) < candidate_index:
            counter += 1
        if max(original_indexes[i:]) > candidate_index:
            counter += 1

        i += 1

    if counter >= 2:
        print(True)
        return True

    print(False)
    return False

    print(original_indexes)


def increasingTriplet(nums: List[int]) -> bool:
    # check to see if there are at least 3 distinctive numbers in array that could be compared
    if len(set(nums)) < 3:
        print(False)
        return False

    ls = nums

    i = 1
    counter = 0
    prev_index = candidate_index = ls[0]
    while i < len(ls):
        candidate_index = ls[i]

        counter = 0
        if candidate_index == prev_index:
            prev_index = candidate_index
            i += 1
            continue

        if any(y < candidate_index for y in ls[:i]):
            counter += 1
        if any(y > candidate_index for y in ls[i:]):
            counter += 1

        if counter >= 2:
            print(True)
            return True

        i += 1
        prev_index = candidate_index

    print(False)
    return False


if __name__ == '__main__':
    # examples
    increasingTriplet(nums=[1, 2, 3, 4, 5])  # True
    increasingTriplet(nums=[5, 4, 3, 2, 1])  # False
    increasingTriplet(nums=[2, 1, 5, 0, 4, 6])  # True
    increasingTriplet(nums=[1, 1, 1, 2, 4])  # True
    increasingTriplet(nums=[1, 1, 5, 6])  # True
    increasingTriplet(nums=[1, 1, 1, 1])  # False
    increasingTriplet(nums=[20, 100, 10, 12, 5, 13])  # True
    increasingTriplet(nums=[5, 1, 6])  # False
    increasingTriplet(nums=[1, 5, 0, 4, 1, 3])  # True
    increasingTriplet(nums=[5, 1, 5, 5, 2, 5, 4]) # True
