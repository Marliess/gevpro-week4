#!/usr/bin/python3

import sys
from collections import Counter
from PyQt4 import QtGui, QtCore



class wordFreqUI(QtGui.QWidget):
    def __init__(self):
        super(wordFreqUI,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Word frequencies")
        self.show()



        

def main(argv):
    if len(argv) == 2:
        infile = open(argv[1])
        c = Counter()
        for line in infile:
            #line = line.lower()
            ws = line.split()
            c.update(ws)
        print(c.most_common(20))

        app = QtGui.QApplication(sys.argv)
        word = wordFreqUI()
        sys.exit(app.exec_())

    
if __name__ == "__main__":
    main(sys.argv)
