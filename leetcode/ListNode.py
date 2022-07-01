class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if not self.next:
            self.next = ListNode(val)
            return self.next
        self.next.insert(val)

    def __eq__(self, other):
        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next
        return not self and not other

    def __repr__(self):
        return f"ListNode({self.val})"

    def __iter__(self):
        self.head = self
        return self

    def __next__(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            return node
        raise StopIteration


def list_to_nodes(nums: str):
    if not nums:
        return None

    nums = iter(nums.strip("{}[]").split(","))
    root = ListNode(next(nums))
    tmp = root
    for num in nums:
        tmp = tmp.insert(num)
    return root
