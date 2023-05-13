from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    # Base cases
    if head is None:
        return None

    if head.next is None:
        return head

    cur = head.next
    last = head

    while cur is not None:  #####
        if cur.val != last.val:
            last.next = cur
            last = cur

        cur = cur.next

    ####
    # [1, 2, 3, 3, 3] wont be caught from the above loop
    # so we just have to make sure last.next is None
    last.next = None

    # return head back
    return head


def create_listnodes(vals: list):
    head = ListNode(vals[0])
    prev = head
    for v in vals[1:]:
        tmp = ListNode(v)
        prev.next = tmp
        prev = tmp

    return head


def listnodes_to_array(head: ListNode):
    mylist = []
    cur = head
    while cur is not None:
        mylist.append(cur.val)
        cur = cur.next
    return mylist


assert listnodes_to_array(deleteDuplicates(create_listnodes([1, 1, 2]))) == [1, 2]

assert listnodes_to_array(deleteDuplicates(create_listnodes([1, 1, 2, 3, 3, 3]))) == [
    1,
    2,
    3,
]
