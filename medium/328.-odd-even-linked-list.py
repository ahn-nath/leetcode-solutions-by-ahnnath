from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __str__(self):
        return f"{self.val} -> {self.next}"


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    # if no value, return None
    if not head or not head.next:
        return head

    # we will have two nodes, one for the odd list and one for the even list
    odd_node = head
    even_node = head.next
    # we will also have a reference to the start of the even list, so we can connect the odd list with the even list
    even_start_node = head.next
    while even_node and even_node.next:
        # first, we capture the next nodes.
        odd_item = even_node.next  # the next odd item is after the even item
        even_item = odd_item.next  # the next even item is after the odd item
        # second, we update the next attributes of the current nodes and point them to the right items
        odd_node.next = odd_item
        even_node.next = even_item
        # third, we update the current nodes, so they point to the next items for the future loop
        even_node = even_item
        odd_node = odd_item

    # finally, we connect the odd list with the even list. The odd node will be the last, so we just need to point it to
    # the start of the even list, which is the first even item
    odd_node.next = even_start_node
    # head = odd_list
    return head


if __name__ == '__main__':
    # [1, 3, 5, 2, 4]
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # [2, 1, 3, 5, 6, 4, 7]
    linked_list2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    # [1,2,3,4,5,6,7,8]
    linked_list3 = ListNode(1,
                            ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    # [1, 1]
    linked_list4 = ListNode(1, ListNode(1))

    oddEvenList(linked_list)
    oddEvenList(linked_list2)
    oddEvenList(linked_list3)
    oddEvenList(linked_list4)
