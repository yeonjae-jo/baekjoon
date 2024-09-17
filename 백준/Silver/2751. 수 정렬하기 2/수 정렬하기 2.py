import sys
numbers = []
x = int(sys.stdin.readline())

for i in range(x):
    numbers.append(int(sys.stdin.readline()))

sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    print(number)
