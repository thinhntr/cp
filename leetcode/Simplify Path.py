# https://leetcode.com/problems/simplify-path/
from tester import Tester
from icecream import ic


class Solution:
    def simplifyPath(self, path: str) -> str:
        absolute = [p for p in path.split("/") if p and p != "."]
        simplified = []
        for p in absolute:
            if p != "..":
                simplified.append(p)
            elif simplified:
                simplified.pop()
        return "/" + "/".join(simplified)


t = Tester(Solution())

t.test("/home", "/home/")
t.test("/", "/../")
t.test("/home/foo", "/home//foo")
t.test("/bin/usr", "/bin/../bin/usr/./../usr")
t.test("/bin/anaconda/bin/python", "/bin/anaconda/bin/../../anaconda/bin/python//")
t.test("/bin/zsh", "/bin/usr/local/time/../../../zsh")
t.test("/bin/zsh", "/bin/usr/local/../../tmp/../zsh")

t.report()
