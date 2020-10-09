############# Bubble sort #############

N = int(input())
c = [int(i) for i in input().split()]

while N != 0:
    for i in range(1, N):
        if c[i] < c[i - 1]:
            c[i], c[i - 1] = c[i - 1], c[i]
    N -= 1

print(*c)

