"""
# idea:

    - pop one element from the list
    - if the element has two identical characters, sum +2 and skip next steps till the last
    - iterate over the remaining list
    - for each element, compare with popped[first] element on the terms:
        1. they are NOT the same
        2. first[0] == second[1] and first[1] == second[0]
    - if both terms are met, pop the second (the one compared) element and sum 2 for each match
    - repeat the process all over again
"""

"""
# idea:
- use counter to get pairs first
- after it, for each "extra", rest one and add to anothe rdictionary
- later, compare dictionary with other keys based on letter positions and possible pairs. Remember to remove keys.
maybe just one normal list and not a dictionary.
"""
from collections import Counter
from typing import List


def longestPalindrome(words: List[str]) -> int:
    longest_total = 0
    pairs_copy = Counter(words)
    identical_present = False

    # iterate over dictionary to add values to the longest_total variab;e
    for key, val in pairs_copy.items():
        # check basic requirements
        matching_reverse_key = key[::-1]
        matching_reverse_key_val = pairs_copy.get(matching_reverse_key)

        # the item has to meet the basic requirements to be in a palindrome
        # 1. handle the case with a same letters key
        if key[0] == key[1]:
            # if a val is not whole/divisible by two, check case
            if val % 2 != 0:
                # check if we have a central pair/exception
                if not identical_present:
                    longest_total += 1
                    identical_present = True
                # update the value
                val = val - 1

            # add value in the end
            longest_total += val

        # 2. handle the case with the key of different letters and a mirror
        elif matching_reverse_key_val:
            # update longest_total by getting the min between the two values
            value_to_add = min(val, matching_reverse_key_val)
            longest_total += (value_to_add * 2)

            # remove the mirroring key(?) to prevent future unnecessary searches
            pairs_copy[key] = None

    # update output
    longest_total = longest_total * 2

    # out
    return longest_total


if __name__ == '__main__':
    # samples
    longestPalindrome(words=["lc", "cl", "gg"])  # 6
    longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"])  # 8
    longestPalindrome(words=["cc", "ll", "xx"])  # 2
    longestPalindrome(words=["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"])

    longestPalindrome(words=["em", "pe", "mp", "ee", "pp", "me", "ep", "em", "em", "me"])  # 14
    longestPalindrome(words=
                      ["ll", "lb", "bb", "bx", "xx", "lx", "xx", "lx", "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb",
                       "bx", "xl", "lb", "xx"])  # 26

    words = ["ll", "lb", "bb", "bx", "xx", "lx", "xx", "lx", "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb",
             "bx", "xl", "lb", "xx"]  # 26
