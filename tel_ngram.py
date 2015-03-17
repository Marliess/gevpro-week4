#!/usr/bin/python3

import sys
from collections import Counter
from PyQt4 import QtGui, QtCore
#thanks to: http://pyqt.sourceforge.net/Docs/PyQt4/qlayout.html

class wordFreqUI(QtGui.QWidget):
    """Constructor"""
    def __init__(self):
        super(wordFreqUI,self).__init__()
        self.initUI()

    def initUI(self):
        """Create a screen with a combobox where the user can
        choose between Bigrams and Unigrams. Create a button in
        the screen where a file can be selected by the user to find
        the Bigrams and Unigrams from this file."""
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
        """Returns a 1 if the user want Unigrams, return a 2
        if the user want Bigrams. """
        if self.combox.currentText() == "Unigrams":
            self.x = 1
        else:
            self.x = 2
        return self.x


    def updateUniBi(self):
        # open file: http://stackoverflow.com/questions/19996128/qtgui-qfiledialog-unicode-designations
        userFile = QtGui.QFileDialog.getOpenFileName(self)
        """The user wants a Unigram(self.x == 1). File will be openend
        and with Counter and most_common() we get the 20 most frequent
        unigrams. These are put in a string and will be displayed on the
        screen. """
                        
        """The user wants a Bigram. File will be openend
        and with Counter and most_common() we get the 20 most frequent
        bigrams. A dictionary is created to store the bigrams and their
        frequencies. These are put in a string and will be displayed on the
        screen. """
        if self.x == 1:
            uniCount = Counter()
            for line in open(userFile):
                uniCount.update(line.split())
            for item in uniCount.most_common(20):
                lbl = QtGui.QLabel(str(item[0]+"   " +str(item[1])),self)
                self.box.addWidget(lbl)
        else:
            biCount = Counter()
            biDictio = {}
            for line in open(userFile):
                bi = len(line.split())
                words = line.split()
                for i in range(bi-1):
                    """Select all bigrams in a sentence"""
                    biSelect = "".join(words[:2])
                    biGram = []
                    """Add the bigrams to the list biGram"""
                    biGram.append(biSelect)
                    """Update the most frequent bigrams"""
                    biCount.update(biGram)
                    biDictio[biSelect] = words[:2]
                    """You see Bigrams instead of RT@..."""
                    words.pop(0)
            for item in biCount.most_common(20):
                lbl = QtGui.QLabel(" ".join(biDictio.get(str(item[0])))+"   "+str(item[1]),self)
                self.box.addWidget(lbl)

        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    word = wordFreqUI()
    sys.exit(app.exec_())
   
