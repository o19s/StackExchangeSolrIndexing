import re
import sys

if  len(sys.argv) !=  2 :
    raise Exception("This script excepts a single argument. The StackExchange file.")

fileName = sys.argv[1]

kvRe = '(\w+)="(.*?)"'

f = open(fileName)
f.readline()
f.readline()
print "<add>"
for i, line in enumerate(f):
    if line == "</posts>" :
        continue
    print "<doc>"
    for field in re.findall(kvRe, line):
        key = field[0]
        value = field[1]
        if (key == "Body" or key == "Title" ) :
            value = re.sub("&lt;/?.+?&gt;|&[^q][#\w]+;"," ",value)
        elif key == "Tags" :
            value = re.sub("&#?\w+;"," ",value)
        elif (key == "CreationDate" or key == "LastActivityDate" or key == "LastEditDate" ) :
            value = value + "Z"

        if len(value) == 0 :
            continue
        print '<field name="%s">%s</field>' % (key, value )
    print "</doc>"
    if i > 1000000 :
        break;
print "</add>"
