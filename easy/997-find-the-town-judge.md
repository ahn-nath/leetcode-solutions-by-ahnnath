# Intuition

Initially, I assumed that each unique number would only have one person they trust, and therefore, it was just a matter
of getting the value from the second index of each array and expecting every other array to also have
the same value at the second index, except for that value. In other words:

- Get the second element of the first array as the suspected town judge.
- Iterate over the rest of the array and check if their second element also had the same value,
- AND, if the second element was never the first element in any other array, because the town judge trust nobody.

Nevertheless, a person can correspond to several other people. In other words, they can trust many people at once.

# Approach

The solution to this would be to them track **who** is trusted and how many people trusts them.
Then we also record the people in the list that trusts others.
Then we simply get the person who is trusted by the total number of people minus one (themselves), and make sure that this person is not in the list of people who trusts.

For the technical approach, we would:
- For each suspect, or trusted person (second element of each array), we record or sum the number of people that trust
them in a dictionary as the value and we keep them as the key.
- For each person that trust (first element of each array), we use a set to track unique copies of all values.
- In the end, we get from the first dictionary the person or key with the maximum number of trustees, and we check that the same key is not part of the people set.
- We return the key. 
- If the array is empty or the conditions are not met, return -1, which indicated no town judge. 

# Complexity

- Time complexity: O(n)

- Space complexity: O(n)

# Code

```
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        suspects = {}
        people = set()
        for arr in trust:
            suspect = arr[1]
            person = arr[0]
            if suspect in suspects:
                suspects[suspect] += 1
            else:
                suspects[suspect] = 1
            people.add(person)

        if people and suspects:
            max_key = max(suspects, key=suspects.get)
            if suspects[max_key] == n - 1 and max_key not in people:
                return max_key

        return -1
```