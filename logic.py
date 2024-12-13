import csv
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDialog
from gui import Ui_DiscrepancyTracker


class DiscrepancyTrackerApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DiscrepancyTracker()
        self.ui.setupUi(self)

        """Set the current date"""
        self.ui.dateEdit.setDate(QDate.currentDate())

        """Disable OK button by default"""
        self.ui.buttonBox.button(self.ui.buttonBox.StandardButton.Ok).setEnabled(False)

        """Connect buttons to validation method"""
        self.ui.precheckButton.toggled.connect(self.validate_form)
        self.ui.afteruseButton.toggled.connect(self.validate_form)
        self.ui.duringuseButton.toggled.connect(self.validate_form)

        self.ui.checkBoxPowerUnit.toggled.connect(self.validate_form)
        self.ui.checkBoxVehicles.toggled.connect(self.validate_form)
        self.ui.checkBoxGolf_cart.toggled.connect(self.validate_form)
        self.ui.checkBoxLavCart.toggled.connect(self.validate_form)
        self.ui.checkBoxFuelTruck.toggled.connect(self.validate_form)
        self.ui.checkBoxTug.toggled.connect(self.validate_form)

        """Connect OK and Cancel buttons"""
        self.ui.buttonBox.accepted.connect(self.save_data)
        self.ui.buttonBox.rejected.connect(self.close)

    def validate_form(self):
        """Check if at least one timing and one asset is selected"""
        timing_selected = (
                self.ui.precheckButton.isChecked() or
                self.ui.afteruseButton.isChecked() or
                self.ui.duringuseButton.isChecked()
        )

        assets_selected = (
                self.ui.checkBoxPowerUnit.isChecked() or
                self.ui.checkBoxVehicles.isChecked() or
                self.ui.checkBoxGolf_cart.isChecked() or
                self.ui.checkBoxLavCart.isChecked() or
                self.ui.checkBoxFuelTruck.isChecked() or
                self.ui.checkBoxTug.isChecked()
        )

        """Enable or disable the OK button"""
        self.ui.buttonBox.button(self.ui.buttonBox.StandardButton.Ok).setEnabled(
            timing_selected and assets_selected
        )

    def save_data(self):
        """Save the data to a CSV file"""
        date = self.ui.dateEdit.text()
        timing = self.get_timing()
        assets = self.get_assets()
        severity = self.get_severity()
        additional_info = self.ui.textEdit.toPlainText()

        file_path = 'Tracker.csv'
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, timing, ', '.join(assets), additional_info, severity])

        self.accept()

    def get_timing(self):
        """Check timing and return the selected timing"""
        if self.ui.precheckButton.isChecked():
            return 'Precheck'
        elif self.ui.afteruseButton.isChecked():
            return 'After-Shift'
        elif self.ui.duringuseButton.isChecked():
            return 'During Use'
        return 'N/A'

    def get_assets(self):
        """Check assets and return the selected assets"""
        assets = []
        if self.ui.checkBoxPowerUnit.isChecked():
            assets.append('Power Unit')
        if self.ui.checkBoxVehicles.isChecked():
            assets.append('Vehicle')
        if self.ui.checkBoxGolf_cart.isChecked():
            assets.append('Golf Cart')
        if self.ui.checkBoxLavCart.isChecked():
            assets.append('LavCart')
        if self.ui.checkBoxFuelTruck.isChecked():
            assets.append('Fuel Truck')
        if self.ui.checkBoxTug.isChecked():
            assets.append('Tug')

        return assets

    def get_severity(self):
        """Check severity and return the selected severity"""
        if self.ui.radioButtonLow.isChecked():
            return 'Low'
        elif self.ui.radioButtonModerate.isChecked():
            return 'Moderate'
        elif self.ui.radioButtonSevere.isChecked():
            return 'Severe'
        return 'N/A'
