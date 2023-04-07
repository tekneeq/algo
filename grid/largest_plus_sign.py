# 764. Largest Plus Sign
# https://leetcode.com/problems/largest-plus-sign/description/
from typing import List


def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
        # brute force
        # for each node (x,y) in grid, get the lartgest plus sign

        # 0 0
        # 0 1
        #

        def get_most(x, y, grid, direction):
            # up means x - 1

            # down means x + 1

            # left means y - 1

            # right means y + 1
            if direction == "up":
                # up means x - 1
                cnt = 0
                cur_x = x
                while True:
                    try:
                        ##
                        if cur_x == 0:
                            break

                        if x == 3 and y == 2:
                            print(f"Checking ({cur_x-1}, {y}) to be {grid[cur_x-1][y]}")

                        if grid[cur_x-1][y] == 1:
                            cnt += 1
                        ##
                        else:
                            # hit the mine so we cant continue
                            break


                        cur_x -= 1
                    except IndexError:
                        break
                return cnt

            if direction == "down":
                # down means x + 1
                cnt = 0
                cur_x = x
                while True:
                    try:
                        if grid[cur_x+1][y] == 1:
                            cnt += 1
                        ##
                        else:
                            break

                        cur_x += 1
                    except IndexError:
                        break
                return cnt


            if direction == "left":
                # left means y - 1
                cnt = 0
                cur_y = y
                while True:
                    try:
                        ##
                        if cur_y == 0:
                            break

                        if grid[x][cur_y-1] == 1:
                            cnt += 1
                        ##
                        else:
                            break
                        cur_y -= 1
                    except IndexError:
                        break
                return cnt

            if direction == "right":
                # left means y + 1
                cnt = 0
                cur_y = y
                while True:
                    try:
                        if grid[x][cur_y+1] == 1:
                            cnt += 1
                        ##
                        else:
                            break
                        cur_y += 1
                    except IndexError:
                        break
                return cnt





        def get_plus(x, y, n, grid):
            # a plus means up/down/left/right are 1

            if x == 0 or y == 0:
                ##
                if grid[x][y] == 1:
                    return 0
                return -1

            if x == n or y == n:

                ##
                if grid[x][y] == n:
                    return 0
                return -1

            ##
            if grid[x][y] == 0:
                return -1

            up = get_most(x, y, grid, "up")
            down = get_most(x, y, grid, "down")
            left = get_most(x, y, grid, "left")
            right = get_most(x, y, grid, "right")

            min_num = min(up, down, left, right)
            print(f"({x}, {y}) - min: {min_num}, up: {up}, down: {down}, left: {left}, right: {right}")

            return min_num



        grid = [ [1 for i in range(n)] for i in range(n) ]

        if len(mines) == n*n:
            return 0

        for x,y in mines:
            grid[x][y] = 0

        max_plus = 0
        for i in range(n):
            for j in range(n):
                plus = get_plus(i,j, n, grid)
                ##
                if plus > -1:
                    plus += 1

                if plus > max_plus:
                    max_plus = plus



        return max_plus

#time and spach both O(n^2)
def orderOfLargestPlusSign2(self, n, mines):
        dp, ans = [[0]*n for _ in range(n)], 0
        banned = {tuple(mine) for mine in mines}

        for i in range(n):
            count = 0
            for j in range(n):
                count = count + 1 if (i,j) not in banned else 0
                dp[i][j] = count

            count = 0
            for j in range(n-1,-1,-1):
                count = count + 1 if (i,j) not in banned else 0
                dp[i][j] = min(dp[i][j], count)


        for j in range(n):
            count = 0
            for i in range(n):
                count = count + 1 if (i,j) not in banned else 0
                dp[i][j] = min(dp[i][j], count)

            count = 0
            for i in range(n-1,-1,-1):
                count = count + 1 if (i,j) not in banned else 0
                dp[i][j] = min(dp[i][j], count)
                ans = max(ans, dp[i][j])

        return ans

