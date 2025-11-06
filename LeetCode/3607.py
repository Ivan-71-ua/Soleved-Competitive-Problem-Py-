
from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(c + 1)]
        maps = [0] * (c + 1)
        id_cur_grp = 1
        group_points = defaultdict(SortedList)
        used = [False] * (c + 1)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(st):
            nonlocal id_cur_grp
            maps[st] = id_cur_grp
            group_points[id_cur_grp].add(st)
            used[st] = True
            for next in adj[st]:
                if not used[next]:
                    dfs(next)
        for i in range(1, c + 1):
            if not used[i]:
                dfs(i)
                id_cur_grp += 1

        res = []
        adj = [1] * (c + 1)
        for do, point in queries:
            cur_id = maps[point]
            if do == 1:
                if len(group_points[cur_id]) > 0:
                    if adj[point] > 0:
                        res.append(point)
                    else:
                        res.append(group_points[cur_id][0])
                else:
                    res.append(-1)
            else:
                if adj[point] > 0:
                    group_points[cur_id].remove(point)
                    adj[point] = -1
        return res




