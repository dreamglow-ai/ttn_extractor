import sys
from PyQt5.QtWidgets import QApplication
from ttn_extractor.gui.ttn_gui import TTNExtractorDialog

def main():
    app = QApplication(sys.argv)
    dlg = TTNExtractorDialog()
    dlg.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
