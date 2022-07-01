# https://leetcode.com/problems/clone-graph/ 
from collections import deque
from tester import Tester

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        newhead = Node(node.val)
        mapping = {node: newhead}
        stack = deque([node])
        while stack:
            currnode = stack.popleft()
            for neighbor in currnode.neighbors:
                if neighbor not in mapping:
                    stack.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val)
                mapping[currnode].neighbors.append(mapping[neighbor])
        
        return newhead

t = Tester(Solution())

t.test()

t.report()