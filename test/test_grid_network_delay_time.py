from grid.network_delay_time import networkDelayTime

TIMES = [[2,1,1],[2,3,1],[3,4,1]]


def test_networkDelayTime():
    assert networkDelayTime(TIMES, 4, 2) == 2