from typing import List


def compress(chars: List[str]) -> int:
    # this is the pointer of the position to be "edited" or modified on site
    p = 0
    # this helps tracks the position of the duplicate characters as we traverse the loop
    c = 0
    # while loop to track the number of duplicates of a single char
    while p < len(chars) and c < len(chars):
        # TODO: initialize c here with current char
        c_length = 1
        current_c = c
        next_c = c + 1
        # count char
        while chars[current_c] == chars[next_c]:
            c_length += 1
            current_c += next_c
            next_c += 1

        # modify char
        character = chars[c]
        chars[p] = character
        # while loop to update array
        while True:
            pass


if __name__ == '__main__':
    # examples
    compress(chars=["a", "a", "b", "b", "c", "c", "c"])
