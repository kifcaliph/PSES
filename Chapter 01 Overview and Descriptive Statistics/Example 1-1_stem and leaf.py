from collections import namedtuple
from pprint import pprint as pp
from math import floor
 
Stem = namedtuple('Stem', 'data, leafdigits')
 
data0 = Stem((6.1, 12.6, 34.7, 1.6, 18.8, 2.2, 3, 2.2, 5.6, 3.8,
              2.2, 3.1, 1.3, 1.1, 14.1, 4, 21, 6.1, 1.3, 20.4,
              7.5, 3.9, 10.1, 8.1, 19.5, 5.2, 12, 15.8, 10.4, 5.2,
              6.4, 10.8, 83.1, 3.6, 6.2, 6.3, 16.3, 12.7, 1.3, 0.8,
              8.8, 5.1, 3.7, 26.3, 6, 48, 8.2, 11.7, 7.2, 3.9, 15.3,
              16.6, 8.8, 12, 4.7, 14.7, 6.4, 17, 2.5, 16.2),
              1.0)
 
def stemplot(stem):
    d = []
    interval = int(10**int(stem.leafdigits))
    for data in sorted(stem.data):
        data = int(floor(data))
        stm, lf = divmod(data,interval)
        d.append( (int(stm), int(lf)) )
    stems, leafs = list(zip(*d))
    stemwidth = max(len(str(x)) for x in stems)
    leafwidth = max(len(str(x)) for x in leafs)
    laststem, out = min(stems) - 1, []
    for s,l in d:
        while laststem < s:
            laststem += 1
            out.append('\n%*i |' % ( stemwidth, laststem))
        out.append(' %0*i' % (leafwidth, l))
    out.append('\n\nKey:\n Stem multiplier: %i\n X | Y  =>  %i*X+Y\n'
               % (interval, interval))
    return ''.join(out)

if __name__ == '__main__':
    print( stemplot(data0) )
