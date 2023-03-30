# 989. Add to Array-Form of Integer

# Intuition
We can convert num, the list, to a string and then convert it to an integer to get the product of adding num 
(as an integer) and k. Then we can add the two numbers together and convert the result to a list by iterating over the
result as a string. We can then return the list.

# Approach
1. Convert num to a string and then to an integer
2. Add the two numbers together (num + k)
3. Convert the result to a string
4. Iterate over the string and add each character to a list from left to right

# Complexity
- Time complexity:
$$O(n)$$


- Space complexity:
$$O(n)$$

# Code
```
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''
        # iterate over each item and append to string
        for n in num:
            s += str(n)
        # sum k and s
        result = k + int(s)
        # convert result to list/array
        array_form = []
        for n in str(result):
            array_form.append(int(n))

        # out
        return array_form
```