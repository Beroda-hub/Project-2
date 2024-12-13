# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DiscrepancyTracker(object):
    def setupUi(self, DiscrepancyTracker):
        DiscrepancyTracker.setObjectName("DiscrepancyTracker")
        DiscrepancyTracker.resize(550, 561)
        DiscrepancyTracker.setMinimumSize(QtCore.QSize(550, 561))
        DiscrepancyTracker.setMaximumSize(QtCore.QSize(550, 561))
        DiscrepancyTracker.setAutoFillBackground(False)
        self.layoutWidget = QtWidgets.QWidget(parent=DiscrepancyTracker)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 0, 341, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.todaysDate_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.todaysDate_label.setObjectName("todaysDate_label")
        self.verticalLayout.addWidget(self.todaysDate_label)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.precheckButton = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.precheckButton.setObjectName("precheckButton")
        self.buttonGroupAssets = QtWidgets.QButtonGroup(DiscrepancyTracker)
        self.buttonGroupAssets.setObjectName("buttonGroupAssets")
        self.buttonGroupAssets.addButton(self.precheckButton)
        self.verticalLayout.addWidget(self.precheckButton)
        self.afteruseButton = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.afteruseButton.setObjectName("afteruseButton")
        self.buttonGroupAssets.addButton(self.afteruseButton)
        self.verticalLayout.addWidget(self.afteruseButton)
        self.duringuseButton = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.duringuseButton.setObjectName("duringuseButton")
        self.buttonGroupAssets.addButton(self.duringuseButton)
        self.verticalLayout.addWidget(self.duringuseButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Asset_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.Asset_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Asset_label.setObjectName("Asset_label")
        self.horizontalLayout_2.addWidget(self.Asset_label)
        self.labelSeverity = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelSeverity.setObjectName("labelSeverity")
        self.horizontalLayout_2.addWidget(self.labelSeverity)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxTug = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxTug.setObjectName("checkBoxTug")
        self.gridLayout.addWidget(self.checkBoxTug, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 1)
        self.checkBoxFuelTruck = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxFuelTruck.setObjectName("checkBoxFuelTruck")
        self.gridLayout.addWidget(self.checkBoxFuelTruck, 1, 1, 1, 1)
        self.checkBoxPowerUnit = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxPowerUnit.setObjectName("checkBoxPowerUnit")
        self.gridLayout.addWidget(self.checkBoxPowerUnit, 1, 0, 1, 1)
        self.checkBoxVehicles = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxVehicles.setObjectName("checkBoxVehicles")
        self.gridLayout.addWidget(self.checkBoxVehicles, 2, 1, 1, 1)
        self.checkBoxGolf_cart = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxGolf_cart.setObjectName("checkBoxGolf_cart")
        self.gridLayout.addWidget(self.checkBoxGolf_cart, 2, 0, 1, 1)
        self.checkBoxLavCart = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxLavCart.setObjectName("checkBoxLavCart")
        self.gridLayout.addWidget(self.checkBoxLavCart, 0, 1, 1, 1)
        self.radioButtonLow = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.radioButtonLow.setObjectName("radioButtonLow")
        self.buttonGroupSeverity = QtWidgets.QButtonGroup(DiscrepancyTracker)
        self.buttonGroupSeverity.setObjectName("buttonGroupSeverity")
        self.buttonGroupSeverity.addButton(self.radioButtonLow)
        self.gridLayout.addWidget(self.radioButtonLow, 0, 2, 1, 1)
        self.radioButtonModerate = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.radioButtonModerate.setObjectName("radioButtonModerate")
        self.buttonGroupSeverity.addButton(self.radioButtonModerate)
        self.gridLayout.addWidget(self.radioButtonModerate, 1, 2, 1, 1)
        self.radioButtonSevere = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.radioButtonSevere.setObjectName("radioButtonSevere")
        self.buttonGroupSeverity.addButton(self.radioButtonSevere)
        self.gridLayout.addWidget(self.radioButtonSevere, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.additionalInformation_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.additionalInformation_label.setObjectName("additionalInformation_label")
        self.verticalLayout.addWidget(self.additionalInformation_label)
        self.textEdit = QtWidgets.QTextEdit(parent=self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.Error_or_passed = QtWidgets.QLabel(parent=self.layoutWidget)
        self.Error_or_passed.setText("")
        self.Error_or_passed.setObjectName("Error_or_passed")
        self.verticalLayout.addWidget(self.Error_or_passed)

        self.retranslateUi(DiscrepancyTracker)
        self.buttonBox.accepted.connect(DiscrepancyTracker.accept) # type: ignore
        self.buttonBox.rejected.connect(DiscrepancyTracker.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DiscrepancyTracker)

    def retranslateUi(self, DiscrepancyTracker):
        _translate = QtCore.QCoreApplication.translate
        DiscrepancyTracker.setWindowTitle(_translate("DiscrepancyTracker", "Discrepancy Tracker"))
        self.todaysDate_label.setText(_translate("DiscrepancyTracker", "Todays Date:"))
        self.label.setText(_translate("DiscrepancyTracker", "When did you find it? \n*Required"))
        self.precheckButton.setText(_translate("DiscrepancyTracker", "Precheck"))
        self.afteruseButton.setText(_translate("DiscrepancyTracker", "After-Shift"))
        self.duringuseButton.setText(_translate("DiscrepancyTracker", "During Use"))
        self.Asset_label.setText(_translate("DiscrepancyTracker", "What asset(s) is the discrepancy for? \n*Required"))
        self.labelSeverity.setText(_translate("DiscrepancyTracker", "        Severity"))
        self.checkBoxTug.setText(_translate("DiscrepancyTracker", "Tug"))
        self.checkBoxFuelTruck.setText(_translate("DiscrepancyTracker", "Fuel Truck"))
        self.checkBoxPowerUnit.setText(_translate("DiscrepancyTracker", "Power Unit"))
        self.checkBoxVehicles.setText(_translate("DiscrepancyTracker", "Vehicle"))
        self.checkBoxGolf_cart.setText(_translate("DiscrepancyTracker", "Golf Cart"))
        self.checkBoxLavCart.setText(_translate("DiscrepancyTracker", "LavCart"))
        self.radioButtonLow.setText(_translate("DiscrepancyTracker", "Low"))
        self.radioButtonModerate.setText(_translate("DiscrepancyTracker", "Moderate"))
        self.radioButtonSevere.setText(_translate("DiscrepancyTracker", "Severe"))
        self.additionalInformation_label.setText(_translate("DiscrepancyTracker", "Please Provide Any Additional Information Below."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiscrepancyTracker = QtWidgets.QDialog()
    ui = Ui_DiscrepancyTracker()
    ui.setupUi(DiscrepancyTracker)
    DiscrepancyTracker.show()
    sys.exit(app.exec())