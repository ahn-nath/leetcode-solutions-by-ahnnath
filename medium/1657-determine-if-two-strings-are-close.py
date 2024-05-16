from collections import defaultdict


def closeStrings(word1: str, word2: str) -> bool:
    count_dict1 = defaultdict(int)
    count_dict2 = defaultdict(int)

    if len(word1) != len(word2):
        return False

    for item in word1:
        count_dict1[item] += 1

    for item in word2:
        count_dict2[item] += 1

    # check the keys are the same
    for key in count_dict1:
        if key not in count_dict2:
            return False

    # check they have the same frequencies
    val1 = count_dict1.values()
    val2 = list(count_dict2.values())
    for value in val1:

        if value not in val2:
            return False

        # remove value from second dict
        val2.remove(value)

    return True


if __name__ == '__main__':
    closeStrings(word1="abc", word2="bca")
    closeStrings(word1="a", word2="aa")
    closeStrings(word1="cabbba", word2="abbccc")
    closeStrings(word1="uau", word2="ssx")
