#!/usr/bin/python3

import sys
from collections import Counter
from PyQt4 import QtGui, QtCore
#thanks to: http://pyqt.sourceforge.net/Docs/PyQt4/qlayout.html

class wordFreqUI(QtGui.QWidget):
    def __init__(self):
        super(wordFreqUI,self).__init__()
        self.initUI()

    def initUI(self):
        self.box = QtGui.QVBoxLayout()
        self.setLayout(self.box)
        self.combox = QtGui.QComboBox(self)
        self.combox.addItems(["Bigrams","Unigrams"])
        self.box.addWidget(self.combox)
        self.combox.currentIndexChanged["QString"].connect(self.eventHandler)
        self.button = QtGui.QPushButton("Choose a file", self)
        self.button.clicked.connect(self.updateUniBi)
        self.box.addWidget(self.button)
        self.setGeometry(450, 450, 400, 100)
        self.setWindowTitle("Word frequencies of Ngrams")
        self.show()

        
    def eventHandler(self):
        if self.combox.currentText() == "Unigrams":
            self.x = 1
        else:
            self.x = 2
        return self.x


    def updateUniBi(self):
        # open file: http://stackoverflow.com/questions/19996128/qtgui-qfiledialog-unicode-designations
        userFile = QtGui.QFileDialog.getOpenFileName(self)
        if self.x == 1:
            uniCount = Counter()
            for line in open(userFile):
                uniCount.update(line.split())
            for item in uniCount.most_common(20):
                lbl = QtGui.QLabel(str(item[0]+' '+str(item[1])),self)
                lbl.setAlignment(QtCore.Qt.AlignRight)
                self.box.addWidget(lbl)
        else:
            biCount = Counter()
            biDictio = {}
            for line in open(userFile):
                bi = len(line.split())
                words = line.split()
                for i in range(bi-1):
                    biOpmaak = ''.join(words[:2])
                    biGram = []
                    biGram.append(biOpmaak)
                    biCount.update(biGram)
                    biDictio[biOpmaak] = words[:2]
                    #words.pop(0) niet nodig om RT @... te laten zien?
            for item in biCount.most_common(20):
                lbl = QtGui.QLabel(' '.join(biDict.get(str(item[0])))+' '+str(item[1]),self)
                lbl.setAlignment(QtCore.Qt.AlignRight)
                self.box.addWidget(lbl)

        

    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    word = wordFreqUI()
    sys.exit(app.exec_())
   
