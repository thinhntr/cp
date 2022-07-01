# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
from collections import deque
from typing import List

from tester import Tester


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        visited_all_state = (1 << n) - 1
        mask = [1<<i for i in range(n)]
        queue = deque([(i, mask[i]) for i in range(n)])
        visited_states = [{mask[i]} for i in range(n)]
        step = 0
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                prev_node, prev_state = queue.popleft()
                if prev_state == visited_all_state:
                    return step
                for node in graph[prev_node]:
                    state = mask[node] | prev_state
                    if state == visited_all_state:
                        return step + 1
                    if state not in visited_states[node]:
                        visited_states[node].add(state)
                        queue.append((node, state))
            step += 1
        return step


t = Tester(Solution())

t.test(4, [[1, 2, 3], [0], [0], [0]])
t.test(4, [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])

t.report()
