__author__ = 'kw@cloudera.com'
import time
import sys
import datetime
import random

if len(sys.argv) < 2:
    sys.stderr.write('Usage: randomFileGen.py /mydir/ .extension nStart nEnd')
    sys.exit(1)

print('#' * 14 + ' Your Command Arguments ' + '#' * 14)
print "\n".join(sys.argv)
print('#' * 52)

print ('Start Time - ' + time.strftime("%d/%m/%Y %H:%M:%S"))

for x in range(int(sys.argv[3]), int(sys.argv[4])):
    with open(str(sys.argv[1]) + str(x) + '.' + str(sys.argv[2]), 'w+') as f:
        f.write(str(x + 1) + ',' + str(random.randrange(10000)) + ',' + str(datetime.datetime.now()) + '\n')
        f.close()