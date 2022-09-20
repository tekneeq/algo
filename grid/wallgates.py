import collections
import copy
from typing import List

ROOMS = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]


def wallgates(rooms: List[List[int]]):
    '''
    286

    You are given an m x n grid rooms initialized with these three possible values.

    -1 A wall or an obstacle.
    0 A gate.
    INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

    :param rooms:
    :return: updated room with distance in each block

    algo:
        find gates first
        for each gate, do a bfs
            while bfs, update only if distance is shorter

    '''
    gates = []
    for row in range(len(rooms)):
        for col in range(len(rooms[row])):
            if rooms[row][col] == 0:
                gates.append((row, col))

    def add_to_queue(q, row, col, dis):
        print(f'adding up at ({row-1}, {col}) with distance {dis+1}')
        q.append((row - 1, col, dis + 1))
        # up
        print(f'adding down at ({row - 1}, {col}) with distance {dis + 1}')
        q.append((row + 1, col, dis + 1))
        # left
        print(f'adding left at ({row}, {col-1}) with distance {dis + 1}')
        q.append((row, col - 1, dis + 1))
        # right
        print(f'adding right at ({row}, {col+1}) with distance {dis + 1}')
        q.append((row, col + 1, dis + 1))

    if len(gates) == 0:
        return
    else:
        print(f'found {len(gates)} gates')
        # for each gate, do a bfs
        for gate in gates:
            print(f'Process gate at {gate}')
            q = collections.deque()
            row, col = gate

            add_to_queue(q, row, col, 0)
            seen = set()

            while q:
                # to support bfs, need to pop left instea of pop right (?)
                # yes
                row, col, dis = q.popleft()

                # exit conditions
                # if gate or wall or not valid or already seen
                # or valid grid
                if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]):
                    print(f'({row}, {col}) out of bound')
                    continue

                if rooms[row][col] in [-1, 0] or (row, col) in seen:
                    print(f'({row}, {col}) is gate/wall/seen')
                    continue



                print(f'Adding ({row}, {col}) neighbors')
                # valid so we need to check its neighbors
                seen.add((row, col))
                rooms[row][col] = min(rooms[row][col], dis)
                add_to_queue(q, row, col, dis)


def wallgates_dfs(rooms: List[List[int]]):
    '''

    You are given an m x n grid rooms initialized with these three possible values.

    -1 A wall or an obstacle.
    0 A gate.
    INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

    :param rooms:
    :return: updated room with distance in each block

    algo:
        
    '''







if __name__ == "__main__":
    prev_rooms = copy.deepcopy(ROOMS)

    wallgates(ROOMS)

    for row in prev_rooms:
        print(row)
    print("=========")
    for row in ROOMS:
        print(row)
