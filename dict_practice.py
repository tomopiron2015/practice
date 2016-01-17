#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist = []

print "--empty list--"
print mylist


mylist.append("no1")
mylist.append("no2")
mylist.append("no3")

print "--insert valu.--"
print mylist

print "--for loop--"

for loop in mylist:
    print loop


print "--insert valu--"
mylist.insert(1,"in1")
mylist.insert(3,"in2")
mylist.insert(5,"no4")

print mylist

for loop in mylist:
    print loop

print "--dict--"

mydic = {'1':'takeharu', '2':'eisuke', '3':'iroha'}
print mydic

print "--for loop--"

for dict in mydic:
    print dict
    print mydic[dict]

print "--print valu--"

print mydic.get('1')
print mydic.get('2')
print mydic.get('3')


print "--set empty dict--"

mydic2 = {}

print "empty dict"
print mydic2

print "--set valu--"
mydic2[1] = "takeharu"
mydic2[2] = "eisuke"
mydic2[3] = "iroha"

print mydic2

print "--for dict--"
for dict in mydic2:
    print mydic2.get(dict)

print "--del from dict--"

mydic3 = {1: 'takeharu', 2: 'eisuke', 3: 'iroha'}
print mydic3

print "--delete exec--"

print mydic3

del mydic3[2]
print mydic3

del mydic3[3]
print mydic3

del mydic3[1]
print mydic3


print "--dictkey to list--"
mydic4 = {1: 'takeharu', 2: 'eisuke', 3: 'iroha'}

print mydic4

print "---list key---"
print mydic4.keys()

print "---list valu---"
print mydic4.values()

print "--list kye&valu--"
print mydic4.items()

