import sys
# import numpy as np
sys.setrecursionlimit(10 ** 8)


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))


    class UnionFind:
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n  # 負値 :-size  正:parent を表す
            self.member = [[] for _ in range(self.n)]
            self.done = False

        def find(self, x):  # root を返す
            if self.parents[x] < 0:
                return x
            else:
                return self.find(self.parents[x])

        def union(self, x, y):  # x, y を結合する
            x_root = self.find(x)
            y_root = self.find(y)

            if x_root == y_root:
                return

            if self.parents[x_root] > self.parents[y_root]:
                x_root, y_root = y_root, x_root

            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root

        def size(self, x):  # x が含まれる木のサイズを返す
            return - self.parents[self.find(x)]

        def same(self, x, y):  # x, y が同一の木に含まれるか返す
            return self.find(x) == self.find(y)

        def members(self, x):  # x を含む木に含まれるメンバーをかえす
            x_root = self.find(x)

            if self.done:  # 2回目以降に呼ばれた際は保存した計算結果を返すことで高速に処理する
                return self.member[x_root]

            for i in range(self.n):
                self.member[self.find(i)].append(i)
                self.done = True

            return self.member[x_root]

            # return [i for i in range(self.n) if self.find(i) == x_root]

        def roots(self):  # 根の一覧を返す
            return [i for i in range(self.n) if self.parents[i] < 0]


    union = UnionFind(N)

    for m in range(M):
        c, d = map(int, sys.stdin.readline().strip().split())
        c -= 1
        d -= 1

        union.union(c, d)


    check = [False] * N
    for n in range(N):
        if check[n] is False:
            members = union.members(n)

            sum_A = 0
            sum_B = 0
            for member in members:
                sum_A += A[member]
                sum_B += B[member]
            if sum_A == sum_B:
                for member in members:
                    check[member] = True
            else:
                print('No')
                sys.exit()

    if False in check:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
