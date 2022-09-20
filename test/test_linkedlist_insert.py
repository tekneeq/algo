from linkedlist.llist_insert import insert, iterate, LList, Item

items = [2, 5, 10, 20, 50]


def test_insert_one():
    # init
    test_llist = None
    prev_item = None
    for idx, val in enumerate(items):
        if idx == 0:
            test_llist = LList(Item(val))
            prev_item = test_llist.head
        else:
            my_item = Item(val)
            prev_item.next = my_item
            prev_item = my_item
    prev_item.next = test_llist.head

    # insert
    insert(test_llist, 1)
    iterate(test_llist)


def test_insert_seven():
    # init
    test_llist = None
    prev_item = None
    for idx, val in enumerate(items):
        if idx == 0:
            test_llist = LList(Item(val))
            prev_item = test_llist.head
        else:
            my_item = Item(val)
            prev_item.next = my_item
            prev_item = my_item
    prev_item.next = test_llist.head

    # insert
    insert(test_llist, 7)
    iterate(test_llist)

def test_insert_hundred():
    # init
    test_llist = None
    prev_item = None
    for idx, val in enumerate(items):
        if idx == 0:
            test_llist = LList(Item(val))
            prev_item = test_llist.head
        else:
            my_item = Item(val)
            prev_item.next = my_item
            prev_item = my_item
    prev_item.next = test_llist.head

    # insert
    insert(test_llist, 100)
    iterate(test_llist)