############# Maximum sort #############

N = int(input())
a = [int(i) for i in input().split()]

while N > 0:
    max_num = a[0]
    index = 0
    for i in range(N):
        if a[i] > max_num:
            max_num = a[i]
            index = i
    a[index], a[N - 1] = a[N - 1], a[index]
    N -= 1

print(*a)

