#119 1 daha rahat
##a = input()
##ince = 'eiöü'
##s = 0
##for i in a:
##    if i in ince:
##        s += 1
##print(s)

#119 2 bele de olar
##a = input()
##s = 0
##for i in a:
##    if i == 'e' or i == 'i' or i == 'ö' or i == 'ü':
##        s += 1
##print(s)

#121 lab6da 4cu sual tiplidi
##a = input()
##ince = 'eiöü'
##soz = ''
##son = ''
##count = 0
##maxx = 0 
##for i in a:
##    if i != ' ':
##        soz += i
##        if i in ince:
##            count += 1
##    else:
##        if count > maxx:
##            maxx = count
##            son = soz
##        soz = ''
##        count = 0
##    if count > maxx:
##        maxx = count
##        son = soz
##print(son)


#123 lab6da 3cu sualla bosluq temalarina gore ferqlenir(burda az sert qoyub)
##a = input()
##count = 1    #dovrde ilk soze baxmayaciq deye 1-le baslayiriq 
##for i in a:
##    if i == ' ':
##        count += 1
##print(count)

#defle
##def soz_sayi(a):
##    count = 1
##    for i in a:
##        if i == ' ':
##            count += 1
##    return count
##a = input()
##print(soz_sayi(a))

#125
##a = input()
##reqem = '0123456789'
##choose = ''
##for i in a:  #i her bir simvolu alir
##    if i in reqem:  # o simvol reqemdise bir bir secir, atir choose-a
##        choose += i
##print(choose)

#126
##def bosluqsuz(a):
##    s = ''
##    for i in a:
##        if i != ' ': #bosluq deyilse simvolu elave ele
##            s += i
##    return s
##a = input()
##print(bosluqsuz(a))

#127 
##def lenn(z):
##    s = 0
##    for i in z:
##        s += 1
##    return s
##a = input('metn:')
##b = input('metn fraqmenti:')
##for i in range(lenn(a)-lenn(b)+1):
###    print(a[i : i + lenn(b)]) #bunu cixanlarin ne oldugunu goresiz deye yazmisam 
##    if a[i:i + lenn(b)] == b:
##        print('var')
##        break
##else:
##    print('yoxdu')

#129 oktay nihad azad
##a = input()
##son = ''
##k = 0 # sozun ilk herfi olub olmadigi ucundu(eger 0disa ilkdi, 1dise deyil)
##for i in a:
##    if i != ' ':
##        if k != 0:
##            son += i
##        else:
##            k = 1
##    else:
##        son += ' '
##        k = 0
##print(son)

#132 nihadoktayazad
##a = input()
##son = ''
##count = 1
##for i in a:
##    if count % 5 == 0: #her 5simvolu(5,10,15..) 5e qaliqsiz bolunurde
##        son += i
##        son += ','
##    else:
##        son += i
##    count += 1
##if son[-1] == ',': #sonuncu simvol ,duse
##    print(son[:-1]+'.') #ona qeder olan simvollari topluyur ustune . gelir
##else:
##    print(son+'.') #deyilse sadece ustune . gelir

#135 lab6 4cu sual tipli
##S = input()
##soz = ''
##son = ''
##count = 0
##maxx = 0
##for i in S:
##    if i != ' ':
##        soz += i
##        if i == 'a':
##            count += 1
##    else:
##        if count > maxx:
##            maxx = count
##            son = soz
##        soz = ''
##        count = 0
##    if count > maxx:
##        maxx = count
##        son = soz
##print(son)

#136
##def lenn(a):
##    s = 0
##    for i in a:
##        s += 1
##    return s
##a = input()
##if lenn(a) % 2 ==0:
##    print(a[lenn(a)//2 - 1:lenn(a)//2+1]) #azad[za]azad 4cu indeksi z(10//2-1), 5ci indeksi a (10//2)
## else:
##    print(a[lenn(a)//2]) #ni[h]ad 3cu indeksi h(5//2+1)

#137 
##a = input()
##count = 0
##maxx = 0
##minn = len(a)
##soz = ''
##son_max = ''
##son_min = ''
##for i in a:
##    if i != ' ':
##        count += 1
##        soz += i
##    else:
##        if count > maxx:
##            maxx = count
##            son_max = soz
##        if count < minn:
##            minn = count
##            son_min = soz
##        soz = ''
##        count = 0
##if count > maxx:
##    maxx = count
##    son_max = soz
##if count < minn:
##    minn = count
##    son_min = soz
##print('max:', son_max,'min:', son_min)

#138
##a = input()
##count = 0
##for i in a + ' ':
##    if i != ' ':
##        count += 1
##    else:
##        print(count)
##        count = 0

#139 continuesuz
##a = input()
##son = ''
##for i in a:
##    if i not in son:
##        son += i
##print(son)

#continue ile(sertde deyir)
##a = input()
##son = ''
##for i in a:
##    if i in son:
##        continue
##    else:
##        son += i
##print(son)

#140
##a = input()
##s = 0
##for i in a:
##    if i != ' ':
##        s += 1
##print(s)

#defle
##def say(a):
##    s = 0
##    for i in a:
##        if i != ' ':
##            s += 1
##    return s
##a = input()
##print(say(a))




























    
