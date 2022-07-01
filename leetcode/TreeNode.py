from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, x):
        if id(self) == id(x):
            return True
        if x and self.val == x.val:
            return self.left == x.left and self.right == x.right
        return False

    def __str__(self):
        vals = [str(node.val) if node else 'null' for node in self]
        while vals[-1] == 'null':
            vals.pop()
        return f"[{','.join(vals)}]"

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __iter__(self):
        self.__nodes = deque([self])
        return self

    def __next__(self):
        if not self.__nodes:
            raise StopIteration

        node = self.__nodes.popleft()
        if node:
            self.__nodes.append(node.left)
            self.__nodes.append(node.right)
        return node


def list_to_treenodes(nums: str):
    if not nums:
        return None

    nodes = [
        TreeNode(int(val)) if val != "null" else None
        for val in nums.strip("[]{}").split(",")
    ]

    childs = nodes[::-1]
    root = childs.pop()

    for node in nodes:
        if not node:
            continue
        if childs:
            node.left = childs.pop()
        if childs:
            node.right = childs.pop()

    return root


if __name__ == "__main__":
    from icecream import ic

    tree = list_to_treenodes("[1,3,2,5,3,null,9]")
    ic(str(tree))
