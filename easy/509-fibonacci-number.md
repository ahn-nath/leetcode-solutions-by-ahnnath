# Intuition
My first thought was to look at several examples of the Fibonnaci sequence. I searched [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number) and found:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.

When you observe this closely, you will notice that in the pattern, after
the first two numbers, we keep adding/summing up the last number of the previous
operation and the result of the two. 

For example, above, we start with:
>  0 + 1 = 1
> 
>  1 (last item of the previous operation) + 1 (result of the previous operation) = 2
Then we continue with the same logic
> 
> 1 + 2 = 3
> 
> 2 + 3 = 5
> 
> 3 + 5 = 8
> 
> 5 + 8 = 13
> 
> 8 + 13 = 21
> 
> 13 + 21 = 34
>
> ...


# Approach
- We define to variables, `prev` and `next` and initialize them to 0 and 1 respectively.
- We start a for loop with a dummy variable, _, and we set `res` to the result of adding prev and next. 
- Then `prev` will be equal to `next`. 
- `next` will be equal to `res`. 
- We finally return the result after we have iterated `n` times.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
class Solution:
    def fib(self, n: int) -> int:
        # if n is zero or 1, there are no iterations we need to make
        if n == 0 or n == 1:
            return n

        # prev will always take the last's addend in future operations
        prev = 0
        # next will take the last value of 'res' or the result as a new addend 
        nexti = 1
        # from 1 till n, sum
        for _ in range(n-1):
            res = prev + nexti
            prev = nexti
            nexti = res

        return res
```


