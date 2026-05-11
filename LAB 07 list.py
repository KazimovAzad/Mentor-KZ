##random ededler daxil olunur
##import random
##n = int(input()) #nece eded lazimdi
##a = [random.randint(0,100) for i in range(n)]
##ededleri ozun daxil eleyirsen(bosluq qoyaraq)
##b = [int(x) for x in input().split()]

#3
##list1 = [int(x) for x in input().split()]
##list2 = []
##for i in list1:
##    list2 += [i + 5]
##print(list2)

#4
##list1 = [int(x) for x in input().split()]
##list2 = []
##for i in list1:
##    if i % 2 != 0:
##        list2 += [i]
##print(list2)

#5
##import random
##def lenn(a):
##    s = 0
##    for i in a:
##        s += 1
##    return s
##a = [random.randint(0,10) for x in range(3)]
##print(a)
##cem = 0
##hasil = 0
##say = 0
##maxx = float('-inf')
##minn = float('inf')
##for i in range(lenn(a)):
##    cem += a[i]
##    hasil *= a[i]
##    say += 1
##    if a[i] > maxx:
##        maxx = a[i]
##        maxxi = i
##    if a[i] < minn:
##        minn = a[i]
##        minni = i
##print('cem:', cem,'hasil:', hasil ,'ededi orta:', cem / say, 'max:', maxx, 'max indeksi:', maxxi,'min:', minn,'min indeksi:', minni, sep ='\n')

#6 asan
#7
##List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225] 
##print(List[:5], List[10:])    

#9
##a = [int(x) for x in input().split()]
##b = [int(x) for x in input().split()]
##s = 0
##for i in a:
##    for j in b:
##        if i == j:
##            s += 1
##if s != 0:
##    print('True')
##else:
##    print('False')

#10
##def lenn(a):
##    s = 0
##    for i in a:
##        s += 1
##    return s
##list1 = [int(x) for x in input().split()]
##list2 = [int(x) for x in input().split()]
##count = 0
##for i in range(lenn(list1)):
##    if list1[i] == list2[i]:
##        count += 1
##        print(list1[i])
##print('sayi:', count)

#11
##list1 = [int(x) for x in input().split()]
##list2 = []
##for i in range(1, len(list1)):
##    list2 += [list1[i]]
##list2 += [list1[0]]
##print(list2)

#12
##list1 = [x for x in input().split()]
##list2 = [x for x in input().split()]
##yeni_list = []
##for i in range(len(list1)):
##    yeni_list += [[list1[i],list2[i]]]
##print(yeni_list)

#13
##listt = [int(x) for x in input().split()]
##cem = 0
##i = 0
##while listt[i] % 2 == 1:
##    cem += listt[i]
##    i += 1
##print(cem)

#14
##import random
##n = int(input('listin olcusu:'))
##list1 = [random.randint(10,50) for x in range(n)]
##list2 = []
##for i in list1:
##    if i ** 0.5 == int(i ** 0.5): 
##        list2 += [i]
##print(list2)
##meselen
##a = 15.532
##b = 16
##print(int(a), int(b))

#15
##import random
##n = int(input())
##list1 = [random.randint(100,999) for x in range(n)]
##list2 =[]
##for i in list1:
##    k = i % 10
##    t = i // 10 % 10
##    if (k + t) % 2 == 1 and abs(k - t):
##        list2 += [i]
##print(list2)

#16
##def yoxla(a):
##    s = 0
##    for i in range(1, a + 1):
##        if a % i == 0:
##            s += 1
##    if s == 2:
##        return 'sade'
##    else:
##        return 'sade deyil'
##import random
##n = int(input())
##a = [random.randint(0,100) for x in range(n)]
##sadeler = []
##for i in a:
##    if yoxla(i) == 'sade':
##        sadeler += [i]
##print(sadeler)

#17
##import random
##a = [random.randint(-10, 10) for x in range(10)]
##son = []
##for i in a:
##    if i % 2 == 0 and i < 0:
##        son += [i]
##print(son)

#18 verdiyi list uzerinden eleyirik taski
##list1 = [1, 2, 'aasf', '1', '123', 123]
##son = []
##for i in list1:
##    if i * 0 == 0 and i >= 0:
##        son += [i]
##print(son)
#basa dusmek ucun
##print(f'{'abc'} * {0} = {'abc' * 0}', f'{'123'} * {0} = {'123' * 0}', f'{123} * {0} = {123 * 0}', sep = '\n')

#19
##a = int(input())
##List = []
##for i in range(1, a + 1):
##    if a % i == 0:
##        List += [i]
##print(List)

#20
N = [int(x) for x in range().split()]
List = []
for i in range(len(N)):
    s = 0
    for j in range(1, i + 1):
        t = (4 * sin(j) + 2 * j)/#log * 2 ** n
        s += t
        t = 0
    List += [s]
    






