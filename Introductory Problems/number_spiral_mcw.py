# -*- coding: utf-8 -*-
"""number spiral mcw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fJDwJape3ximQnZGl27rgo7USoPo9z5x
"""

# number spiral - nish
testCase = int(input())
for t in range(testCase):
  x,y = map(int,input().split())
  if x<y:
    if y%2==0:
      temp = (y-1)*(y-1)+1
      res = temp+x-1
    else:
      temp = y*y
      res = temp-x+1
  else:
    if x%2==0:
      temp = x*x
      res = temp-y+1
    else:
      temp = (x-1)*(x-1)+1
      res = temp+y-1
  print(int(res))