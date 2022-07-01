from pathlib import Path
from time import perf_counter

class Tester:
    def __init__(self, solution):
        self.name = next(filter(lambda it: not it.startswith("_"), dir(solution)))
        self.fun = getattr(solution, self.name)
        self.total = 0
        self.fail = 0
        self.time = 0

    def test(self, expected, *args, **kwargs):
        start = perf_counter()
        output = self.fun(*args, **kwargs)
        self.time += perf_counter() - start

        isCorrect = output == expected
        self.total += 1

        print(f"Test {self.total} ... {isCorrect}")
        if not isCorrect:
            print("Input:", args, kwargs)
            print("Output:  ", output)
            print("Expected:", expected)
            self.fail += 1
        print()

    def report(self):
        print(f"{self.name} passed {self.total - self.fail} / {self.total} tests")
        print(f"Ran in {round(self.time*1000, 4)}ms")
        print()


class ObjectTester:
    def __init__(self, filepath):
        self.module = __import__(Path(filepath).stem)
        self.total = 0
        self.fail = 0
        self.time = 0
    
    def test(self, expected, ops, args):
        start = perf_counter()
        obj = getattr(self.module, ops[0])(*args[0])
        outputs = [None]
        outputs.extend(getattr(obj, op)(*arg) for op, arg in zip(ops[1:], args[1:]))
        self.time += perf_counter() - start

        for op, arg, output, expect in zip(ops, args, outputs, expected):
            isCorrect = output == expect
            self.total += 1

            print(f"Test {self.total} ... {isCorrect}")
            if not isCorrect:
                print("Input:", op, arg)
                print("Output:  ", output)
                print("Expected:", expect)
                self.fail += 1
            print()

    def report(self):
        print(f"Passed {self.total - self.fail} / {self.total} tests")
        print(f"Ran in {round(self.time*1000, 4)}ms")
        print()
            