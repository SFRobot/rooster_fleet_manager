# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fleet_manager.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(986, 517)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabFleet = QtGui.QWidget()
        self.tabFleet.setObjectName(_fromUtf8("tabFleet"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabFleet)
        self.horizontalLayout_2.setMargin(10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayoutJobs = QtGui.QVBoxLayout()
        self.verticalLayoutJobs.setObjectName(_fromUtf8("verticalLayoutJobs"))
        self.labelJobsTitle = QtGui.QLabel(self.tabFleet)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelJobsTitle.setFont(font)
        self.labelJobsTitle.setObjectName(_fromUtf8("labelJobsTitle"))
        self.verticalLayoutJobs.addWidget(self.labelJobsTitle)
        self.treeWidgetJobs = QtGui.QTreeWidget(self.tabFleet)
        self.treeWidgetJobs.setAlternatingRowColors(True)
        self.treeWidgetJobs.setObjectName(_fromUtf8("treeWidgetJobs"))
        self.treeWidgetJobs.header().setVisible(True)
        self.treeWidgetJobs.header().setDefaultSectionSize(70)
        self.verticalLayoutJobs.addWidget(self.treeWidgetJobs)
        self.horizontalLayout_2.addLayout(self.verticalLayoutJobs)
        self.verticalLayoutMEx = QtGui.QVBoxLayout()
        self.verticalLayoutMEx.setObjectName(_fromUtf8("verticalLayoutMEx"))
        self.labelMExTitle = QtGui.QLabel(self.tabFleet)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMExTitle.setFont(font)
        self.labelMExTitle.setObjectName(_fromUtf8("labelMExTitle"))
        self.verticalLayoutMEx.addWidget(self.labelMExTitle)
        self.treeWidgetMEx = QtGui.QTreeWidget(self.tabFleet)
        self.treeWidgetMEx.setAlternatingRowColors(True)
        self.treeWidgetMEx.setObjectName(_fromUtf8("treeWidgetMEx"))
        self.treeWidgetMEx.header().setDefaultSectionSize(70)
        self.verticalLayoutMEx.addWidget(self.treeWidgetMEx)
        self.horizontalLayout_2.addLayout(self.verticalLayoutMEx)
        self.tabWidget.addTab(self.tabFleet, _fromUtf8(""))
        self.tabOrders = QtGui.QWidget()
        self.tabOrders.setObjectName(_fromUtf8("tabOrders"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabOrders)
        self.verticalLayout_3.setMargin(10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayoutOrderBase = QtGui.QHBoxLayout()
        self.horizontalLayoutOrderBase.setObjectName(_fromUtf8("horizontalLayoutOrderBase"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelKeyword = QtGui.QLabel(self.tabOrders)
        self.labelKeyword.setObjectName(_fromUtf8("labelKeyword"))
        self.horizontalLayout_3.addWidget(self.labelKeyword)
        self.comboBoxKeyword = QtGui.QComboBox(self.tabOrders)
        self.comboBoxKeyword.setObjectName(_fromUtf8("comboBoxKeyword"))
        self.comboBoxKeyword.addItem(_fromUtf8(""))
        self.comboBoxKeyword.addItem(_fromUtf8(""))
        self.comboBoxKeyword.addItem(_fromUtf8(""))
        self.comboBoxKeyword.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBoxKeyword)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayoutOrderBase.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelPriority = QtGui.QLabel(self.tabOrders)
        self.labelPriority.setObjectName(_fromUtf8("labelPriority"))
        self.horizontalLayout_4.addWidget(self.labelPriority)
        self.comboBoxPriority = QtGui.QComboBox(self.tabOrders)
        self.comboBoxPriority.setObjectName(_fromUtf8("comboBoxPriority"))
        self.comboBoxPriority.addItem(_fromUtf8(""))
        self.comboBoxPriority.addItem(_fromUtf8(""))
        self.comboBoxPriority.addItem(_fromUtf8(""))
        self.comboBoxPriority.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.comboBoxPriority)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayoutOrderBase.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayoutOrderBase)
        self.horizontalLayoutOrderArguments = QtGui.QHBoxLayout()
        self.horizontalLayoutOrderArguments.setObjectName(_fromUtf8("horizontalLayoutOrderArguments"))
        self.labelArguments = QtGui.QLabel(self.tabOrders)
        self.labelArguments.setObjectName(_fromUtf8("labelArguments"))
        self.horizontalLayoutOrderArguments.addWidget(self.labelArguments)
        self.verticalLayout_3.addLayout(self.horizontalLayoutOrderArguments)
        self.lineEditArguments = QtGui.QLineEdit(self.tabOrders)
        self.lineEditArguments.setObjectName(_fromUtf8("lineEditArguments"))
        self.verticalLayout_3.addWidget(self.lineEditArguments)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayoutAddOrder = QtGui.QHBoxLayout()
        self.horizontalLayoutAddOrder.setObjectName(_fromUtf8("horizontalLayoutAddOrder"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutAddOrder.addItem(spacerItem3)
        self.pushButtonAddOrder = QtGui.QPushButton(self.tabOrders)
        self.pushButtonAddOrder.setMinimumSize(QtCore.QSize(300, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddOrder.setIcon(icon)
        self.pushButtonAddOrder.setObjectName(_fromUtf8("pushButtonAddOrder"))
        self.horizontalLayoutAddOrder.addWidget(self.pushButtonAddOrder)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutAddOrder.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayoutAddOrder)
        spacerItem5 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.labelArguments_2 = QtGui.QLabel(self.tabOrders)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.labelArguments_2.setFont(font)
        self.labelArguments_2.setObjectName(_fromUtf8("labelArguments_2"))
        self.verticalLayout_3.addWidget(self.labelArguments_2)
        self.treeWidgetOrders = QtGui.QTreeWidget(self.tabOrders)
        self.treeWidgetOrders.setAlternatingRowColors(True)
        self.treeWidgetOrders.setObjectName(_fromUtf8("treeWidgetOrders"))
        self.verticalLayout_3.addWidget(self.treeWidgetOrders)
        self.horizontalLayoutOrderButtons = QtGui.QHBoxLayout()
        self.horizontalLayoutOrderButtons.setObjectName(_fromUtf8("horizontalLayoutOrderButtons"))
        self.pushButtonPlaceOrder = QtGui.QPushButton(self.tabOrders)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPlaceOrder.setIcon(icon1)
        self.pushButtonPlaceOrder.setObjectName(_fromUtf8("pushButtonPlaceOrder"))
        self.horizontalLayoutOrderButtons.addWidget(self.pushButtonPlaceOrder)
        self.pushButtonClearList = QtGui.QPushButton(self.tabOrders)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/New document.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClearList.setIcon(icon2)
        self.pushButtonClearList.setObjectName(_fromUtf8("pushButtonClearList"))
        self.horizontalLayoutOrderButtons.addWidget(self.pushButtonClearList)
        self.verticalLayout_3.addLayout(self.horizontalLayoutOrderButtons)
        self.tabWidget.addTab(self.tabOrders, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPlaceholder = QtGui.QAction(MainWindow)
        self.actionPlaceholder.setObjectName(_fromUtf8("actionPlaceholder"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit_application = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_application.setIcon(icon4)
        self.actionQuit_application.setObjectName(_fromUtf8("actionQuit_application"))
        self.actionPlaceholder2 = QtGui.QAction(MainWindow)
        self.actionPlaceholder2.setObjectName(_fromUtf8("actionPlaceholder2"))
        self.menuFile.addAction(self.actionPlaceholder)
        self.menuFile.addAction(self.actionPlaceholder2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_application)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fleet Manager", None))
        self.labelJobsTitle.setText(_translate("MainWindow", "Jobs", None))
        self.treeWidgetJobs.setSortingEnabled(True)
        self.treeWidgetJobs.headerItem().setText(0, _translate("MainWindow", "Job ID", None))
        self.treeWidgetJobs.headerItem().setText(1, _translate("MainWindow", "Priority", None))
        self.treeWidgetJobs.headerItem().setText(2, _translate("MainWindow", "Keyword", None))
        self.treeWidgetJobs.headerItem().setText(3, _translate("MainWindow", "Status", None))
        self.treeWidgetJobs.headerItem().setText(4, _translate("MainWindow", "MEx ID", None))
        self.treeWidgetJobs.headerItem().setText(5, _translate("MainWindow", "Task", None))
        self.labelMExTitle.setText(_translate("MainWindow", "Mobile Executors (MEx)", None))
        self.treeWidgetMEx.setSortingEnabled(True)
        self.treeWidgetMEx.headerItem().setText(0, _translate("MainWindow", "MEx ID", None))
        self.treeWidgetMEx.headerItem().setText(1, _translate("MainWindow", "Status", None))
        self.treeWidgetMEx.headerItem().setText(2, _translate("MainWindow", "Job ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFleet), _translate("MainWindow", "Fleet", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabFleet), _translate("MainWindow", "Fleet overview tab with information of Jobs and MExes", None))
        self.labelKeyword.setText(_translate("MainWindow", "Keyword:", None))
        self.comboBoxKeyword.setStatusTip(_translate("MainWindow", "The keyword used for the order. Defines Job type.", None))
        self.comboBoxKeyword.setItemText(0, _translate("MainWindow", "MOVE", None))
        self.comboBoxKeyword.setItemText(1, _translate("MainWindow", "LOAD", None))
        self.comboBoxKeyword.setItemText(2, _translate("MainWindow", "UNLOAD", None))
        self.comboBoxKeyword.setItemText(3, _translate("MainWindow", "TRANSPORT", None))
        self.labelPriority.setText(_translate("MainWindow", "Priority:", None))
        self.comboBoxPriority.setStatusTip(_translate("MainWindow", "The priority of the order, higher priority orders are allocated earlier.", None))
        self.comboBoxPriority.setItemText(0, _translate("MainWindow", "LOW", None))
        self.comboBoxPriority.setItemText(1, _translate("MainWindow", "MEDIUM", None))
        self.comboBoxPriority.setItemText(2, _translate("MainWindow", "HIGH", None))
        self.comboBoxPriority.setItemText(3, _translate("MainWindow", "CRITICAL", None))
        self.labelArguments.setText(_translate("MainWindow", "Order arguments (arguments must be seperated with spaces):", None))
        self.pushButtonAddOrder.setStatusTip(_translate("MainWindow", "Add the above defined order to the order list below.", None))
        self.pushButtonAddOrder.setText(_translate("MainWindow", " &Add order to Order list", None))
        self.labelArguments_2.setText(_translate("MainWindow", "Order list", None))
        self.treeWidgetOrders.headerItem().setText(0, _translate("MainWindow", "Keyword", None))
        self.treeWidgetOrders.headerItem().setText(1, _translate("MainWindow", "Priority", None))
        self.treeWidgetOrders.headerItem().setText(2, _translate("MainWindow", "Arguments", None))
        self.pushButtonPlaceOrder.setStatusTip(_translate("MainWindow", "Call the Job Manager service, placing the current orders in the order list.", None))
        self.pushButtonPlaceOrder.setText(_translate("MainWindow", "  &Place orders", None))
        self.pushButtonClearList.setStatusTip(_translate("MainWindow", "Clears all orders in the order list.", None))
        self.pushButtonClearList.setText(_translate("MainWindow", "  &Clear list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOrders), _translate("MainWindow", "Orders", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabOrders), _translate("MainWindow", "Order placement tab with ability to create and send new orders.", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionPlaceholder.setText(_translate("MainWindow", "Placeholder", None))
        self.actionAbout.setText(_translate("MainWindow", "&About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "Shows a popup with additional information about this application.", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionQuit_application.setText(_translate("MainWindow", "&Quit application", None))
        self.actionQuit_application.setStatusTip(_translate("MainWindow", "Closes the application.", None))
        self.actionQuit_application.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionPlaceholder2.setText(_translate("MainWindow", "Placeholder2", None))

import images_rc