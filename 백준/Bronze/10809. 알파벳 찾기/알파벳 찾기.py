import string

s = input()
answer = []
letters = list(string.ascii_lowercase)

for i in letters:
    answer.append(str(s.find(i)))

print(' '.join(answer))