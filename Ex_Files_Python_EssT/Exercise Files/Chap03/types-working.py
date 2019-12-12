# !/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 'seven "{1:<09}" "{0:>09}"'.format(8,123459)
y = 'seven {} {}'.format(8,9)

a = 8
b = 9
z = f'seven {a:<09} {b:>09}'
print('z is {}'.format(z))
print(type(z))


from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x1 = a + a + a - b
# x1 = .1 + .1 + .1 - .3
print ('x1 is {}'.format(x1))
print(type(x1))



x2 = 1
print ('x2 is {}'.format(x2))
print(type(x2))

if x2:
    print('True')
else:
    print('False')