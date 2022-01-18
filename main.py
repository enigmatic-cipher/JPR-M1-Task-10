"""
Given n as input, print the following pattern. Note the first number is always n*(n-1) and the number of terms in the pattern is n-1.
Input-> n=4
Output-> 12#24#36#
"""

n = 4
pt = "#"
st = ""
for i in range(1,n):
  st = st + str(i*(n*(n-1))) + pt
print(st)

