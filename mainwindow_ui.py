# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1551, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_tc_button = QFrame(self.centralwidget)
        self.add_tc_button.setObjectName(u"add_tc_button")
        self.add_tc_button.setFrameShape(QFrame.StyledPanel)
        self.add_tc_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.add_tc_button)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_result_button = QPushButton(self.add_tc_button)
        self.add_result_button.setObjectName(u"add_result_button")

        self.horizontalLayout.addWidget(self.add_result_button)

        self.add_tc_button_2 = QPushButton(self.add_tc_button)
        self.add_tc_button_2.setObjectName(u"add_tc_button_2")

        self.horizontalLayout.addWidget(self.add_tc_button_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.add_tc_button)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.tag_comboBox = QComboBox(self.frame)
        self.tag_comboBox.setObjectName(u"tag_comboBox")

        self.horizontalLayout_3.addWidget(self.tag_comboBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.board_comboBox = QComboBox(self.frame)
        self.board_comboBox.setObjectName(u"board_comboBox")

        self.horizontalLayout_4.addWidget(self.board_comboBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.bsp_comboBox = QComboBox(self.frame)
        self.bsp_comboBox.setObjectName(u"bsp_comboBox")

        self.horizontalLayout_5.addWidget(self.bsp_comboBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.search_result_button = QPushButton(self.frame)
        self.search_result_button.setObjectName(u"search_result_button")

        self.horizontalLayout_2.addWidget(self.search_result_button)


        self.verticalLayout_2.addWidget(self.frame)

        self.result_tableWidget = QTableWidget(self.add_tc_button)
        if (self.result_tableWidget.columnCount() < 12):
            self.result_tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.result_tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.result_tableWidget.setObjectName(u"result_tableWidget")
        self.result_tableWidget.setColumnCount(12)

        self.verticalLayout_2.addWidget(self.result_tableWidget)


        self.verticalLayout.addWidget(self.add_tc_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_result_button.setText(QCoreApplication.translate("MainWindow", u"Add Test Result", None))
        self.add_tc_button_2.setText(QCoreApplication.translate("MainWindow", u"Add Test Case", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"board", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"bsp", None))
        self.search_result_button.setText(QCoreApplication.translate("MainWindow", u"Search Test Result", None))
        ___qtablewidgetitem = self.result_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.result_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem2 = self.result_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sub Category", None));
        ___qtablewidgetitem3 = self.result_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem4 = self.result_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem5 = self.result_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Domain", None));
        ___qtablewidgetitem6 = self.result_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pre-condition", None));
        ___qtablewidgetitem7 = self.result_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Test Sequence", None));
        ___qtablewidgetitem8 = self.result_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Pass Criteria", None));
        ___qtablewidgetitem9 = self.result_tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Linked Work Item", None));
        ___qtablewidgetitem10 = self.result_tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Comment", None));
        ___qtablewidgetitem11 = self.result_tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"result", None));
    # retranslateUi

