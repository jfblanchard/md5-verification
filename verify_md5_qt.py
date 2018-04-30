import os
import sys
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
        self.original = ''
        
        # Connect up the buttons.
        self.ui.browseButton.clicked.connect(self.browse_file)
        self.ui.startButton.clicked.connect(self.verify_digest)
        self.ui.closeButton.clicked.connect(self.close_me)
        self.ui.resetButton.clicked.connect(self.reset_me)


    def browse_file(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(None)[0]
        self.ui.inputEdit.setText(self.filename)
        
        
    def close_me(self):
        self.close()
        
        
    def reset_me(self):
        self.ui.digestEdit.setText('')
        self.filename = ''
        self.ui.inputEdit.setText('')
        self.ui.resultsBox.setText('')
        self.ui.progressBar.setValue(0)
              

    def verify_digest(self):
        """ Function to compute hash sums.

        """
        # check if empty strings.
        # hashes = hashlib.algorithms_available

        original = self.ui.digestEdit.text()
        print('original = ' + original)

        h = hashlib.new('md5')
        # h = hashlib.new('sha256')

        if os.path.isfile(self.filename):
            bytes_read = 0
            block_size = 128  #bytes
            file_size = os.path.getsize(self.filename)
            
            with open(self.filename, 'rb') as f:
                for block in iter(lambda: f.read(block_size), b""):
                    h.update(block)
                    bytes_read += block_size
                    self.ui.progressBar.setValue(100*bytes_read/file_size)
                    
            computed_hash = h.hexdigest()
            
            # compare results...move to separate function?
            self.ui.resultsBox.setTextColor(QColor(0, 0, 0))
            self.ui.resultsBox.setText('Original: ' + original)
            self.ui.resultsBox.append('Computed: ' + computed_hash + '\n')
            if original == computed_hash:
                self.ui.resultsBox.setTextColor(QColor(50, 225, 50))
                self.ui.resultsBox.append('Success.  File Integrity Verified')
            else:
                self.ui.resultsBox.setTextColor(QColor(225, 50, 50))
                self.ui.resultsBox.append('Verification Failed.')
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'File not found.  Please check file name.')


if __name__ == '__main__':
    app = 0
    app = QApplication(sys.argv)
    window = HashDialog()
    window.show()
    sys.exit(app.exec_())


# Todo:
# Add more algorithm types
    