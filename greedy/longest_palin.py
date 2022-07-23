"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""
import collections


def longest_palindrome(s: str) -> int:
    ans = 0
    uniq_char = False
    for k, v in collections.Counter(s).items():
        print(f"letter {k} value {v}")
        ans += v // 2 * 2

        if v % 2 == 1:
            uniq_char = True

    if uniq_char:
        ans += 1

    return ans
