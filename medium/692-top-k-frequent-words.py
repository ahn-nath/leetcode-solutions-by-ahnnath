from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    # track overall counts for each string
    word_count = {}
    for w in words:
        if w not in word_count:
            word_count[w] = 1
        else:
            word_count[w] += 1

    # track and record overall groups for each count
    count_groups = {}
    for word, count in word_count.items():
        if count not in count_groups:
            count_groups[count] = [word]
        else:
            arr = count_groups[count]
            arr.append(word)
            count_groups[count] = arr

    # get frequent words
    number_added = 0
    frequent_words = []
    # targets = sorted(list(count_groups.keys()))
    while number_added < k:
        max_count = max(count_groups)
        target = sorted(count_groups[max_count])

        for word in target:
            frequent_words.append(word)
            number_added += 1
            if number_added >= k:
                break

        # remove used key from dictionary
        del count_groups[max_count]

    # out
    print(frequent_words)
    return frequent_words


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=1)  # ['i']
    topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2)  # ['i', 'love']
    topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                 k=4)  # ["the","is","sunny","day"]
