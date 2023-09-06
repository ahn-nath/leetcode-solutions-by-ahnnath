def reverseVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    # get list of vowels in string as a list
    vowels_list = [x for x in s if x.lower() in vowels]
    s = list(s)

    # iterate over string and replace each vowels with the last vowel in "vowels_list", remove the item after replacing
    for i in range(len(s)):
        # if a vowel, replace it
        if s[i].lower() in vowels:
            next_vowel = vowels_list.pop()
            s[i] = next_vowel
    # out
    print(s)
    print("".join(s))
    return "".join(s)


if __name__ == '__main__':
    # examples
    print("A".lower())
    reverseVowels(s="hello") # holle
    reverseVowels(s="leetcode")