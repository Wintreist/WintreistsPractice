# Form implementation generated from reading ui file 'EjectedObject.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Ejected_Object(object):
    def setupUi(self, Form_Ejected_Object):
        Form_Ejected_Object.setObjectName("Form_Ejected_Object")
        Form_Ejected_Object.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Ejected_Object)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=Form_Ejected_Object)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_image = QtWidgets.QLabel(parent=self.groupBox)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.verticalLayout_2.addWidget(self.label_image)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form_Ejected_Object)
        QtCore.QMetaObject.connectSlotsByName(Form_Ejected_Object)

    def retranslateUi(self, Form_Ejected_Object):
        _translate = QtCore.QCoreApplication.translate
        Form_Ejected_Object.setWindowTitle(_translate("Form_Ejected_Object", "Form"))