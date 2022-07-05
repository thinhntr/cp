import heapq
import itertools

PQ_REMOVED = "<removed-task>"


class PriorityQueue:
    """None-duplicate priority queue

    References
    ----------
        https://docs.python.org/3/library/heapq.html
    """
    def __init__(self):
       self.pq = [] 
       self.entry_finder = {}
       self.counter = itertools.count()
    
    def __len__(self):
        return len(self.entry_finder)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = PQ_REMOVED

    def push(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
        

    def pop(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not PQ_REMOVED:
                del self.entry_finder[task]
                return priority, task
        raise KeyError('pop from an empty priority queue')

if __name__ == '__main__':
    q = PriorityQueue()
    q.push('thinh', 3)
    q.push('nguyen', 4)
    q.push('hi', 0)
    q.push('nguyen', 2)
    while q:
        print(q.pop())