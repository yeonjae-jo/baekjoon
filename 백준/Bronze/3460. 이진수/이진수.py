T = int(input())

for _ in range(T):
    bnum = list(reversed(bin(int(input()))[2:]))
    for i in range(len(bnum)):
        if bnum[i] == '1':
            print(i, end=' ')