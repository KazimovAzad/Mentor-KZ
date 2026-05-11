# sort and search algorithms

# ******** bubble sort
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = list(map(int, input().split()))
print(bubble_sort(a))


# ********** selection sort

# def selection_sort(A):
#    N = len(A)
#    for i in range(N):
#        i_min = i
#        for j in range(i + 1, N):
#            if A[j] < A[i_min]:
#                i_min = j
#        A[i], A[i_min] = A[i_min], A[i]
#    return A


# *********** quick sort

# def quicks(a):
#     if len(a) <= 1:
#         return a
#     p = a[len(a)//2]
#     l = [x for x in a if x < p]
#     m = [x for x in a if x == p]
#     r = [x for x in a if x > p]
#     return quicks(l) + m + quicks(r)
