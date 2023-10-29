from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    max_length = 0
    sequence_count = 0
    supply = k

    i = 0
    # iterate over array to track consecutive 1s
    while i < len(nums):
        item = nums[i]

        while item == 1 and supply < 0:
            if item == 1:
                sequence_count += 1
            # if you find a 0, stop to check if the number of consecutive 0s before the next 1 is equal or less than k
            else:
                supply -= 1
                sequence_count += 1
                # TODO: it may not be necessary to always count the sequence count in if-else blocks

        # if no supply available, add k to the counter and reset the sequence
        if supply == 0 and nums[i + 1] != 1:
            # track the max_length with each sequence
            if sequence_count > max_length:
                max_length = sequence_count

            # start with the next sequence
            supply = k
            sequence_count = 0

        # continue
        i += 1

    print(max_length)
    return max_length


def longestOnes(nums: List[int], k: int) -> int:
    # NOTE: this algorithm is still not working properly and needs to be improved
    max_seq = 0
    seq = 0

    if 1 not in nums:
        return 0

    first = nums.index(1)
    start, end = first, first + 1
    supply = k

    # iterate over array with a while loop
    while start < len(nums):
        ele = nums[start]

        if ele == 1:
            seq += 1

        # if ele == 0 and supply is available, deduct
        elif supply > 0:
            supply -= 1
            seq += 1
        # if no supply, reset values
        else:
            # update the sequence if we start with a 1
            if end < len(nums) and nums[end] == 1:
                """   
                else:
                    print(len(nums))
                    return len(nums)
                """

                supply = k
                seq = 0
                # note: they will be updated soon
                start = end - 1
                end = end

        # check if we need to update max_seq
        if seq > max_seq:
            max_seq = seq

        start += 1
        end += 1

    # print(seq+supply)
    if seq + supply < len(nums):
        max_seq = seq + supply if seq + supply > max_seq else max_seq
    else:
        max_seq = len(nums) if max_seq < seq + supply else max_seq
    # check for max sequence
    print(max_seq)
    return max_seq


if __name__ == '__main__':
    longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2)  # 6
    longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3)  # 10
    longestOnes(nums=[0, 0, 1, 1, 1, 0, 0], k=0)  # 3
    longestOnes(nums=[0, 0, 0, 1], k=4)  # 4
