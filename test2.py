# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1107, 852)
        self.tabWidget_RecentFolder = QtGui.QTabWidget(Dialog)
        self.tabWidget_RecentFolder.setGeometry(QtCore.QRect(0, 10, 1111, 781))
        self.tabWidget_RecentFolder.setObjectName(_fromUtf8("tabWidget_RecentFolder"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget_RecentFolder.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1101, 771))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableWidget_OS = QtGui.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget_OS.setObjectName(_fromUtf8("tableWidget_OS"))
        self.tableWidget_OS.setColumnCount(0)
        self.tableWidget_OS.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget_OS)
        self.tabWidget_RecentFolder.addTab(self.tab_2, _fromUtf8(""))
        self.tab_Registry = QtGui.QWidget()
        self.tab_Registry.setObjectName(_fromUtf8("tab_Registry"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_Registry)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget_UserAssist = QtGui.QTabWidget(self.tab_Registry)
        self.tabWidget_UserAssist.setObjectName(_fromUtf8("tabWidget_UserAssist"))
        self.tab_MountedDevices = QtGui.QWidget()
        self.tab_MountedDevices.setObjectName(_fromUtf8("tab_MountedDevices"))
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.tab_MountedDevices)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 1081, 701))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tableWidget_MountedDevices = QtGui.QTableWidget(self.horizontalLayoutWidget_6)
        self.tableWidget_MountedDevices.setObjectName(_fromUtf8("tableWidget_MountedDevices"))
        self.tableWidget_MountedDevices.setColumnCount(0)
        self.tableWidget_MountedDevices.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.tableWidget_MountedDevices)
        self.tabWidget_UserAssist.addTab(self.tab_MountedDevices, _fromUtf8(""))
        self.tab_OpenSavePidMRU = QtGui.QWidget()
        self.tab_OpenSavePidMRU.setObjectName(_fromUtf8("tab_OpenSavePidMRU"))
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.tab_OpenSavePidMRU)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 1081, 701))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tableWidget_OpenSavePidlMRU = QtGui.QTableWidget(self.horizontalLayoutWidget_5)
        self.tableWidget_OpenSavePidlMRU.setObjectName(_fromUtf8("tableWidget_OpenSavePidlMRU"))
        self.tableWidget_OpenSavePidlMRU.setColumnCount(0)
        self.tableWidget_OpenSavePidlMRU.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.tableWidget_OpenSavePidlMRU)
        self.tabWidget_UserAssist.addTab(self.tab_OpenSavePidMRU, _fromUtf8(""))
        self.tab_TypedPaths = QtGui.QWidget()
        self.tab_TypedPaths.setObjectName(_fromUtf8("tab_TypedPaths"))
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.tab_TypedPaths)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 1081, 701))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.tableWidget_TypedPaths = QtGui.QTableWidget(self.horizontalLayoutWidget_7)
        self.tableWidget_TypedPaths.setObjectName(_fromUtf8("tableWidget_TypedPaths"))
        self.tableWidget_TypedPaths.setColumnCount(0)
        self.tableWidget_TypedPaths.setRowCount(0)
        self.horizontalLayout_8.addWidget(self.tableWidget_TypedPaths)
        self.tabWidget_UserAssist.addTab(self.tab_TypedPaths, _fromUtf8(""))
        self.tab_UserAssist = QtGui.QWidget()
        self.tab_UserAssist.setObjectName(_fromUtf8("tab_UserAssist"))
        self.horizontalLayoutWidget_8 = QtGui.QWidget(self.tab_UserAssist)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 1081, 701))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.tableWidget_5 = QtGui.QTableWidget(self.horizontalLayoutWidget_8)
        self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.horizontalLayout_9.addWidget(self.tableWidget_5)
        self.tabWidget_UserAssist.addTab(self.tab_UserAssist, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget_UserAssist)
        self.tabWidget_RecentFolder.addTab(self.tab_Registry, _fromUtf8(""))
        self.tab_Jumplists = QtGui.QWidget()
        self.tab_Jumplists.setObjectName(_fromUtf8("tab_Jumplists"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_Jumplists)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget_JumpLists = QtGui.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget_JumpLists.setObjectName(_fromUtf8("tableWidget_JumpLists"))
        self.tableWidget_JumpLists.setColumnCount(0)
        self.tableWidget_JumpLists.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget_JumpLists)
        self.tabWidget_RecentFolder.addTab(self.tab_Jumplists, _fromUtf8(""))
        self.tab_Prefetch = QtGui.QWidget()
        self.tab_Prefetch.setObjectName(_fromUtf8("tab_Prefetch"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab_Prefetch)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableWidget_Prefetch = QtGui.QTableWidget(self.horizontalLayoutWidget_3)
        self.tableWidget_Prefetch.setObjectName(_fromUtf8("tableWidget_Prefetch"))
        self.tableWidget_Prefetch.setColumnCount(0)
        self.tableWidget_Prefetch.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidget_Prefetch)
        self.tabWidget_RecentFolder.addTab(self.tab_Prefetch, _fromUtf8(""))
        self.tab_RecentFolder = QtGui.QWidget()
        self.tab_RecentFolder.setObjectName(_fromUtf8("tab_RecentFolder"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.tab_RecentFolder)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tableWidget_6 = QtGui.QTableWidget(self.horizontalLayoutWidget_4)
        self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_6"))
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.tableWidget_6)
        self.tabWidget_RecentFolder.addTab(self.tab_RecentFolder, _fromUtf8(""))
        self.button_Start_Exam = QtGui.QPushButton(Dialog)
        self.button_Start_Exam.setGeometry(QtCore.QRect(890, 810, 93, 28))
        self.button_Start_Exam.setObjectName(_fromUtf8("button_Start_Exam"))
        self.button_Exit = QtGui.QPushButton(Dialog)
        self.button_Exit.setGeometry(QtCore.QRect(1000, 810, 93, 28))
        self.button_Exit.setObjectName(_fromUtf8("button_Exit"))

        self.retranslateUi(Dialog)
        self.tabWidget_RecentFolder.setCurrentIndex(1)
        self.tabWidget_UserAssist.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget_RecentFolder.setTabText(self.tabWidget_RecentFolder.indexOf(self.tab), _translate("Dialog", "Start", None))
        self.tabWidget_RecentFolder.setTabText(self.tabWidget_RecentFolder.indexOf(self.tab_2), _translate("Dialog", "Operating System Information", None))
        self.tabWidget_UserAssist.setTabText(self.tabWidget_UserAssist.indexOf(self.tab_MountedDevices), _translate("Dialog", "Mounted Devices", None))
        self.tabWidget_UserAssist.setTabText(self.tabWidget_UserAssist.indexOf(self.tab_OpenSavePidMRU), _translate("Dialog", "OpenSavePidlMRU", None))
        self.tabWidget_UserAssist.setTabText(self.tabWidget_UserAssist.indexOf(self.tab_TypedPaths), _translate("Dialog", "Typed Paths", None))
        self.tabWidget_UserAssist.setTabText(self.tabWidget_UserAssist.indexOf(self.tab_UserAssist), _translate("Dialog", "UserAssist", None))
        self.tabWidget_RecentFolder.setTabText(self.tabWidget_RecentFolder.indexOf(self.tab_Registry), _translate("Dialog", "Registry", None))
        self.tabWidget_RecentFolder.setTabText(self.tabWidget_RecentFolder.indexOf(self.tab_Jumplists), _translate("Dialog", "Jumplists", None))
        self.tabWidget_RecentFolder.setTabText(self.tabWidget_RecentFolder.indexOf(self.tab_Prefetch), _translate("Dialog", "Prefetch", None))
        self.tabWidget_RecentFolder.setTabText(self.tabWidget_RecentFolder.indexOf(self.tab_RecentFolder), _translate("Dialog", "Recent Folder", None))
        self.button_Start_Exam.setText(_translate("Dialog", "Start", None))
        self.button_Exit.setText(_translate("Dialog", "Cancel", None))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Ui_Dialog(object)
    f.Show()
    app.setMainWidget(f)
    app.exec_loop()
