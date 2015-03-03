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
        self.btn = QtGui.QPushButton("Click to enter filename", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        uni = QtGui.QCheckBox("Unigrams", self)
        uni.move(20, 60)
        uni.toggle()
        # zorgen dat unigram checkbox herkent wordt
        # en daadwerkelijk 20 meest frequente unigrammen geeft
        bi = QtGui.QCheckBox("Bigrams", self)
        bi.move(150, 60)
        bi.toggle()
        # zorgen dat bigram checkbox herkent wordt
        # en daadwerkelijk 20 meest frequente bigrammen geeft

        self.setGeometry(450, 450, 400, 300)
        self.setWindowTitle("N-gram")
        self.show()
        
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, "N-gram", "Enter filename:")
        if ok:
            self.le = QtGui.QLineEdit(self)
            self.le.move(130, 22)
            self.le.setText(str(text))
        # zorgen dat het ingevoerde bestand meegegeven wordt aan de
        # main functie waar het geopend kan worden en de n grammen
        # berekend kunnen worden


    def unigram(self):
        #moet nog aangepast worden
        words = main(sys.argv)
        count = 1
        for (i,j) in words:
            self.lbl = QtGui.QLabel(i,self)
            self.lvl = QtGui.QLabel(str(j),self)
            self.lbl = self.lbl.move(50, count*12)
            self.lvl = self.lvl.move(250,count*12)
            count = count + 1

    def bigram(self):
        #moet nog aangepast worden
        words = main(sys.argv)
        count = 1
        for (i,j) in words:
            self.lbl = QtGui.QLabel(i,self)
            self.lvl = QtGui.QLabel(str(j),self)
            self.lbl = self.lbl.move(50, count*12)
            self.lvl = self.lvl.move(250,count*12)
            count = count + 1


def main(argv):
    if len(argv) == 2:
        infile = open(argv[1])
        # tekstbestand wordt hier meegegeven
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
   
