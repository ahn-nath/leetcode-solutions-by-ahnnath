import re


def reverseWords(s: str) -> str:
    # separate words by any sequence of non-word characters, strip trailing space
    # to make processing easier
    words = re.split('\W+', s.strip())
    # reverse items in list
    words.reverse()

    # out: join words by single space
    return " ".join(words)


if __name__ == '__main__':
    # examples
    reverseWords(s="the sky is blue")  # "blue is sky the"
    reverseWords(s="  hello world  ")  # "word hello"
