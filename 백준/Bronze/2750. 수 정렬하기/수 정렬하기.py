cnt = int(input())
numbers = []

for i in range(0, cnt):
    numbers.append(int(input()))

sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    print(number)

