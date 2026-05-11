##def faktorial(a):
##    hasil = 1
##    for i in range (1,a+1):
##        hasil *= i
##    return hasil    
##eded = int(input())
##eded2 = int(input())
##
##print(faktorial(eded))
##print(faktorial(eded2))


##def reqem_cemi(a):
##    cem = 0
##    while a>0:
##        b = a % 10
##        print(b)
##        cem += b
##        a = a // 10
##   
##    
##    return cem
##
##eded = int(input())
##print(reqem_cemi(eded))

##697
## 7 + 9 + 6 = 22



## 2 den 100 e qeder butun sade ededleri teyin edin


##def sade_eded(a):
##    count = 0
##    for i in range(1,a+1):
##        if a % i == 0 :
##            count += 1
##    if count == 2:
##        return True
##    else:
##        return False
##        

##for i in range(2,101):
##    if sade_eded(i) == True:
##        print(i)


##Task1
##(-1) daxil edilənədək əldə olunan natural ədədlərin cəminin cüt və ya tək olduğunu göstərən funksiya yazın. 
        
##def cem(a):
##    if a % 2 == 0:
##        return True
##    else:
##        return False
##n = int(input())
##s = 0
##while n!= -1:
##    s = s + n
##    n=int(input())
##if cem(s) == True:
##    print("he")
##else:
##    print("yox")



##def tek_cut(a):
##    if a % 2 == 0 :
##        return "cut"
##    else:
##        return "tek"
##def cem(a):
##    cem = 0
##    while eded != -1:
##        cem += eded
##        eded = int(input())
##    return cem
##
##
##eded = int(input())
####s = cem(eded)
####print(tek_cut(s))
##print(tek_cut(cem(eded)))
    
##
##eded = int(input())
##cem = 0
##while eded != -1:
##    cem += eded
##    eded = int(input())
##print(tek_cut(cem))



##Task 2

##def yoxla(a,b):
##    if (a/b) % 2 == 0:
##        return "cut"
##    else:
##        return "tek"
##    
##a = int(input())
##b = int(input())
##print(yoxla(a,b))


##Task 3

##def yoxla(n,k):
##    if k**k == n:
##        return True
##    else:
##        return False
##n = int(input())
##k = int(input())
##print(yoxla(n,k))

##Task 4

##def yoxla(a):
##    for i in range(1,a):
##        if i * (i+1) == a:
##            return "Pronic"
##    return "Heteromecic"
##
##p = int(input())
##print(yoxla(p))


##Task 5

##def uzunluq(a):
##    count = 0
##    while a > 0:
##        count += 1
##        a = a // 10
##    return count
##eded = int(input())
##tam_eded = abs(eded)
##print(uzunluq(tam_eded))


##Task 6

##def disarium(a):
##    count = 0
##    kopya = a
##    while a>0:
##        count += 1
##        a //= 10
##    cem = 0
##    while kopya > 0:
##        reqem = kopya % 10
##        cem += reqem ** count
##        count -= 1
##        kopya //= 10
##    return cem
##        
##    
##eded = int(input())
##if disarium(eded) == eded:
##    print("disariumdur")
##else:
##    print("disarium deyil")

##Task 7

##def curzon(a):
##    s = 2 ** a + 1
##    r = 2 * a + 1
##    if s % r == 0:
##        return "curzon"
##    else:
##        return "curzon deyil"
##n = int(input())
##print(curzon(n))


##Task 8

##def kempner(a):
##    kopya = a
##    count = 0
##    for i in range(1,a+1):
##        if a % i == 0:
##            count += 1
##    if count == 2:
##        return a
##    else:
##        f = 1
##        reqem = 1
##        while f % a != 0:
##            reqem += 1
##            f *= reqem
##        return reqem
##eded = int(input())
##print(kempner(eded))

##Task 9

##def moran(a):
##    cem = 0
##    kopya = a
##    while kopya > 0:
##        reqem = kopya % 10
##        cem += reqem
##        kopya //= 10
##    new = a // cem
##    count = 0
##    for i in range(1,new+1):
##        if new % i == 0:
##            count += 1
##    if count == 2:
##        return "Moran"
##    else:
##        return "Moran deyil"
##eded = int(input())
##print(moran(eded))

##Task 10

##def yoxla(a):
##    sonuncu = a % 10
##    while a > 0:
##        birinci = a % 10
##        a = a // 10
##    new = (birinci + sonuncu)**(1/2)
##    if new > 3:
##        return True
##    else:
##        return False
##eded = int(input())
##print(yoxla(eded))
        

##Task 11

##def qarsiliqli_sade(a,b):
##    count = 0
##    for i in range(1,a+1):
##        if a % i == 0 and b % i == 0:
##            count += 1
##    if count == 1:
##        return True
##    else:
##        return False
##eded1 = int(input())
##eded2 = int(input())
##print(qarsiliqli_sade(eded1,eded2))


##Task 13

##def ebob(a,b):
##    while a != b:
##        if a>b:
##            a = a - b
##        else:
##            b = b - a
##    return a
##def ekob(a,b):
##    ekob = a * b // ebob(a,b)
##    return ekob
##eded1 = int(input())
##eded2 = int(input())
##print(ebob(eded1,eded2))
##print(ekob(eded1,eded2))

##Ebob
##a =10
##b = 15
##b = b - a = 5
##a = a -b = 5


##Ekob
##a * b / ebob


##Task6

##def disarium(a):
##    kopya2 = a
##    kopya = a
##    count = 0
##    while kopya > 0:
##        count += 1
##        kopya //= 10
##    cem = 0
##    while a > 0:
##        reqem = a % 10
##        cem += reqem ** count
##        count -= 1
##        a //=10
##    if cem == kopya2:
##        return "disariumdur"
##    else:
##        return "disarium deyil"
##eded = int(input())
##print(disarium(eded))
        
        

    


##eded = int(input())
##kopya = abs(eded)
##min1 = kopya % 10
##max1 = kopya % 10
##while kopya > 0:
##    reqem = kopya % 10
##    if reqem >= max1:
##        max1 = reqem
##    elif reqem <= min1:
##        min1 = reqem
##    kopya //= 10
##if max1 != 9 and min1 != max1:
##    new = 900 + 10 *max1 + min1
##elif min1 == max1 and max1 != 9:
##    if min1 != 8:
##        new = 980 + min1
##    else:
##        new = 900 + 10 * min1 + 7
##elif max1 == 9:
##    if min1 != 8:
##        new = max1 + 80 + min1
##    else:
##        new = 900 + min1 + 7
##print(new)
##  

##81403
