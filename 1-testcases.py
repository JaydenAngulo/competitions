import sys
import math
import string

test_line = sys.stdin.readline().rstrip()

T = int(test_line)
print("Number of test cases:", T)

for i in range(T):
    line = sys.stdin.readline().rstrip()
    a, b = map(int, line.split())
    sum = a + b
    product = a * b
    print(sum, product)