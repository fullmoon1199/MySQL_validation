# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_result.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListView, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(847, 297)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tag_lineEdit = QLineEdit(self.frame_6)
        self.tag_lineEdit.setObjectName(u"tag_lineEdit")
        self.tag_lineEdit.setMinimumSize(QSize(0, 0))
        self.tag_lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.tag_lineEdit)

        self.add_tag_button = QPushButton(self.frame_6)
        self.add_tag_button.setObjectName(u"add_tag_button")

        self.verticalLayout_7.addWidget(self.add_tag_button)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.tag_listView = QListView(self.frame_6)
        self.tag_listView.setObjectName(u"tag_listView")

        self.verticalLayout_7.addWidget(self.tag_listView)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.board_listView = QListView(self.frame_5)
        self.board_listView.setObjectName(u"board_listView")
        self.board_listView.setMinimumSize(QSize(100, 0))
        self.board_listView.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_6.addWidget(self.board_listView)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.bsp_listView = QListView(self.frame_3)
        self.bsp_listView.setObjectName(u"bsp_listView")
        self.bsp_listView.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_4.addWidget(self.bsp_listView)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.tc_listView = QListView(self.frame_4)
        self.tc_listView.setObjectName(u"tc_listView")
        self.tc_listView.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_5.addWidget(self.tc_listView)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pass_button = QRadioButton(self.frame_2)
        self.pass_button.setObjectName(u"pass_button")

        self.verticalLayout_3.addWidget(self.pass_button)

        self.fail_button = QRadioButton(self.frame_2)
        self.fail_button.setObjectName(u"fail_button")

        self.verticalLayout_3.addWidget(self.fail_button)

        self.na_button = QRadioButton(self.frame_2)
        self.na_button.setObjectName(u"na_button")

        self.verticalLayout_3.addWidget(self.na_button)


        self.horizontalLayout.addWidget(self.frame_2)

        self.add_button = QPushButton(self.frame)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tag_lineEdit.setInputMask("")
        self.tag_lineEdit.setText("")
        self.tag_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Add Tag", None))
        self.add_tag_button.setText(QCoreApplication.translate("Form", u"Add Tag", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"tag :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"board :", None))
        self.label.setText(QCoreApplication.translate("Form", u"bsp : ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TC : ", None))
        self.pass_button.setText(QCoreApplication.translate("Form", u"Pass", None))
        self.fail_button.setText(QCoreApplication.translate("Form", u"Fail", None))
        self.na_button.setText(QCoreApplication.translate("Form", u"N/A", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"ADD", None))
    # retranslateUi

