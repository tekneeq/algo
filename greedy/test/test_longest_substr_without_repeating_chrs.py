from greedy.problem.longest_substr_without_repeating_chrs import lengthOfLongestSubstring


def test_longest_substr_without_repeating_chrs():
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("dvdf") == 3


