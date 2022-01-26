from greedy.problem.longest_palin import longest_palindrome


def test_longest_palindrome():
    assert longest_palindrome("abccccdd") == 7
    assert longest_palindrome("a") == 1
    assert longest_palindrome("bb") == 2
