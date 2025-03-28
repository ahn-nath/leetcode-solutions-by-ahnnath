from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
         Merges nums2 into nums1 in sorted order (in-place).
         nums1 has enough space (m + n) to hold additional elements from nums2.
         """

    # Remove extra elements (if any) by truncating nums1 to length m
    del nums1[m:]  # In-place deletion

    p1, p2 = 0, 0

    while p1 < len(nums1) and p2 < n:
        if nums1[p1] > nums2[p2]:
            nums1.insert(p1, nums2[p2])  # Insert in-place
            p2 += 1
        p1 += 1

    # If there are remaining elements in nums2, append them
    if p2 < n:
        nums1.extend(nums2[p2:])  # Extend in-place


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    merge(nums1, m, nums2, n)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    merge(nums1, m, nums2, n)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    merge(nums1, m, nums2, n)
