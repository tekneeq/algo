# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# 28. Find the Index of the First Occurrence in a String


haystack = "mississipi"
needle = "pi"
needle = "ssipi"


def strStr(haystack: str, needle: str) -> int:
    def one(haystack, needle):
        hptr = nptr = 0
        found_idx = -1
        maybe_idx = -1
        started = False
        while hptr < len(haystack):
            if haystack[hptr] == needle[nptr]:
                started = True
                if nptr == 0:
                    maybe_idx = hptr

                nptr += 1

                # check if end of nptr
                if nptr == len(needle):
                    found_idx = maybe_idx
                    break
            else:
                nptr = 0

                if started:
                    hptr = maybe_idx

                started = False

            hptr += 1

        return found_idx

    return one(haystack, needle)


assert (strStr(haystack, needle)) == 5
