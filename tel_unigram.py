#!/usr/bin/python3

import sys
import math
from collections import Counter
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QLabel



class wordFreqUI(QtGui.QWidget):
    def __init__(self):
        super(wordFreqUI,self).__init__()
        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        words = main(sys.argv)
        count = 1
        for (i,j) in words:
            self.lbl = QtGui.QLabel(i,self)
            self.lvl = QtGui.QLabel(str(j),self)
            self.lbl = self.lbl.move(50, count*12)
            self.lvl = self.lvl.move(250,count*12)
            count = count + 1
        
              
        self.setGeometry(450,450,400,300)
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
        return(c.most_common(20))

    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    word = wordFreqUI()
    sys.exit(app.exec_())
   
