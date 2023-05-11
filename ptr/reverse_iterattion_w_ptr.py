from typing import List


def plusOne(digits: List[int]) -> List[int]:
    # [9]
    # [1, 0]

    # [1, 9]
    # [2, 0]

    # [9, 9]
    # [1, 0, 0]

    ptr = len(digits) - 1
    started = False
    carry = 0
    while ptr >= 0:
        if not started:
            csum = digits[ptr] + 1
            started = True
        else:
            csum = digits[ptr] + carry

        if csum > 9:
            digits[ptr] = csum % 10
            carry = 1
        else:
            digits[ptr] = csum
            carry = 0
            break

        ptr -= 1

    if carry == 1:
        return [1] + digits

    return digits


assert plusOne([9]) == [1, 0]
assert plusOne([1, 9]) == [2, 0]
assert plusOne([9, 9]) == [1, 0, 0]
