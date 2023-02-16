# Intuition

By looking at the problem, we can tell that every single person in the second position
(or 1st) of each array in the trust list would become a suspect, and only the person who matches the total number of
people (that person who is trusted by everyone), can be the town judge.

Next, we need to check that not only the most trusted suspect is trusted by everyone, but also that he is has not
trusted anyone and therefore is not present in our list of confidants or people who has trusted someone.

# Approach
First we check if the list is empty and n==1. If so, we return 1, which is the default person because if only one
person exists, he is the town judge.

Second, we will track the people who are trusted and the number of confidants. We add the person in position 1 to a dictionary; when the 
trusted person is not in dictionary, they are initialized with the first person or the value "1", else a new person is 
added to the count.  

We will also add the person in position 0 (the person who trusts) to a set, to track the number of unique individuals 
that has trusted someone. 

# Complexity

- Time complexity:

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n ==1:
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