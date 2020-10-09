############# Merge sort #############

def sort_slianiem(c):
    if len(c) > 1:
        mid = len(c) // 2
        left = c[:mid]
        right = c[mid:]
        sort_slianiem(left)
        sort_slianiem(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                c[k] = left[i]
                i = i + 1
            else:
                c[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            c[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            c[k] = right[j]
            j = j + 1
            k = k + 1

n = int(input())
c = [int(i) for i in input().split()]
sort_slianiem(c)
print(*c)
