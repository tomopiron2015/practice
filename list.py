#!/usr/bin/python
# -*- coding: utf-8 -*-

test_list_1 = ['python','ruby','java','sql']
print test_list_1

print "---1---"
for i in test_list_1:
    print i

for i in test_list_1:
    print test_list_1.index(i)

print test_list_1.index('sql'),test_list_1.index('java'),test_list_1.index('ruby'),test_list_1.index('python')

# Add to List
test_list_2 = []

print "---2---"
print test_list_2

test_list_2.append('python')
test_list_2.append('ruby')
test_list_2.append('java')
test_list_2.append('sql')

print test_list_2

# Add to list with index

test_list_3 = ['python', 'ruby', 'java', 'sql']
print "---3---"
print test_list_3

print "--add index--"

test_list_3.insert(1,'-')
test_list_3.insert(3,'-')
test_list_3.insert(5,'-')

print test_list_3


# Delete value

test_list_4 = ['python', 'ruby', 'java', 'sql']

print "---4---"
print test_list_4

test_list_4.remove("java")

print "--remove java--"
print test_list_4


# Delete value by inex

test_list_5 = ['python', 'ruby', 'java', 'sql']

print "---5---"
print test_list_5

print "--remove index val--"

print test_list_5.pop(2)
print test_list_5


# Get index val

test_list_6 =  ['python', 'ruby', 'java', 'sql']

print "---6---"
print test_list_6

print "--get index val--"

print test_list_6.index('python')
print test_list_6.index('ruby')
print test_list_6.index('java')
print test_list_6.index('sql')

# Count list value

test_list_7 =  ['python', 'ruby', 'java', 'sql', 'python', 'ruby', 'python']

print "---7---"
print test_list_7

print "--count val--"

for i in range(test_list_7.count('python')):
    test_list_7.count('python')
    print test_list_7

    test_list_7.remove('python')

print test_list_7
