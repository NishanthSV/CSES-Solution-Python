# -*- coding: utf-8 -*-
"""Apartments mcw nish.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bmQ8Gg_poio1_eQDUIo89_EJiEYP6UXq
"""

# Apartmets - nish

n,m,k = map(int,input().split())
desired = list(map(int,input().split()))
available = list(map(int,input().split()))

desired = sorted(desired)
available = sorted(available)
count=0
for des in desired:
  for ava in available:
    if ava in range(des-k,des+k):
      count+=1
      desired.remove(des)
      available.remove(ava)
print(count)