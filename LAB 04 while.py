#1
##i = 4
##while i < 10:
##    i += 1
##    if i == 7 or i == 9:
##        continue
##    print(i)

#2
##i = int(input())
##s = 0
##while i != 0:
##    s += i
##    i = int(input())
##print(s)

#3
##i = int(input())
##s = 0
##count = 0
##while i != -1:
##    s += i
##    count += 1
##    i = int(input())
##print(s/count)

#4
##a = int(input())
##s = 0
##while a > 0:
##    k = a % 10
##    a = a // 10
##    s += k
##print(s)

#5
##a = int(input())#1441
##copy = a
##a2 = 0
##while a > 0:
##    a2 = a2 * 10 + a % 10
##    a = a // 10
##if copy == a2:
##    print('polindrom')
##else:
##    print('deyil')

#6
##a = int(input())#12342
##while a > 0:
##    if a % 10 == a // 10 % 10:
##        print('he')
##        break
##    a = a // 10
##else:
##    print('yox')

#7
##i = 100 
##while i < 1000:
##    s = (i % 10) ** 3 + (i // 10 % 10 ) ** 3 + (i // 100) ** 3
##    if i == s:
##        print(i)
##    i += 1

#9
##n = int(input())
##s = 0
##i = 0
##while  n > 0:
##    k = n % 10
##    s = s + k * 2 ** i
##    i += 1
##    n = n // 10
##print(s)

#10
##n = int(input())
##s = 0
##i = 1
##while n > 0:
##    k = n % 2
##    s += k * i
##    n = n // 2
##    i = i * 10
##print(s)

#11
##i = 0
##i_2 = 1
##print(i, i_2, end = ' ')
##while i <= 50:
##    i_3 = i + i_2
##    print(i_3, end = ' ')
##    i = i_2
##    i_2 = i_3

###12a
##N = int(input())
##s = 0
##n = 0
##while n <= N:
##    s += n / (1 + n ** 3) ** 1/2
##    n += 1
##print(s)

#12b
##N = int(input())
##s = 0
##i = 1
##while i <= N:
##    s += (i ** i) / i
##    i += 1
##print(s)

#12c
##N = int(input())
##s = 0
##n = 1
##while n <= N:
##    s += (1.1 ** n + n ** 2) / 5 * n
##    n += 1
##print(s)


#13
##def topla(a):
##    s = 0
##    while a > 0:
##        k = a % 10
##        a = a // 10
##        s += k
##    return s
##def vur(a):
##    f = 1
##    while a > 0:
##        k = a % 10
##        a = a // 10
##        f *= k
##    return f
##n = int(input('reqem daxil edin: '))
##choice = input('secim edin: ')
##if choice == '1':
##    print(topla(n))
##elif choice == '2':
##    print(vur(n))
##else:
##    exit()

#14
def avtomorf(a):
    a2 = a ** 2
    s = 0
    i = 1
    while a2 > 0:
        k = a2 % 10
        a2 = a2 // 10
        s = s  + k * i
        i = i * 10
        if s == a:
            return s
N = int(input())
i = 1
while i <= N:
    if i == avtomorf(i):
        print(i)
    i+=1
    


#15
##N = int(input())
##i = 1
##while i <= N:
##    copy = i
##    result = True
##    while copy > 0:
##        k = copy % 10
##        if k == 0 or i % k != 0:
##            result = False
##            break
##        copy = copy // 10
##    if result == True:
##        print(i)
##    i += 1


    







    


