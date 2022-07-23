def lengthOfLongestSubstring(s: str) -> int:
    # abcabcbb => abc
    # abcbb

    # bbbb => b
    # pwwkew => wke
    #   if match ch is last, restart substr
    # wpwkew => pwke
    #   if match ch is first, substr = substr[1:]
    # dvdf => vdf

    # keep track of:
    #   whats in current substring
    # decision:
    #   when to create a new substring

    max_substr = ""
    max_substr_len = 0

    substr = ""

    for idx, ch in enumerate(s):
        if ch not in substr:
            substr += ch

        else:

            # first, record this substr
            if len(substr) > len(max_substr):
                max_substr = substr

            # make the substring until the ch matched
            substr_idx_start = -1
            for sidx, sch in enumerate(substr):
                if sch == ch:
                    substr_idx_start = sidx
                    break
            substr = substr[substr_idx_start + 1:] + ch

    if len(substr) > len(max_substr):
        max_substr = substr

    return len(max_substr)