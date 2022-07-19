from dp.problem.coin_change import coin_change, coin_change_brute


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change_brute([1, 2, 5], 11) == 3
