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


def sortList_slow(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # iterate over list
    is_not_checked_as_sorted = True  # if the list has not been verified as sorted
    while is_not_checked_as_sorted:
        # check the whole list to see if sorted, we assume it is sorted at first
        is_not_checked_as_sorted = False
        node = head
        prev = None
        nexti = node.next
        # iterate over the whole list to swap elements
        while nexti:
            # swap and mark list as unsorted
            if node.val > nexti.val:
                is_not_checked_as_sorted = True

                # if the node of head will be swapped, update the head reference
                if node is head:
                    head = nexti

                # swap elements: the nexti node should be before the node and point to node.next for its next attribute,
                # and the nexti node should point to the nexti.next value
                nexti.next, node.next = node, nexti.next
                if prev:
                    prev.next = nexti
                # update values
                node = nexti

            # check next
            prev = node
            node = node.next
            nexti = node.next

    print(head)
    return head


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # iterate over strong to get elements
    node = head
    numbers = []
    while node:
        numbers.append(node.val)
        node = node.next

    # sort results and compare contents
    if numbers == numbers.sort():
        return head

    # construct linked list
    head = ListNode(numbers[0])
    prev = head
    if len(numbers) > 1:
        for num in numbers[1:]:
            # create new node and add to linked list
            new_node = ListNode(num)
            prev.next = new_node
            # update prev
            prev = new_node
    print(head)
    return head





if __name__ == '__main__':
    linked_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    # [-1,5,3,4,0]
    linked_list2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

    print(sortList(linked_list))
    print(sortList(head=None))
    print(sortList(linked_list2))  # [-1,0,3,4,5]
