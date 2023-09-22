from typing import List


def compress(chars: List[str]) -> int:
    # this is the pointer of the position to be "edited" or modified on site
    p = 0
    current_c = 0
    # while loop to iterate over the whole list of chars
    while p < len(chars) and current_c < len(chars):
        # defines the length of the char being evaluated
        c_dupli_length = 1
        # immediate next position
        next_c = current_c + 1
        # count char
        while next_c < len(chars) and chars[current_c] == chars[next_c]:
            # increment length of duplicates counter for current char
            c_dupli_length += 1
            current_c = next_c
            next_c = next_c + 1
        # modify char
        character = chars[current_c]
        # modify position to be edited
        chars[p] = character
        # while loop to the next position with the count
        if c_dupli_length > 1:
            for letter in str(c_dupli_length):
                p += 1
                chars[p] = letter

        # prepare next char to be evaluated and move up the 'p' position
        current_c = next_c
        p += 1

    return p


if __name__ == '__main__':
    # examples
    compress(chars=["a", "a", "b", "b", "c", "c", "c"])  # Output: Return 6, and the first 6 characters of the input
    # array should be: ["a","2","b","2","c","3"]
    compress(chars=["a"])  # Return 1, and the first character of the input array should be: ["a"]
    compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    # Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
