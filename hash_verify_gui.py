# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hash_verify_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hashDialog(object):
    def setupUi(self, hashDialog):
        hashDialog.setObjectName("hashDialog")
        hashDialog.setEnabled(True)
        hashDialog.resize(548, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(hashDialog.sizePolicy().hasHeightForWidth())
        hashDialog.setSizePolicy(sizePolicy)
        self.browseButton = QtWidgets.QPushButton(hashDialog)
        self.browseButton.setGeometry(QtCore.QRect(450, 33, 80, 23))
        self.browseButton.setObjectName("browseButton")
        self.inputEdit = QtWidgets.QLineEdit(hashDialog)
        self.inputEdit.setGeometry(QtCore.QRect(20, 33, 411, 23))
        self.inputEdit.setObjectName("inputEdit")
        self.inputlabel = QtWidgets.QLabel(hashDialog)
        self.inputlabel.setGeometry(QtCore.QRect(20, 10, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 78, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.inputlabel.setPalette(palette)
        self.inputlabel.setObjectName("inputlabel")
        self.digestLabel = QtWidgets.QLabel(hashDialog)
        self.digestLabel.setGeometry(QtCore.QRect(20, 76, 231, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 78, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 78, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.digestLabel.setPalette(palette)
        self.digestLabel.setObjectName("digestLabel")
        self.digestEdit = QtWidgets.QLineEdit(hashDialog)
        self.digestEdit.setGeometry(QtCore.QRect(20, 100, 511, 23))
        self.digestEdit.setObjectName("digestEdit")
        self.progressBar = QtWidgets.QProgressBar(hashDialog)
        self.progressBar.setGeometry(QtCore.QRect(130, 327, 301, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.resultsBox = QtWidgets.QTextBrowser(hashDialog)
        self.resultsBox.setGeometry(QtCore.QRect(20, 230, 511, 81))
        self.resultsBox.setObjectName("resultsBox")
        self.resultsLabel = QtWidgets.QLabel(hashDialog)
        self.resultsLabel.setGeometry(QtCore.QRect(20, 208, 59, 15))
        self.resultsLabel.setObjectName("resultsLabel")
        self.progressLabel = QtWidgets.QLabel(hashDialog)
        self.progressLabel.setGeometry(QtCore.QRect(20, 330, 59, 15))
        self.progressLabel.setObjectName("progressLabel")
        self.startButton = QtWidgets.QPushButton(hashDialog)
        self.startButton.setGeometry(QtCore.QRect(210, 150, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.startButton.setPalette(palette)
        self.startButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.startButton.setObjectName("startButton")
        self.closeButton = QtWidgets.QPushButton(hashDialog)
        self.closeButton.setGeometry(QtCore.QRect(450, 370, 82, 25))
        self.closeButton.setObjectName("closeButton")
        self.resetButton = QtWidgets.QPushButton(hashDialog)
        self.resetButton.setGeometry(QtCore.QRect(360, 370, 82, 25))
        self.resetButton.setObjectName("resetButton")

        self.retranslateUi(hashDialog)
        QtCore.QMetaObject.connectSlotsByName(hashDialog)

    def retranslateUi(self, hashDialog):
        _translate = QtCore.QCoreApplication.translate
        hashDialog.setWindowTitle(_translate("hashDialog", "Hash Sum Verification"))
        self.browseButton.setToolTip(_translate("hashDialog", "Browse for file"))
        self.browseButton.setText(_translate("hashDialog", "Browse"))
        self.inputlabel.setText(_translate("hashDialog", "Input File"))
        self.digestLabel.setText(_translate("hashDialog", "Original Hash Sum (paste or copy)"))
        self.resultsBox.setPlaceholderText(_translate("hashDialog", "Not started"))
        self.resultsLabel.setText(_translate("hashDialog", "Results"))
        self.progressLabel.setText(_translate("hashDialog", "Progress"))
        self.startButton.setToolTip(_translate("hashDialog", "Start the computation"))
        self.startButton.setText(_translate("hashDialog", "Start"))
        self.closeButton.setText(_translate("hashDialog", "Close"))
        self.resetButton.setText(_translate("hashDialog", "Reset"))

