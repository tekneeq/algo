from functools import lru_cache

def longest_valid_paren_stack(s: str):
    max_length = 0
    stck = [-1]  # initialize with a start index
    for i in range(len(s)):
        if s[i] == '(':
            stck.append(i)
        else:
            stck.pop()
            if not stck:  # if popped -1, add a new start index
                stck.append(i)
            else:
                max_length = max(max_length, i - stck[-1])  # update the length of the valid substring
    return max_length


def longest_valid_paren(s: str):
    @lru_cache()
    def dp(i):
        if i == -1 or s[i] == "(":
            print(f"\t1st")
            return 0

        if i >= 1 and s[i - 1:i + 1] == "()":
            print(f"\t2nd")
            return dp(i - 2) + 2

        P = i - dp(i - 1) - 1
        print(f"\tP {P}")

        if P >= 0 and s[P] == "(":
            print(f"\t3rd")
            return dp(i - 1) + dp(P - 1) + 2

        print(f"\t4th")
        return 0

    for i in range(len(s)):
        print(f"{i}: {dp(i)}")
        print()

    return max(dp(i) for i in range(len(s))) if s else 0