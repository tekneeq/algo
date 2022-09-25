import collections
from typing import List
import heapq

'''
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, 
vi is the target node, and 
wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 

If it is impossible for all the n nodes to receive the signal, return -1
'''
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # from K, we need to do a BFS/DFS and assign distance from k

    nodes = collections.defaultdict(list)
    for (u,v,w) in times:
        nodes[u].append((w,v))

    pq = [(0,k)]
    seen = {}
    while pq:
        dis, node = heapq.heappop(pq)
        if node in seen:
            continue

        seen[node] = dis

        for (xdis, xnode) in nodes[node]:
            heapq.heappush(pq, (dis+xdis, xnode))


    if len(seen) != n:
        return -1
    else:
        return max(seen.values())

