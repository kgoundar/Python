# !/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ] # can reassign values
x[2] = 42

y = (1, 2, 3, 4, 5) # cannot reassign values later

z = range(5)

a = range(5, 10, 2) # cannot reassign values later

c = list(range(5))
c[2] = 35

d = { 'one': 1 'two':2, 'three': 3, 'four'}

for i in x:
    print('i is {}'.format(i))

for j in y:
    print('j is {}'.format(j))

for k in z:
    print('k is {}'.format(k))

for l in a:
    print('l is {}'.format(l))

for m in c:
    print('m is {}'.format(m))