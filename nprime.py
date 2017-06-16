#!/usr/bin/python
"""
@author: Yijia Zhang

find the nth prime number.

the 1234567-th prime number is: 19394489
finished in 6 seconds.

the 12345678-th prime number is: 224284387
finished in 75 seconds.

This is the development version.
"""
n = 12345

import math
import time

start = time.time()

def onebyone(n):
    prime = [2]
    i = 3
    number = 1
    while number != n:
        sqi = math.sqrt(i)
        for j in prime:
            if j<i and i%j == 0:
                i = i + 1
                break
            elif j > sqi:
                prime.append(i)
                number = number + 1
                i = i + 1
                break
            else:
                continue
                
    return prime[-1]

def thieve(n):
    '''
    n should be no less than 6.
    much fast than onebyone(), but use much more memory.
    The largest achievable n is 12345678 limited by memory.
    
    excluding even number also accelerate a lot.
    '''
    # initialization.
    uplimit = int( n*( math.log(n) + math.log( math.log(n) ) ) )
    sqr = int( math.sqrt(uplimit) )
    numbers = {}# mark for each number whether it is excluded.
    numbers[2] = True# tiny improvement from int.
    for i in range(3, uplimit+1, 2):
        numbers[i] = True
    
    # thieve.
    thieveTool = 3
    while thieveTool <= sqr:
        for i in range(3*thieveTool, uplimit+1, 2*thieveTool):
            #if numbers[i] != 0: # this judgement makes things worse.
            numbers[i] = False
        # get the next thieveTool.
        k = thieveTool + 2
        while not numbers[k]:
            k = k + 2
        thieveTool = k
    
    # count to the nth prime.
    count = 1
    i = 3
    while count != n:
        if numbers[i]:
            count = count + 1
        i = i + 2
    return i - 2

def thieveImpr(n):
    '''
    n should be no less than 6.
    do 2, 3 manually. but not faster than thieve(). reduced memory from 10G to 6G.
    '''
    # initialization.
    uplimit = int( n*( math.log(n) + math.log( math.log(n) ) ) )
    sqr = int( math.sqrt(uplimit) )
    numbers = {}# mark for each number whether it is excluded.
    numbers[2] = True# tiny improvement from int.
    numbers[3] = True
    for i in range(5, uplimit+1, 6):
        numbers[i] = True
    for i in range(7, uplimit+1, 6):
        numbers[i] = True
    
    # thieve.
    thieveTool = 5
    while thieveTool <= sqr:
        for i in range(5*thieveTool, uplimit+1, 6*thieveTool):
            numbers[i] = False
        for i in range(7*thieveTool, uplimit+1, 6*thieveTool):
            numbers[i] = False
        # get the next thieveTool.
        k = thieveTool + 2
        while k not in numbers.keys() or not numbers[k]:
            k = k + 2
        thieveTool = k
    
    # count to the nth prime.
    count = 2
    i = 5
    while count != n:
        if i in numbers.keys() and numbers[i]:
            count = count + 1
        i = i + 2
    return i - 2

print('start...')
    
nth = thieveImpr(n)
print('the %d-th prime number is: %d' % (n, nth) )

duration = time.time()-start
print('finished in %s seconds.' % round(duration) )
