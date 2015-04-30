# This used to conduct pre-install checks on target cluster nodes
# Kevin Worrell - kw@cloudera.com - 02-08-2014
#
# TODO(kw@cloudera.com): Add a condition to allow for writing a shell script of actually executing with python

__author__ = 'kworrell'
import commands
import sys

if len(sys.argv) < 1:
    sys.stderr.write('Usage: python preCheck.py myConfigFile')
    sys.exit(1)

dictlabels = {}
dictlabels['a'] = 'Information Checks'
dictlabels['d'] = 'Disk Config Checks'
dictlabels['n'] = 'Network Config Checks'
dictlabels['g'] = 'General Config Checks'
dictlabels['k'] = 'Kernel Setting Checks'

cmdoutput = []
badoutput = []

# TODO(kw@cloudera.com): Add sys.argv functionality and remove hardcoded file name
with open(str(sys.argv[1]), 'rt') as fchecks:
    for line in fchecks:
        # myline = line.split(sep='~')
        myline = line.split('~')
        # TODO(kw@cloudera.com): place types in a dict and use dict.items()
        if myline[0].strip() in ['a','k','d','g','n']:
            # mycommand = subprocess.getoutput(myline[2].strip())
            mycommand = commands.getoutput(myline[2].strip())
            if myline[0].strip() in ['a']:
                cmdoutput.append((myline[0].strip(), myline[1].strip(), mycommand.strip()))
            elif myline[0].strip() in ['d','n','g','k']:
                cmdoutput.append((myline[0].strip(), myline[1].strip(), mycommand.strip(),myline[3].strip(), myline[2].strip()))


prev = ''
print('\n' + '#'*14 + '\n# Check for: #\n' + '#'*14 + '\n \n' + 'X'*5 + ' = Failed Check \nINVALID COMMAND = is a malformed linux command \n\m/ = Command passed')
#cmdoutput.sort()
for i, e in enumerate(cmdoutput):
    if e[0].strip() != prev:
        print('\n' + '#'*40 + ' ' + dictlabels[e[0].strip()] + ' ' + '#'*40)
    if e[0].strip() == 'a':
        print ('%03d) %s' % (i, '{0:<25} [ {1:>1} ]'.format(e[1],e[2].strip())))
    if e[0].strip() in ['d','n','g','k']:
        if e[2].strip() == 'passed':
            print ('%03d) %s' % (i, '\m/ ---> : {0:<25} [ {1:>1} ]'.format(e[1],e[2].strip())))
        if e[2].strip() == 'failed':
            print ('%03d) %s' % (i, 'X'*5 + ' ---> : {0:<25} [ {1:^1} ] {2:>1}'.format(e[1],e[2].strip(),e[3].strip())))
            badoutput.append(('FAILED:', e[1].strip(), e[4].strip(), e[2].strip(), e[3].strip()))
        elif e[2].strip() not in ['failed', 'passed']:
            badoutput.append(('INVALID:', e[1].strip(), e[4].strip(), e[2].strip(), e[3].strip()))
    prev = e[0].strip()

print('\n' + '_'*40 + ' INVALID COMMANDS / FAILED TESTS ' + '_'*40 + '\n')
for i, e in enumerate(badoutput):
    print ('|' + '%03d) %s' % (i, '{0:<1} {1:<45} ---> "{2:>1}"'.format(e[0], e[1], e[2])))
print('_'*(' INVALID COMMANDS / FAILED TESTS '.__len__() + 80))