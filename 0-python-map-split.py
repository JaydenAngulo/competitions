# good practice to always import these:
import sys
import math
import string

numbers = ["2", "5", "7"]
print("Original numbers as strings", numbers)

result = map(int, numbers)
print("Map result:", result)

converted = list(result)
print("Converted object:", converted)

print("\n--- Using standard input ---")

line = sys.stdin.readline().rstrip()
print("Line:", line)

split_line = line.split()
print("After split():", split_line)

a, b = map(int, split_line)

print("a =", a)
print("b =", b)
print("EXAMPLE ON HOW TO LOOP ON MULTIPLE LINES AND MAP AND SPLIT THEM")

for l in sys.stdin:
    line = l.rstrip()
    
    a, b = map(int, line.split())

    sum = a + b
    product = a * b
    print(sum, product)