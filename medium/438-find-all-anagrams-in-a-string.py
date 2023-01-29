from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    partition, anagram = {}, {}
    limit = len(p)
    start, i, counter = 0, 0, 0
    keys_start = []

    for char in p:
        if char in anagram:
            anagram[char] += 1
        else:
            anagram[char] = 1

    # iterate over loop until you reach the end
    while i < len(s):
        # current value corresponding to index
        letter = s[i]

        # update the dictionary, if the key is present
        if letter in partition:
            partition[letter] += 1
        else:
            partition[letter] = 1
        # count and move on with next letter
        # counter += 1

        # check if we should finish the evaluation of the anagram
        if sum(partition.values()) == limit:
            are_the_same = True

            # compare the two dictionaries if they are the same and change the sliding window
            for k, v in anagram.items():
                val = partition.get(k)
                # if any of the two are not the same, break loop because both dictionary need to be the same
                if v != val:
                    are_the_same = False
                    break

            # save the first key if the same
            if are_the_same:
                keys_start.append(start)

            # remove previous start
            partition.pop(s[start])
            start = start + 1
            print("double dict:", partition)
        # keep with next index
        i += 1

    print(keys_start)


def findAnagrams(s: str, p: str) -> List[int]:
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    # initialization
    start_keys = []
    p = sorted(p)
    limit = len(p)
    portion = list(s[:limit])
    start = 0

    for i in range(limit - 1, len(s)):
        # if the slice sorted is equal to the anagram, add start index to array
        if sorted(portion) == p:
            # append start index
            start_keys.append(start)

        # if we do have a next index,
        if i + 1 < len(s):
            # delete first item
            del portion[0]
            # append new last item
            portion.append(s[i+1])
        start += 1

    # return array
    return start_keys


if __name__ == '__main__':
    # findAnagrams(s="abab", p="ab")  # [0,6]
    findAnagrams(s="cbaebabacd", p="abc")  # [0,1,2]
