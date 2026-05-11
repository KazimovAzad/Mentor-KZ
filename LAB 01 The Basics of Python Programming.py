#1
##a = 2 ** 4
##print(f'{a} = {2} ** {4}')

#2
##a = float(input('en: '))
##b = float(input('uzunluq: '))
##s = a * b
##print(f'{s} = {a} * {b}')

#3
##a = float(input('en: '))
##b = float(input('uzunluq: '))
##c = float(input('hundurluk: '))
##SS = 2 * (a*b + a*c + b*c)
##print(f'{V} = {a} * {b} * {c}', 'sethin sahesi: ', SS)

#4
##import math
##r = float(input('radius: '))
##h = float(input('hundurluk: '))
##S = math.pi * r**2 * h
##print(S)

#5
##import math
##a = float(input('1ci teref: '))
##b = float(input('2ci teref: '))
##y = float(input('arasindaki bucaq: '))
##S = round(1/2 * a * b * (math.sin( math.pi * y / 180)), 2)
##S2 = round(1/2 * a * b * (math.sin(math.radians( y))), 2)
##print(S,S2)

#6
##a = float(input('1ci teref: '))
##b = float(input('2ci teref: '))
##y = float(input('arasindaki bucaq: '))
##s = a+b+c
##print(s, a*b*c, s/3)

#7
##import random
##a = random.randint(1000,9999)
##s = 0
##f = 1
##while a > 0:
##    i = a %10
##    a = a //10 
##    s += i**2
##    f *= i
##print('eded', a, 'cem:', s,'hasil', f)

#8
##import random
##a = random.uniform(6.5,10.5)
##b = random.uniform(6.5,10.5)
##f = round(a * b, 2)
##print(a,b,f)

#9
##import random
##a = random.randint(10000,99999)
##print('random eded:',a)
##while a > 0:
##    k = a % 10
##    print(k, k **2)
##    a = a // 10

#10
##import math
##import random
##x = random.uniform(-1 , 1)
##y = random.uniform(-1 , 1)
##a = round(math.sqrt(1 + y**2) * math.sin(x**2/(1 + abs(y))), 3)
##b = round(math.cos(math.sin(5*x)*2/math.sqrt(abs(y))), 3)
##print(a, b)

#11
##a = int(input())
##a1 = a // 100
##a2 = (a % 100)//10
##a3 = a % 10
##print(a1, a2, a3, sep = ', ')






