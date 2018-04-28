import os, sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QColor
from hash_verify_gui import Ui_hashDialog
from PyQt5 import QtWidgets
import hashlib



class HashDialog(QDialog):
    def __init__(self):
        super(HashDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_hashDialog()
        self.ui.setupUi(self)
        self.filename = ''
        self.digest = ''
        # Connect up the buttons.
        self.ui.browseButton.clicked.connect(self.browse_file)
        self.ui.startButton.clicked.connect(self.verify_digest)

        
    def browse_file(self):
        print('need to bring up a file dialog here.')
        self.filename = QtWidgets.QFileDialog.getOpenFileName(None)[0]
        print('Filename selected is: ' + self.filename)
        self.ui.inputEdit.setText(self.filename)
    
        
    def verify_digest(self):
        """ Function to compute hash sums.
        
        """
        #check if empty strings.
        #hashes = hashlib.algorithms_available
        
        original = self.ui.digestEdit.text()
        print('original = ' +  original)
    
        h = hashlib.new('md5')
        #h = hashlib.new('sha256')
        
        if os.path.isfile(self.filename):
            with open(self.filename,'rb') as f:
                for block in iter(lambda: f.read(128), b""):
                    h.update(block)
                
            computed_hash = h.hexdigest()
            #self.compare results
            self.ui.resultsBox.setTextColor(QColor(0,0,0))
            self.ui.resultsBox.setText('Original: '+ original)
            self.ui.resultsBox.append('Computed: ' + computed_hash + '\n')
            if original == computed_hash:
                self.ui.resultsBox.setTextColor(QColor(50,255,50))
                self.ui.resultsBox.append('Success.  File Integrity Verified')
            else:
                self.ui.resultsBox.setTextColor(QColor(255, 50, 50))
                self.ui.resultsBox.append('Fail.  File does not match original.')
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'File not found.  Please check file name.')
        #print ('MD5 Hash Sum: ' + hash_string)
        print ('Computed: ' + computed_hash)
        
        
             
if __name__ == '__main__':  
    app = 0
    app = QApplication(sys.argv)
    window = HashDialog()
    window.show()
    sys.exit(app.exec_())
    
    
# Todo:
# Close and reset buttons need mapping
# Implement progress bar
# Profile block sizes to determine optimum
    
        