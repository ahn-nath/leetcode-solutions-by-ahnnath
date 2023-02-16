from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    # sort the words in lexicographical order
    words.sort()

    # for loop to keep unique keys
    keys = []
    count = []
    for w in words:
        # for each new key, record and set space for its count
        if w not in keys:
            words.append(w)
            count.append(0)
        else:
            # get the index and update the count
            i = keys.index(w)
            count[i] = count[i] + 1

    # for loop to get the index of the max value until k is reached

    # sort the list of indexes and iterate to get them in a different list


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    words.sort()
    print(words)

    seti = set(words)
    print(seti)

    # list comprehension to cle
