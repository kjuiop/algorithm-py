import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    answer = a + b
    if answer > 0:
        print(a + b)
    