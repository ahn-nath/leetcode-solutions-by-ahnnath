def KUniqueCharacters(strParam):
    longest_substring = ""
    curr_substring = ""
    k = int(strParam[0])
    unique_k_end = 1
    unique_chars = []

    pointer = 1
    while pointer < len(strParam):  # iterate through the string
        if strParam[pointer] in unique_chars:
            curr_substring += strParam[pointer]

            # update unique_k_end
            if strParam[pointer] == strParam[unique_k_end]:
                unique_k_end = pointer

        elif len(unique_chars) + 1 <= k:
            unique_chars.append(strParam[pointer])
            curr_substring += strParam[pointer]

        else:
            pointer = unique_k_end
            unique_k_end = unique_k_end + 1
            unique_chars = []

            if len(curr_substring) > len(longest_substring):
                longest_substring = curr_substring

            curr_substring = ""

        pointer += 1

    # return
    return longest_substring


if __name__ == '__main__':
    # Output with chosen alternative
    print(KUniqueCharacters(strParam="2abcba"))  # "bcb"
    print(KUniqueCharacters(strParam="3abcabcabc"))  # "abcabcabc"

    """
  print(KUniqueCharacters(strParam=[1, "abcabcabc"]))  # "a"
  print(KUniqueCharacters(strParam=[2, "abcabcabc"]))  # "ab"
  print(KUniqueCharacters(strParam=[3, "abcabcabc"]))  # "abc"
  print(KUniqueCharacters(strParam=[4, "abcabcabc"]))  # "abca"
  print(KUniqueCharacters(strParam=[5, "abcabcabc"]))  # "abcab"
  print(KUniqueCharacters(strParam=[6, "abcabcabc"]))  # "abcabc"
  print(KUniqueCharacters(strParam=[7, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[8, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[9, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[10, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[11, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[12, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[13, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[14, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[15, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[16, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[17, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[18, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[19, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[20, "abcabcabc"]))  # "abcabcabc"
  print(KUniqueCharacters(strParam=[21, "abcabcabc
  """
