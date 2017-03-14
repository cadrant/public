from operator import itemgetter

def mode(L):
    freq = {}
    most_freq = 0
    freq[most_freq] = -1
    # your code here
    for n in L:
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] = freq[n] + 1
            print "hey", n
            if freq[n] >= freq[most_freq]:
                print n
                most_freq = n
    print most_freq
    print freq
    return most_freq

####
# Test
#
import time
from random import randint

def my_test():
    print mode ([2, 4, 7, 2, 6, 9, 2, 3, 1, 8, 4, 6, 7, 1, 5, 6, 8, 4, 6, 6, 1, 2, 2, 7, 5, 3, 4, 7, 5, 3, 4, 2, 1, 8, 3, 3, 5, 4, 3, 5, 2, 10, 6, 3, 3, 5, 5, 6, 3, 4])


def there_test():
    assert 5 == mode([1, 5, 2, 5, 3, 5])
    mode ([2, 4, 7, 2, 6, 9, 2, 3, 1, 8, 4, 6, 7, 1, 5, 6, 8, 4, 6, 6, 1, 2, 2, 7, 5, 3, 4, 7, 5, 3, 4, 2, 1, 8, 3, 3, 5, 4, 3, 5, 2, 10, 6, 3, 3, 5, 5, 6, 3, 4])
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for j in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for j in range(500):
            mode(L)
        end = time.clock()
        print start, end
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print (x1, x2), (y1, y2)
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time, 
    # these factors should be close (kind of)
    print slopes

my_test()
