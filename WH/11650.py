# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vFtAD7DGzRVfySc7EQZsnB9BGXv9OJxp
"""

#11650

import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    m, n = map(int, read().split())
    ans.append((m,n))

for i in sorted(ans):
    print(i[0], i[1])