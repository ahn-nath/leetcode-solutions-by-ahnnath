from typing import List


def findAnagrams(self, s: str, p: str) -> List[int]:
    partition, anagram = {}, {}
    limit = len(p)
    start, i, counter = 0
    keys_start = []

    # iterate over loop until you reach the end
    while start < len(s):
        # current value corresponding to index
        letter = s[i]

        # update the dictionary, if the key is present
        if letter in partition:
            partition[letter] += 1
        else:
            partition[letter] = 1
        # count and move on with next letter
        counter += 1

        # check if we should finish the evaluation of the anagram
        if counter == limit:
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
        # keep with next index
        i += 1


if __name__ == '__main__':
    pass
