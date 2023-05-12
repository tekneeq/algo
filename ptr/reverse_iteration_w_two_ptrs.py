def addBinary(a: str, b: str) -> str:
    a_ptr, b_ptr = len(a) - 1, len(b) - 1

    sum_str = ""
    carry = 0
    cnt = 0
    while a_ptr >= 0 or b_ptr >= 0:
        cnt += 1

        if a_ptr >= 0 and b_ptr >= 0:
            # both ptrs left
            csum = int(a[a_ptr]) + int(b[b_ptr]) + carry
            if csum > 1:
                if csum == 3:
                    sum_str = "1" + sum_str
                else:
                    sum_str = "0" + sum_str
                carry = 1
            else:
                sum_str = str(csum) + sum_str
                carry = 0

        elif a_ptr >= 0:
            # only a_ptrs left
            csum = int(a[a_ptr]) + carry
            if csum > 1:
                carry = 1
                sum_str = "0" + sum_str
            else:
                sum_str = str(csum) + sum_str
                carry = 0
        else:
            # only b_ptrs left
            csum = int(b[b_ptr]) + carry
            if csum > 1:
                carry = 1
                sum_str = "0" + sum_str
            else:
                sum_str = str(csum) + sum_str
                carry = 0

        a_ptr -= 1
        b_ptr -= 1

    if carry == 1:
        sum_str = "1" + sum_str

    return sum_str


assert addBinary("11", "1") == "100"
assert addBinary("1010", "1011") == "10101"
assert addBinary("11", "11") == "110"
