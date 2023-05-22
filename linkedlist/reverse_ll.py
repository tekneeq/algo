from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def iter():
        cur, prev = head, None

        while cur is not None:
            tmp = cur.next

            # reverse the link
            cur.next = prev
            prev = cur

            # cur is the next node
            cur = tmp

        return prev

    def recur():
        def recurr(n, p):
            tmp = n.next

            n.next = p

            if tmp is None:
                return n

            p = n
            n = tmp

            return recurr(n, p)

        if head is None or head.next is None:
            return head

        output = recurr(head, None)
        return output

    out = recur()
    return out
