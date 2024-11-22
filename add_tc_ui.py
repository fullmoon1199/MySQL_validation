# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_tc.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1202, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.id_lineEdit = QLineEdit(Form)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.horizontalLayout.addWidget(self.id_lineEdit)

        self.category_lineEdit = QLineEdit(Form)
        self.category_lineEdit.setObjectName(u"category_lineEdit")

        self.horizontalLayout.addWidget(self.category_lineEdit)

        self.sub_caregory_lineEdit = QLineEdit(Form)
        self.sub_caregory_lineEdit.setObjectName(u"sub_caregory_lineEdit")

        self.horizontalLayout.addWidget(self.sub_caregory_lineEdit)

        self.title_lineEdit = QLineEdit(Form)
        self.title_lineEdit.setObjectName(u"title_lineEdit")

        self.horizontalLayout.addWidget(self.title_lineEdit)

        self.status_lineEdit = QLineEdit(Form)
        self.status_lineEdit.setObjectName(u"status_lineEdit")

        self.horizontalLayout.addWidget(self.status_lineEdit)

        self.domain_lineEdit = QLineEdit(Form)
        self.domain_lineEdit.setObjectName(u"domain_lineEdit")

        self.horizontalLayout.addWidget(self.domain_lineEdit)

        self.pre_condition_lineEdit = QLineEdit(Form)
        self.pre_condition_lineEdit.setObjectName(u"pre_condition_lineEdit")

        self.horizontalLayout.addWidget(self.pre_condition_lineEdit)

        self.test_sequence_lineEdit = QLineEdit(Form)
        self.test_sequence_lineEdit.setObjectName(u"test_sequence_lineEdit")

        self.horizontalLayout.addWidget(self.test_sequence_lineEdit)

        self.pass_criteria_lineEdit = QLineEdit(Form)
        self.pass_criteria_lineEdit.setObjectName(u"pass_criteria_lineEdit")

        self.horizontalLayout.addWidget(self.pass_criteria_lineEdit)

        self.link_lineEdit = QLineEdit(Form)
        self.link_lineEdit.setObjectName(u"link_lineEdit")

        self.horizontalLayout.addWidget(self.link_lineEdit)

        self.comment_lineEdit = QLineEdit(Form)
        self.comment_lineEdit.setObjectName(u"comment_lineEdit")

        self.horizontalLayout.addWidget(self.comment_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_tc_tag_comboBox = QComboBox(Form)
        self.add_tc_tag_comboBox.setObjectName(u"add_tc_tag_comboBox")

        self.horizontalLayout_3.addWidget(self.add_tc_tag_comboBox)

        self.add_tc_board_comboBox = QComboBox(Form)
        self.add_tc_board_comboBox.setObjectName(u"add_tc_board_comboBox")

        self.horizontalLayout_3.addWidget(self.add_tc_board_comboBox)

        self.add_tc_bsp_comboBox = QComboBox(Form)
        self.add_tc_bsp_comboBox.setObjectName(u"add_tc_bsp_comboBox")

        self.horizontalLayout_3.addWidget(self.add_tc_bsp_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.auto_tc_pushButton = QPushButton(Form)
        self.auto_tc_pushButton.setObjectName(u"auto_tc_pushButton")
        self.auto_tc_pushButton.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.auto_tc_pushButton)

        self.add_tc_button = QPushButton(Form)
        self.add_tc_button.setObjectName(u"add_tc_button")
        self.add_tc_button.setMinimumSize(QSize(100, 100))
        self.add_tc_button.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.add_tc_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_lineEdit.setInputMask("")
        self.id_lineEdit.setText("")
        self.id_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"ID", None))
        self.category_lineEdit.setText("")
        self.category_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Category", None))
        self.sub_caregory_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Sub Category", None))
        self.title_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Title", None))
        self.status_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Status", None))
        self.domain_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Domain", None))
        self.pre_condition_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Pre-condition", None))
        self.test_sequence_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Test Sequence", None))
        self.pass_criteria_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Pass Criteria", None))
        self.link_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Linked Work Items", None))
        self.comment_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Comment", None))
        self.auto_tc_pushButton.setText(QCoreApplication.translate("Form", u"Auto", None))
        self.add_tc_button.setText(QCoreApplication.translate("Form", u"Add Test Case", None))
    # retranslateUi

