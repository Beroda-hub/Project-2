import sys
from PyQt6.QtWidgets import QApplication
from logic import DiscrepancyTrackerApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiscrepancyTrackerApp()
    window.show()
    sys.exit(app.exec())