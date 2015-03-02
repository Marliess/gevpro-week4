#!/usr/bin/python3

import sys
from collections import Counter
#from PyQt4 import QtGui

def main(argv):
    if len(argv) == 2:
        infile = open(argv[1])
        c = Counter()
        for line in infile:
            #line = line.lower()
            ws = line.split()
            c.update(ws)
        print(c.most_common(20))

    
if __name__ == "__main__":
    main(sys.argv)
