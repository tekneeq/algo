"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    # Time: O(N)
    # Space: O(N)
    def mark():
        cur = head
        cycle = False
        while cur is not None:
            try:
                if cur.visited:
                    cycle = True
                    break
            except:
                pass

            cur.visited = True

            cur = cur.next

        return cycle

    # Time: O(N)
    # Space: O(1)
    def floyd():
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                # there is an END
                return False

            slow = slow.next
            fast = fast.next.next

        return True

    return floyd()
