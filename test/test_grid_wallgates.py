from grid.wallgates import wallgates, wallgates_dfs

ROOMS = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
ANS = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
def test_wallgates():
    assert wallgates(ROOMS) == ANS

def test_wallgates_dfs():
    assert wallgates_dfs(ROOMS) == ANS
