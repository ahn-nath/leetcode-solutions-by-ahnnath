import timeit

"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end
 of the merged string.

Return the merged string.
"""


def mergeAlternately(word1: str, word2: str) -> str:
    result = ''
    # make them lists
    word1 = list(word1)
    word2 = list(word2)
    # while both strings are not empty, keep loopin
    while word1 and word2:
        result += word1.pop(0)
        result += word2.pop(0)

    # append the rest of the first string if not empty
    if word1:
        result += ''.join(word1)

    # append the rest of the second string if not empty
    if word2:
        result += ''.join(word2)

    # out
    return result


def mergeAlternately_a2(word1: str, word2: str) -> str:
    smallest = min([word1, word2], key=len)
    largest = max([word1, word2], key=len)

    result = ''

    for i in range(len(smallest)):
        result += word1[i]
        result += word2[i]

    result += largest[i + 1:]

    return result


if __name__ == '__main__':
    # Output with chosen alternative
    mergeAlternately(word1="abc", word2="pqr")  # apbqcr
    mergeAlternately(word1="ab", word2="pqrs")  # apbqrs
    mergeAlternately(word1="abcd", word2="pq")  # apbqcd

    # Time performance between the two alternatives
    t1 = timeit.timeit(lambda: mergeAlternately(word1="abc", word2="pqr"), number=10000)
    t2 = timeit.timeit(lambda: mergeAlternately_a2(word1="abc", word2="pqr"), number=10000)
    print(f'mergeAlternately - t1: {t1}')
    print(f'mergeAlternately_a2 - t: {t2}')
