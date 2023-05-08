arr = [1, 1, 1, 2, 2, 3, 4, 5]

"""
slow 0 
fast 0 

when fast=3 (2) and slow=0 (1),
2 != 1, 
    arr[0+1] = (2)+
    1 2 1 2 2 3 4 5 
    slow 1
    fast 4

1 2 1 2 2 3 4 5
when fast=4 (2) and slow=1 (2),
    do nothing

1 2 1 2 2 3 4 5
when fast=5 (3) and slow=1 (2)
    arr[1+1] = (3)
    1 2 3 2 2 3 4 5 
    slow 2
    fast 6

when fast=6 (4) and slow=2 (3)
    arr[2+1] = (4)
    1 2 3 4 2 3 4 5
    slow 3
    fast 7

when fast=7 (5) and slow=3 (4)
    arr[3+1] = (5)
    1 2 3 4 5 3 4 5
    slow 4
    fast 8




"""


def one(arr):
    idx = 0

    slow = fast = 0
    while fast < len(arr):
        print(f"slow {slow} {arr[slow]}, {fast} {arr[fast]}")

        if arr[fast] != arr[slow]:
            print(f"\t They are no longer equal. Brining slow up to fast")
            arr[slow + 1] = arr[fast]
            slow += 1

        fast += 1

    tmp = slow + 1
    while tmp < len(arr):
        arr[tmp] = "_"
        tmp += 1

    print(arr)

    return slow + 1


print(one(arr))
