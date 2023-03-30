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


def isPalindrome(head: Optional[ListNode]) -> bool:
    # if no value, True
    if not head:
        return True
    # if only one value, True
    if not head.next:
        return True

    # traverse list
    node = head
    output = ""
    while node:
        output += str(node.val)
        node = node.next

    return output == output[::-1]



if __name__ == "__main__":
    # case 1
    head_test = ListNode(1)
    head_test.next = ListNode(2)
    head_test.next.next = ListNode(3)
    head_test.next.next.next = ListNode(2)
    head_test.next.next.next.next = ListNode(1)
    print(head_test)
    print(isPalindrome(head_test))

    # case 2
    head_test = ListNode(1)
    head_test.next = ListNode(2)
    print(head_test)
    print(isPalindrome(head_test))

    # case 3
    head_test = ListNode(1)
    head_test.next = ListNode(2)
    head_test.next.next = ListNode(2)
    head_test.next.next.next = ListNode(1)
    print(head_test)
    print(isPalindrome(head_test))
