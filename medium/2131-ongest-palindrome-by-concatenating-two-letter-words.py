
'''
# idea:

- pop one element from the list
- if the element has two identical characters, sum +2 and skip next steps till the last
- iterate over the remaining list
- for each element, compare with popped[first] element on the terms:
    1. they are NOT the same
    2. first[0] == second[1] and first[1] == second[0]
- if both terms are met, pop the second (the one compared) element and sum 2 for each match
- repeat the process all over again
'''