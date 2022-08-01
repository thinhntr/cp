# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
from typing import List

from tester import Tester


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        v1 = {node1}
        v2 = {node2}
        while True:
            found = False
            if node1 in v2:
                found = True
            if node2 in v1:
                return min(node2, node1) if found else node2
            if found: return node1
            

            if edges[node1] != -1:
                node1 = edges[node1]
            if edges[node2] != -1:
                node2 = edges[node2]
            if node1 in v1 and node2 in v2:
                break
            v1.add(node1)
            v2.add(node2)

        return -1


t = Tester(Solution())

t.test(1, [4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6)
t.test(2, [4, 2, 3, 4, 2], 0, 1)
t.test(2, [4, 2, 3, 4, 2], 1, 0)
t.test(2, [2, 2, 3, -1], 0, 1)
t.test(2, [1, 2, -1], 0, 2)

t.report()
