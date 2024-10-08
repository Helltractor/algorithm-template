#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : daily/8/29 上午11:47
# @Author : liupengsay
from collections import defaultdict, deque
from heapq import heappush, heappop
from math import inf

from data_structure.sorted_list.template import SortedList


class Dijkstra:
    def __init__(self):
        return
    
    @staticmethod
    def get_shortest_path(dct, src, initial=0):
        """template of shortest path by dijkstra"""
        #  which can to changed to be the longest path problem by opposite number
        n = len(dct)
        dis = [inf] * n
        stack = [initial * n + src]
        dis[src] = initial
        while stack:
            val = heappop(stack)
            d, i = val // n, val % n
            if dis[i] < d:
                continue
            for j, w in dct[i]:
                assert w >= 0
                dj = d + w
                if dj < dis[j]:
                    dis[j] = dj
                    heappush(stack, dj * n + j)
        return dis
    
    @staticmethod
    def get_longest_path(dct, src, initial=0):
        """template of shortest path by dijkstra"""
        #  which can to changed to be the longest path problem by opposite number
        n = len(dct)
        dis = [inf] * n
        stack = [(-initial, src)]
        dis[src] = -initial
        while stack:
            d, i = heappop(stack)
            if dis[i] < d:
                continue
            for j, w in dct[i]:
                dj = d - w
                if dj < dis[j]:
                    dis[j] = dj
                    heappush(stack, (dj, j))
        return [-x for x in dis]
    
    @staticmethod
    def get_dijkstra_result_sorted_list(dct, src):
        n = len(dct)
        dis = [inf] * n
        dis[src] = 0
        lst = SortedList([(0, src)])
        while lst:
            d, i = lst.pop(0)
            if dis[i] < d:
                continue
            for j, w in dct[i]:
                dj = w + d
                if dj < dis[j]:
                    if dis[j] < inf:
                        lst.discard((dis[j], j))
                    dis[j] = dj
                    lst.add((dj, j))
        return dis
    
    @staticmethod
    def get_cnt_of_shortest_path(dct, src, mod=-1):
        """number of shortest path"""
        n = len(dct)
        dis = [inf] * n
        stack = [(0, src)]
        dis[src] = 0
        cnt = [0] * n
        cnt[src] = 1
        while stack:
            d, i = heappop(stack)
            if dis[i] < d:
                continue
            for j, w in dct[i]:
                dj = w + d
                if dj < dis[j]:
                    dis[j] = dj
                    cnt[j] = cnt[i]
                    # smaller than the shortest path
                    heappush(stack, (dj, j))
                elif dj == dis[j]:
                    # equal to the shortest path
                    cnt[j] += cnt[i]
                    if mod != -1:
                        cnt[j] %= mod
        return cnt, dis
    
    @staticmethod
    def get_dijkstra_result_limit(dct, src, limit, target):
        n = len(dct)
        dis = [inf] * n
        dis[src] = 0 if src not in limit else inf
        stack = [(dis[src], src)]
        while stack and target:
            d, i = heappop(stack)
            if i in target:
                target.discard(i)
            if dis[i] < d:
                continue
            for j, w in dct[i]:
                if j not in limit:
                    dj = w + d
                    if dj < dis[j]:
                        dis[j] = dj
                        heappush(stack, (dj, j))
        return dis
    
    @staticmethod
    def get_shortest_path_from_src_to_dst(dct, src, dst):
        n = len(dct)
        dis = [inf] * n
        stack = [(0, src)]
        dis[src] = 0
        father = [-1] * n
        while stack:
            d, i = heappop(stack)
            if dis[i] < d:
                continue
            if i == dst:
                break
            for j, w in dct[i]:
                dj = w + d
                if dj < dis[j]:
                    dis[j] = dj
                    father[j] = i
                    heappush(stack, (dj, j))
        if dis[dst] == inf:
            return [], inf
        # backtrack for the path
        path = []
        i = dst
        while i != -1:
            path.append(i)
            i = father[i]
        return path, dis[dst]
    
    @staticmethod
    def gen_maximum_product_path(dct, src, dsc):
        dis = defaultdict(lambda: inf)
        stack = [(-1, src)]
        dis[src] = 1
        while stack:
            d, i = heappop(stack)
            d = -d
            if dis[i] > d:
                continue
            for j in dct[i]:
                dj = dct[i][j] * d
                if dj > dis[j]:
                    dis[j] = dj
                    heappush(stack, (-dj, j))
        return dis[dsc]
    
    @staticmethod
    def get_second_shortest_path(dct, src):
        """template of strictly second shorter path"""
        n = len(dct)
        dis = [[inf] * 2 for _ in range(n)]
        dis[src][0] = 0
        stack = [(0, src)]
        while stack:
            d, i = heappop(stack)
            if dis[i][1] < d:
                continue
            for j, w in dct[i]:
                if dis[j][0] > d + w:
                    dis[j][1] = dis[j][0]
                    dis[j][0] = d + w
                    heappush(stack, (d + w, j))
                elif dis[j][0] < d + w < dis[j][1]:  # if not strictly then change to d+w < dis[j][1]
                    dis[j][1] = d + w
                    heappush(stack, (d + w, j))
        return dis
    
    @staticmethod
    def get_cnt_of_second_shortest_path(dct, src, mod=-1):
        """number of strictly second shorter path"""
        n = len(dct)
        dis = [[inf] * 2 for _ in range(n)]
        dis[src][0] = 0
        stack = [(0, src, 0)]
        cnt = [[0] * 2 for _ in range(n)]
        cnt[src][0] = 1
        while stack:
            d, i, state = heappop(stack)
            if dis[i][1] < d:
                continue
            pre = cnt[i][state]
            for j, w in dct[i]:
                dd = d + w
                if dis[j][0] > dd:
                    dis[j][0] = dd
                    cnt[j][0] = pre
                    heappush(stack, (d + w, j, 0))
                elif dis[j][0] == dd:
                    cnt[j][0] += pre
                    if mod != -1:
                        cnt[j][0] %= mod
                elif dis[j][0] < dd < dis[j][1]:  # if not strictly then change to d+w < dis[j][1]
                    dis[j][1] = d + w
                    cnt[j][1] = pre
                    heappush(stack, (d + w, j, 1))
                elif dd == dis[j][1]:
                    cnt[j][1] += pre
                    if mod != -1:
                        cnt[j][1] %= mod
        return dis, cnt
    
    @staticmethod
    def get_cnt_of_second_shortest_path_by_bfs(dct, src, mod=-1):
        """number of strictly second shorter path by bfs"""
        n = len(dct)
        dis = [inf] * 2 * n
        dis[src * 2] = 0
        stack = [(0, src, 0)]
        cnt = [0] * 2 * n
        cnt[src * 2] = 1
        while stack:
            d, i, state = heappop(stack)
            pre = cnt[i * 2 + state]
            for j in dct[i]:
                dd = d + 1
                if dd < dis[j * 2]:
                    dis[j * 2] = dd
                    cnt[j * 2] = pre
                    stack.append((dd, j, 0))
                elif dd == dis[j * 2]:
                    cnt[j * 2] += pre
                    cnt[j * 2] %= mod
                elif dis[j * 2] + 1 == dd < dis[j * 2 + 1]:
                    dis[j * 2 + 1] = dd
                    cnt[j * 2 + 1] = pre
                    stack.append((dd, j, 1))
                elif dis[j * 2] + 1 == dd == dis[j * 2 + 1]:
                    cnt[j * 2 + 1] += pre
                    cnt[j * 2 + 1] %= mod
        return dis, cnt
    
    @staticmethod
    def get_shortest_path_by_bfs(dct, src, initial=-1):
        """shortest path implemention by 01 bfs """
        n = len(dct)
        dis = [initial] * n
        stack = [src]
        dis[src] = 0
        while stack:
            nex = []
            for i in stack:
                for j in dct[i]:
                    if dis[j] == initial:
                        dis[j] = dis[i] + 1
                        nex.append(j)
            stack = nex
        return dis
    
    @staticmethod
    def get_shortest_by_bfs_inf_odd(dct, src):
        """shortest odd path and even path"""
        n = len(dct)
        dis = [[inf, inf] for _ in range(n)]
        stack = deque([[src, 0]])
        dis[0][0] = 0
        while stack:
            i, x = stack.popleft()
            for j in dct[i]:
                dd = x + 1
                if dis[j][dd % 2] == inf:
                    dis[j][dd % 2] = x + 1
                    stack.append([j, x + 1])
        return dis


