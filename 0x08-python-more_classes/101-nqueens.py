#!/usr/bin/python3

import sys


cols = set()
pos_diag = set()  # (row + col)
neg_diag = set()  # (row - col)
n = int(sys.argv[1])

res = []
board = list(['0'] * n for i in range(n))


def back_track(row):
    if row == n:
        cboard = [''.join(row) for row in board]
        res.append(cboard)
        return

    for c in range(n):
        if c in cols or (row + c) in pos_diag or (row - c) in neg_diag:
            continue
        cols.add(c)
        pos_diag.add(row + c)
        neg_diag.add(row - c)
        board[row][c] = '1'

        back_track(row + 1)

        cols.remove(c)
        pos_diag.remove(row + c)
        neg_diag.remove(row - c)
        board[row][c] = '0'


back_track(0)

for i in range(len(res)):
    idxs = []
    for j in range(len(res[i])):
        for k in range(len(res[i][j])):
            if res[i][j][k] == '1':
                idxs.append([j, k])
    print(idxs)
