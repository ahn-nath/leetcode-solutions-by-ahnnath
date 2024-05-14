from typing import List


def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    # current = asteroids.pop()
    position = len(asteroids) - 1
    while position > 0:
        # previous = position - 1
        # current = position

        # if they have different signs that collide
        if asteroids[position - 1] >= 0 and asteroids[position] < 0:
            c = abs(asteroids[position])
            p = abs(asteroids[position - 1])

            # remove the smaller asteroid
            result = position - 1 if p < c else position if p > c else None

            if result is not None:
                asteroids.pop(result)
            # if they have the same size, remove both
            else:
                asteroids.pop(position)
                asteroids.pop(position - 1)

            # if something was removed, check the same position to compare the new element
            position = position if position < len(asteroids) - 1 else len(asteroids) - 1
            continue

        position -= 1

    return asteroids


if __name__ == '__main__':
    asteroidCollision(asteroids=[-3, -10, 5, 6])  # [-3, -10, 5, 6]
    asteroidCollision(asteroids=[5, 10, -5])  # [5, 10]
    asteroidCollision(asteroids=[8, -8])  # []
    asteroidCollision(asteroids=[10, 2, -5])  # [10]
    asteroidCollision([-2, -1, 1, 2])  # [-2, -1, 1, 2]
    asteroidCollision(asteroids=[-2, -1, 2, -2])  # [-2, -1]
    asteroidCollision(asteroids=[1, -2, -2, -2])
