############# Inserts sort #############

N = int(input())
a = [int(i) for i in input().split()]
k = 0

for i in range(N):
    k = i - 1
    num = a[i]
    while a[k] > num and k >= 0:
        a[k + 1], a[k] = a[k], a[k + 1]
        k -= 1

print(*a)
