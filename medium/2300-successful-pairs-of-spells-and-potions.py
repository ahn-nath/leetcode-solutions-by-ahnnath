from typing import List


def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    # init
    pairs = []
    # sort
    potions.sort()
    for spell in spells:
        # special case
        if spell == 1 and potions[-1] < success:
            pairs.append(0)
            continue

        start = 0
        # initially, it is equal to len(potions)
        special_index = len(potions)
        end = special_index - 1

        while start <= end:
            mid = (start + end) // 2

            if (potions[mid] * spell) >= success:
                end = mid - 1
                special_index = mid

            if (potions[mid] * spell) < success:
                start = mid + 1

        pairs.append(len(potions) - special_index)

    return pairs


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    # init
    pairs = []
    # initially, it is equal to len(potions)
    special_index = len(potions)
    # sort
    potions.sort()
    spells_sorted = sorted(spells)
    for spell in spells_sorted:
        start = 0
        end = special_index - 1

        while start <= end:
            mid = (start + end) // 2

            if (potions[mid] * spell) >= success:
                end = mid - 1
                special_index = mid

            if (potions[mid] * spell) < success:
                start = mid + 1

        # pairs.append(len(potions) - special_index)
        pairs.insert(spells.index(spell), len(potions) - special_index)
    print(pairs)
    return pairs


if __name__ == '__main__':
    # examples
    successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16)  # 2, 0, 2
    successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7)  # 4, 0, 3
