from operator import itemgetter
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = list(map(lambda p: (*p, p[0]**2 + p[1]**2), points))
        points.sort(key=itemgetter(2))
        return map(lambda p: p[:2], points[:k])
        