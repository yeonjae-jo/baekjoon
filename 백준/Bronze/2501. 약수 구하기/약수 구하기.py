numbers = []
n, k = map(int, input().split(" "))
for i in range(1, n+1):
    if n % i == 0:
        numbers.append(i)

if len(numbers) > k-1:
    print(numbers[k-1])
else:
    print(0)
