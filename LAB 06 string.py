#2
##a = input()
##s = ''
##for i in a:
##    if i == 'a':
##        s += 'b'
##    elif i == 'A':
##        s += 'B'
##    elif i == 'b':
##        s += 'a'
##    elif i == 'B':
##        s += 'A'
##    else:
##        s += i
##print(s)

#3
##def lenn(a):
##    s = 0
##    for i in a:
##        s += 1
##    return s
##a = input()
##s = 0
##for i in range(1, lenn(a)):
##    if a[i - 1] == " " and a[i] != " ":
##        s += 1
##if a[0] != " ":
##    s += 1
##print(s)

#4
##a = input()
##count = 0 
##maxx = 0
##soz = "" 
##son = ""
##for i in a:
##    if i != " ":
##        soz += i
##        count += 1
##    else:
##        if maxx < count:
##            maxx = count
##            son = soz
##        soz = ""
##        count = 0
##    if soz != "":
##        if maxx < count:
##            maxx = count
##            son = soz
##print(son, maxx)

#5
##a = input()
##son = ''
##soyad = ''
##k = 0
##while a[k] != ' ':
##    soyad += a[k]
##    k += 1
##while a[k] == ' ':
##    k += 1
##son += a[k] + '.'
##while a[k] == ' ':
##    k += 1
##son += a[k] + '.'
##print(son + soyad)

#6 c:/azad/oktay/nihad.jpg
##a = input()
##k = -1
##for i in range(len(a)):
##    if a[i] == '/':
##        print(a[k + 1:i])
##        k = i
##print(a[k + 1:])

#7
##def lenn(z):
##    s = 0
##    for i in z:
##        s += 1
##    return s
##
##a = input('setir:')
##x = input('neyi:')
##y = input('ne ile:')
##son = ''
##i = 0
##while i < lenn(a):
##    if a[i : i + lenn(x)] == x:
##        son += y
##        i += lenn(x)
##    else:
##        son += a[i]
##    i += 1
##print(son)

#8
##def lenn(z):
##    s = 0
##    for i in z:
##        s += 1
##    return s
##
##a = input('setir:')
##x = input('axtarilan:')
##count = 0
##for i in range(lenn(a)):
##    if a[i : i + lenn(x)] == x:
##        count += 1
##print(count)

#9
##a = 'Bayram günü gələcəyik sizə bayramlaşmağa. Bayramlaşsaz da bayramlaşacağıq. Bayramlaşmasanız da bayramlaşacağıq.'
##count = 0
##son = ''
##for i in range(len(a)):
##    if a[i : i + len('bayram')] == 'bayram':
##        son += 'novruz'
##        count += 1
##        i += len('bayram')
##    else:
##        son += a[i]
##print(son, 'deyisen soz sayi:',count)

#10 9un eynisidi ozunuz baxmadan isleyin

#11
##a = input()
##k = 1 #(her sozun reqemlemesi 1den baslayir)
##son = ''
##for i in a:
##    if i != ' ':
##        if k == 2: #sozun 2ci herfi
##            k += 1
##            continue
##        else:
##            k += 1
##    else:
##        k = 1 #boslugu goren kimi sifirlayir
##    son += i
##print(son)

#12 
##a = input()
##verilen='AOUEbcmf3579!?,;'
##son = ''
##for i in a:
##    if i in verilen and i not in son: #eger setirde 2 A varsa biri cixmalidi ona gore 2ci serti veririk
##        son += i
##print(son, ' simvollari var')

###13
##a = input()
##s = 0
##t = ''
##for i in a:
##    if i == '+':
##        s += int(t)
##        t = ''
##    else:
##        t += i
##s += int(t)
##print(s)

#14
##a = input()
##s = 0
##t = ''
##isare = '+'
##for i in a:
##    elif i == '+' or i == '-':
##        if isare == '+':
##            s += int(t)
##        else:
##            s -= int(t)
##        isare = i
##        t = ''
##    else:
##        t += i
##if isare == '+':
##    s += int(t)
##else:
##    s -= int(t)
##print(s)

#14

#15 defle
##def ilk(z):
##    s = ''
##    for i in z:
##        if i != ' ':
##            s += i
##        else:
##            return s
##a = input()
##print(ilk(a))
##
#defsiz
##a = input()
##s = ''
##for i in a:
##    if i != ' ':
##        s += i
##    else:
##        break
##print(s)

#16 nihad.azad.oktay.jpg
##def countt(a): #ifadede olan . sayini tapan funksiya
##    count = 0
##    for i in a:
##        if i == '.':
##            count += 1
##    return count
##
##a = input('fayl adi:')
##x = input('yeni genislenme:')
##son = ''
##t = 0 #necenci . oldugu
##count = countt(a) #. sayi
##for i in a:
##    if i == '.':
##        t += 1
##        if t == count:
##            son = son + '.' + x
##            break
##    son += i
##print(son)

#17






























