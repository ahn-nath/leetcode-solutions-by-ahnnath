from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # print the linked list
    def __str__(self):
        node = self
        output = ""
        while node:
            output += str(node.val)
            output += " -> "
            node = node.next
        output += "None"
        return output


def removeNthFromEnd(head: Optional[ListNode], num: int) -> Optional[ListNode]:
    """
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
        :param head:
        :param num:
        :return: head of the linked list
    """
    node = head
    count = 0
    linked_list_indexes = {}
    # while the node is not null
    while node:
        # we count each node to keep track of the Linked List size
        count += 1
        # add reference to node in dictionary
        linked_list_indexes[count] = node
        # next
        node = node.next

    # process to remove index at position
    if count <= 1:
        head = None
    # if the head will be deleted
    elif count == num:
        return head.next
    else:
        # get the index prior to it,
        prev_node = linked_list_indexes.get(count - num)
        # and the index next to it
        next_node = linked_list_indexes.get((count - num) + 2)
        # remove node
        prev_node.next = next_node

    return head


if __name__ == "__main__":
    # case 1
    head_test = ListNode(1)
    head_test.next = ListNode(2)
    head_test.next.next = ListNode(3)
    head_test.next.next.next = ListNode(4)
    head_test.next.next.next.next = ListNode(5)
    n = 2

    # case 2
    head_test2 = ListNode(1)
    n2 = 1

    # case 3
    head_test3 = ListNode(1)
    head_test3.next = ListNode(2)
    n3 = 1

    # print results
    print(removeNthFromEnd(head_test, n))
    print(removeNthFromEnd(head_test2, n2))
    print(removeNthFromEnd(head_test3, n3))
