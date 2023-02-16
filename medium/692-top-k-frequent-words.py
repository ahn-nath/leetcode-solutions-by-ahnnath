from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    # TODO: study heaps before submitting the solution

    # sort the words in lexicographical order
    words.sort()

    # for loop to keep unique keys
    keys = []
    count = []
    for w in words:
        # for each new key, record and set space for its count
        if w not in keys:
            keys.append(w)
            count.append(1)
        else:
            # get the index and update the count
            i = keys.index(w)
            count[i] = count[i] + 1

    # for loop to get the index of the max value until k is reached
    indexes_max = []
    for _ in range(k):
        max_index = count.index(max(count))
        # update list to get next max index
        count[max_index] = -1
        # append to list
        indexes_max.append(max_index)

    indexes_max.sort()

    # sort the list of indexes and iterate to get them in a different list
    frequent_words = []
    for index in indexes_max:
        frequent_words.append(keys[index])

    print("frequent words:", frequent_words)
    return frequent_words


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2)  # ['i', 'love']
    topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                 k=4)  # ["the","is","sunny","day"]
