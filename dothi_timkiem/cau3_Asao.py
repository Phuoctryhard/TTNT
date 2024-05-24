# tran huu ving , nguyen ngoc huong


from collections import defaultdict
from queue import PriorityQueue

data = defaultdict(list)
data['S'] = ['A', 5, 'B', 6, 'C', 5, 10]
data['A'] = ['D', 6, 'E', 7, 9]
data['B'] = ['F', 3, 'G', 4, 8]
data['C'] = ['H', 6, 'K', 4, 7]
data['D'] = ['M', 5, 'N', 8, 6]
data['E'] = ['I', 8, 5]
data['F'] = ['J', 4, 'L', 4, 4]
data['K'] = ['Z', 2, 3]
data['G'] = [10]
data['H'] = [10]
data['M'] = [0]
data['N'] = [10]
data['I'] = [6]
data['J'] = [0]
data['L'] = [9]
data['Z'] = [8]


class Node:
    def __init__(self, name, par=None, g=0, h=0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h

    def __lt__(self, other):
        if other is None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name


def equal(O, G):
    return O.name == G.name


def Check(tmp, c):
    if tmp is None:
        return False
    return any(tmp == item for item in c.queue)


def Path(O):
    if O is None:
        return
    Path(O.par)
    print(O.name)


def AStart(S=Node('S'), G=Node('L')):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)

    while True:
        if Open.empty():
            print('Tim kiem that bai')
            return

        O = Open.get()
        Closed.put(O)
        print('Duyet: ', O.name, O.g, O.h)

        if equal(O, G):
            print('Tim kiem thanh cong')
            Path(O)
            print("Khoang cach: ", O.g + O.h)
            return

        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            g = O.g + data[O.name][i + 1]
            h = data[name][-1]
            tmp = Node(name=name, g=g, h=h)
            tmp.par = O
            ok1 = Check(tmp, Open)
            ok2 = Check(tmp, Closed)

            if not ok1 and not ok2:
                Open.put(tmp)

            i += 2


AStart()
