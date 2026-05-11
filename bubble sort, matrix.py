# bubble sort
##def bubble_sort(a):
##    n = 0
##    for i in a:
##        n += 1
##    for i in range(n):
##        for j in range(n - 1 - i):
##            if a[j] > a[j + 1]:
##                a[j], a[j + 1] = a[j + 1], a[j]
##    return a

#matrix
##import random
##def matrixx(n, m):
##    A = []
##    for i in range(n):
##        A += [[0] * m]
##        for j in range(m):
##            A[i][j] = random.randint(-10, 10)
##    return A
##n = int(input())
##m = int(input())
##for row in matrixx(n, m):
##    for j in row:
##        print(f'{j:4}', end = '')
##    print()
