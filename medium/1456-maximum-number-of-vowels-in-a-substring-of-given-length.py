def maxVowels(s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    max_vowels = 0
    # iterate over array to count vowels
    while i < len(s):  # TODO: check it to be subs_count + i < len
        # set the current letter and reset the counter used for contingent vowels
        letter = s[i]
        subs_count = 0
        # if the current item is a vowel, count it
        while letter in vowels:
            subs_count += 1
            # update
            i += 1
            letter = s[i] if i < len(s) else None

        # if the subs_count is greater than max_vowels, update max_vowels
        if subs_count > max_vowels:
            max_vowels = subs_count

        if max_vowels >= k:
            print(k)
            return k

        # continue loop
        i += 1

    print(max_vowels)
    return max_vowels


def maxVowels(s: str, k: int) -> int:
    # we use a set because the lookup will be faster
    vowels = {'a', 'e', 'i', 'o', 'u'}

    start, end = 0, 0

    max_count = 0
    subs_count = 0
    while subs_count + (len(s) - end) > max_count:
        # sliding window that will change the subs_count according to the positions we lose in the window
        if s[end] in vowels:
            subs_count += 1

        # if we have reached the limit of the window, update start and check subs_count
        if end - start >= k - 1:
            # check if subs_count has reached the limit to return
            if subs_count >= k:
                print(k)
                return k
            # else, update max_count if necessary
            if subs_count > max_count:
                max_count = subs_count

            # check if we need to update the subs_count
            if s[start] in vowels:
                subs_count -= 1

            start += 1

        end += 1

    print(max_count)
    return max_count


if __name__ == '__main__':
    maxVowels(s="abciiidef", k=3)  # 3
    maxVowels(s="aeiou", k=2)  # 2
    maxVowels(s="leetcode", k=3)  # 2
    maxVowels(s="weallloveyou", k=7) # 4
