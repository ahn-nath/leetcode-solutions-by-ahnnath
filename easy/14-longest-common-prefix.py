from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # initialize
    longest_prefix = ''
    # pick the shortest string to find the longest prefix possible
    limit = min(strs, key=len)

    # iterate over the first string of the list
    for i in range(len(limit)):
        # get the letter in range
        letter = strs[0][i]
        add_to_prefix = True
        # check if the other string have the same letter in position
        for string in strs:
            # if one letter is not present in string, break the loop
            if string[i] != letter:
                add_to_prefix = False
                break
        # end search if one letter is not present in any of the strings
        if not add_to_prefix:
            break
        # else, keep looking and record letter
        longest_prefix += letter

    # out
    return longest_prefix


if __name__ == '__main__':
    longestCommonPrefix(strs=["flower", "flow", "flight"])
    longestCommonPrefix(strs=["dog", "racecar", "car"])
    longestCommonPrefix(strs=[""])
