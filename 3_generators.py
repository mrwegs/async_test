from time import time


def gen1(s):
    for c in s:
        yield c


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('Zhenya')
g2 = gen2(6)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        print(next(task))
        tasks.append(task)
    except StopIteration:
        pass

