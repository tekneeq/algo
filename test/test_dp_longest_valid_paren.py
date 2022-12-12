from dp.longest_valid_paren import longest_valid_paren, longest_valid_paren_stack


def test_longest_valid_paren():
    #assert longest_valid_paren("(()") == 2
    #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
    #  (  (  )  )  (  )  )  )  )  (  )  (  )  (  )  (  )
    #  0  0  2  4  0  6  0  0  0  0  2  0  4  0  6  0  8
    #        0       -1  6  7
    #\assert longest_valid_paren("(())())))()()()()") == 8


def test_longest_valid_paren_stack():
    #assert longest_valid_paren("(()") == 2
    #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
    #  (  (  )  )  (  )  )  )  )  (  )  (  )  (  )  (  )
    #  0  0  2  4  0  6  0  0  0  0  2  0  4  0  6  0  8
    #        0       -1  6  7
    assert longest_valid_paren_stack("(())())))()()()()") == 8