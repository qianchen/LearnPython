#print 'hello, world!'
#print 'the quick brown fox', 'jumps over', 'the lazy dog'
#print '100+200 =', 100+200 
#name = raw_input("please enter your name: ")
#print 'hello', name

#print absolute value of an integer:
#a = 100
#if a>=0:
#    print a 
#else:
#    print -a

#print 'I\'m ok.'
#print 'I\'m learning\t python.'
#print '\\\n\\'
#print r'\\\n\\'
#print '''line1
#line2
#line3'''

#if True and False:
#    print "qian"
#else:
#    print "ting"
#
#a = 123 #a is an integer
#print a
#a = "abc" #a is a string
#print a

#print ord('A')
#print chr(65)
#print u'\u4e2d'

#print "hello, %s" % 'world'
#print "%2d-%02d" % (3,1)
#print "%.2f" % 3.1415926
#print "Age: %s.Gender: %s" % (25, True)
#print "%s %%" % '3'
#print "%d %%" % 3
#print b"abc"

#classmates = ['qian', 'ting']
#print classmates
#print len(classmates)
#print classmates[-1]
#print classmates[-2]
#classmates.append('father')
#classmates.insert(1, 'mother')
#print classmates
#print "pop():"
#classmates.pop()
#print classmates

#python = []
#print len(python)
#ruby = ['hello', 'world']
#python = ['hello', 123, ruby, False]
#print python[2][1]
#
#Ruby = ('hello', 'world', python)
#print Ruby
#Ruby[2][2][0] = 'die'
#print Ruby

#sum = 0
#for i in range(101):
#    sum = sum + i
#print sum
#
#sum = 0
#n = 99
#while n > 0:
#    sum += n
#    n -= 2
#print sum
#
#sum = 0
#bMark = False
#if sum > 100:
#    bMark = False
#elif sum > 0:
#    bMark = False
#else:
#    bMark = True
#
#if bMark == True:
#    print "sum is no meaning"


#dict and set
#name = {'jack': 1, 'hellen': 2, 'jack': 3}
#print name.get('jack')
#
#year1 = set([1,2,4])
#print year1
#year2 = set([1,3])
#print year2
#print year1 & year2
#print year1 | year2


#Function
#print "Compare 1 to 3"
#print cmp(1, 3)
#print "The integer of 3.1"
#print int(3.1)
#a = int
#print a(3.1)
#def my_abs(x):
#    if x>= 0:
#        pass
#    else:
#        return -x
#
#print my_abs(1)
#def Test(a = []):
#    print a
#    a.append('End')
#    return a
#
#print Test()
#print Test()
#def Fina(*numb):
#    sum = 0
#    for n in numb:
#        sum += n*n
#    return sum
#
#print "1*1 + 2*2 + 3*3="
#print Fina(1,2,3)
#def Ma(**numb):
#    print numb
#numb = {'he': 1, 'she': 2}
#Ma(**numb)
#def AllParm(a,b,c=0,*tu,**di):
#    print 'a =', a, 'b =', b, 'c =', c, 'tu =', tu, 'di =', di
#
#AllParm(1,2,3,'a','b',A=10)
#def DiGui(numb):
#    return TailAcc(numb, 1)
#
#def TailAcc(numb, accumu):
#    if numb == 1:
#        return accumu
#    return TailAcc(numb - 1, numb * accumu)
#
#print "5!="
#print DiGui(5)


#Advance behavior
#L = [1,2,3,4,5,6,7]
#print L[:4:2] 
#for i,value in enumerate([1,2,3,4]):
#    print i,value
#import os
#print [d for d in os.listdir('.')]
#d = {'A': 1, 'B': 2}
#print [key + '=' + 'value' for key, value in d.iteritems()]
#L = ['Hello', 'World', 18, 'Apple', None]
#K = [s.lower() for s in L if isinstance(s, str)]
#print K
