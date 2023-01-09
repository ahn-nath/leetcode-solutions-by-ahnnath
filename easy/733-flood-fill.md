# Intuition
The solution you need to apply to the code can be summarized as: 
If the initial color of the starting pixel is not the same as the color received as an argument, change it to the color received as an argument. 
Change the color of the neighboring pixels (the starting pixel's neighbors).

My first thoughts after understanding the task were:
Instead of checking against the pixels that do not meet our criteria (are not going to be updated), we can simply tag the ones that meet the criteria and update all pixels without a flag immediately. That means that I intended to iterate over the matrix without considering or performing meaningful operations on those pixels that did not have the starting color. 
I thought about iterating each top, bottom, left, and right pixel from the starting pixel upwards, but that resulted in a confusing and not-so-efficient solution. 


# Approach

**Concepts:**
- *Starting color:* the color of the starting pixel we find in image[sr][sc], which is represented by an int.
 

- *Starting pixel*: the item we received as the starting point of the search image[sr][sc] Where sr (row index) and sc (column index) are both parameters.


- *Neighboring pixels:* those pixels that are connected 4-directionally to the starting point or that are 4-directionally connected to the pixels with just mentioned. 4 directionally, would mean vertically and horizontally. In other words, to the left and right side of the starting pixels, as well as to the top and bottom sides. 

**The code**
1. *Initialization*
Initially, we record the starting color, which is used as a criterion to identify the pixels we need to change, and we initialize a stack with the starting pixel. The stack will save/keep those pixels that are neighbors of the starting pixel. Then we check if the starting color is the same as the color we received as an argument, because if so, no changes are needed to the matrix. 
NOTE: Remember, we update the pixel given, as well as its neighboring pixels (which must have the same color as the starting pixels in order for them to be updated). If the starting pixels have the intended color, the other pixels should too and no update is needed. 


2. *Loop*
We first check the starting pixel, if it has the starting color as its value, we change the color to “color,” And we check if it has any pixel connected to the top, bottom, left and right. If so, we update the stack and add those items to the list. 


3. *Continuation*
We continue to do so for the next items and repeat the process until the stack is empty. Once the stack is empty, we know there are no neighboring pixels or pixels connected to the starting point that has the starting color.  

We finally return the image. 

# Complexity
**Time Complexity:** O(N), where N is the number of pixels in the image. The time complexity of this for loop would be O (n) because the number of iterations is varying with the value of n.


# Code
```
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # get the initial color other adjacent pixels should be
        initial_color = image[sr][sc]
        stack = [(sr, sc)]

        # if the initial color is the same as the color we want to change to, return the image
        if initial_color == color:
            return image

        # while stack has something to look for
        while len(stack) != 0:
            # set current to latest element
            current = stack.pop()
            sr, sc = current

            # check if current is target, to stop search
            if image[sr][sc] == initial_color:
                image[sr][sc] = color

                # handle children
                # left = (sr, sc - 1) if sc - 1 >= 0 else None
                left = image[sr][sc - 1] if sc - 1 >= 0 else None
                # right = (sr, sc + 1) if sc + 1 < len(image[0]) else None
                right = image[sr][sc + 1] if sc + 1 < len(image[sr]) else None
                # top = (sr - 1, sc) if sr - 1 >= 0 else None
                top = image[sr - 1][sc] if sr - 1 >= 0 else None
                # bottom = (sr + 1, sc) if sr + 1 < len(image) else None
                bottom = image[sr + 1][sc] if sr + 1 < len(image) else None

                # check if adjacent pixels are present (top, bottom, left, right)
                if top == initial_color:
                    stack.append((sr - 1, sc))

                if bottom == initial_color:
                    stack.append((sr + 1, sc))

                if left == initial_color:
                    stack.append((sr, sc - 1))

                if right == initial_color:
                    stack.append((sr, sc + 1))

        # output
        return image
```