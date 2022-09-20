
class LList():
    def __init__(self, head=None):
        self.head = head

class Item():
    def __init__(self, value):
        self.value = value
        self.next = None

def insert(llist, value):
    # 1) first item
    # 2) mid item
    # 3) last item

    new_item = Item(value)
    if new_item.value < llist.head.value:
        # head becomes new item
        # new_item.next is origin head
        # last item.next is new head
        new_item.next = llist.head
        llist.head = new_item

        cur_item = llist.head
        while cur_item.value < cur_item.next.value:
            cur_item = cur_item.next
        cur_item.next = new_item
        return

    added = False
    cur_item = llist.head
    while cur_item.value < cur_item.next.value:
        if cur_item.value < new_item.value < cur_item.next.value:
            save_next = cur_item.next
            cur_item.next = new_item
            new_item.next = save_next

            added = True
            break

        cur_item = cur_item.next

    if not added:
        # last item next  = new item
        # new item next = head
        cur_item.next = new_item
        new_item.next = llist.head

    return


def iterate(llist):

    print()
    cur_item = llist.head
    print_str = ""
    while cur_item.value < cur_item.next.value:
        print_str += f"{cur_item.value}->"
        cur_item = cur_item.next

    # last item
    print_str += f"{cur_item.value}"
    print(print_str)