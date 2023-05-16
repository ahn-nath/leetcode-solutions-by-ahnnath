# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __str__(self):
        return f"{self.val} -> {self.next}"


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # iterate over list
    is_unsorted = False
    was_iterated = False
    first_item = None
    while is_unsorted or not was_iterated:
        # check the whole list to see in unsorted
        is_unsorted = False
        node = head
        nexti = node.next
        # iterate over the whole list to swap elements
        while nexti:
            # swap and mark list as unsorted
            if node.val > nexti.val:
                is_unsorted = True
                # swap elements: the nexti node should be before the node and point to node.next for its next attribute,
                # and the nexti node should point to the nexti.next value
                nexti.next, node.next = node, nexti.next

            # update values
            node = nexti
            nexti = node.next
        if is_unsorted and not first_item:
            first_item = node
            was_iterated = True

    print(head)
    return first_item


if __name__ == '__main__':
    linked_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sortList(linked_list)