class UnDirectedShortestCycle:
    def __init__(self):
        return
    
    @staticmethod
    def find_shortest_cycle_with_node(n, dct):
        # brute force by point
        ans = inf
        for i in range(n):
            dist = [inf] * n
            par = [-1] * n
            dist[i] = 0
            stack = [(0, i)]
            while stack:
                _, x = heappop(stack)
                for child in dct[x]:
                    if dist[x] > ans:
                        break
                    if dist[child] > dct[x][child] + dist[x]:
                        dist[child] = dct[x][child] + dist[x]
                        par[child] = x
                        heappush(stack, (dist[child], child))
                    elif par[x] != child and par[child] != x:
                        cur = dist[x] + dist[child] + dct[x][child]
                        ans = ans if ans < cur else cur
        return ans if ans != inf else -1
    
    @staticmethod
    def find_shortest_cycle_with_edge(n, dct, edges):
        # brute force by edge
        ans = inf
        for x, y, w in edges:
            dct[x].pop(y)
            dct[y].pop(x)
            dis = [inf] * n
            stack = [(0, x)]
            dis[x] = 0
            while stack:
                d, i = heappop(stack)
                if dis[i] < d:
                    continue
                if i == y:
                    break
                for j in dct[i]:
                    dj = dct[i][j] + d
                    if dj < dis[j]:
                        dis[j] = dj
                        heappush(stack, (dj, j))
            ans = ans if ans < dis[y] + w else dis[y] + w
            dct[x][y] = w
            dct[y][x] = w
        return ans if ans < inf else -1
