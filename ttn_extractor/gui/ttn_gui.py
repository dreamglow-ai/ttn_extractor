import os
import json
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton, QProgressBar
)

# Load presets from the presets.json file
PRESETS_PATH = os.path.join(os.path.dirname(__file__), "../presets/presets.json")

class TTNExtractorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Extracteur TTN")
        self.setFixedSize(400, 300)
        self._load_presets()
        self._setup_ui()

    def _load_presets(self):
        with open(PRESETS_PATH, encoding="utf-8") as f:
            self.presets = json.load(f)

    def _setup_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Bureau:"))
        self.bureau_combo = QComboBox()
        for b in self.presets["bureau"]:
            self.bureau_combo.addItem(b['label'], b['code'])
        layout.addWidget(self.bureau_combo)

        layout.addWidget(QLabel("N° Escale Début:"))
        self.start_spin = QSpinBox()
        self.start_spin.setMinimum(10000)
        self.start_spin.setMaximum(99999)
        layout.addWidget(self.start_spin)

        layout.addWidget(QLabel("N° Escale Fin:"))
        self.end_spin = QSpinBox()
        self.end_spin.setMinimum(10000)
        self.end_spin.setMaximum(99999)
        layout.addWidget(self.end_spin)

        layout.addWidget(QLabel("Année:"))
        self.annee_combo = QComboBox()
        for a in self.presets["annee"]:
            self.annee_combo.addItem(str(a))
        layout.addWidget(self.annee_combo)

        self.extract_btn = QPushButton("Extraire")
        self.extract_btn.clicked.connect(self._on_extract)
        layout.addWidget(self.extract_btn)

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        layout.addWidget(self.progress)

        self.setLayout(layout)

    def _on_extract(self):
        bureau = self.bureau_combo.currentData()
        start = self.start_spin.value()
        end = self.end_spin.value()
        annee = self.annee_combo.currentText()
        print(f"Bureau: {bureau}, Start: {start}, End: {end}, Année: {annee}")
        # Placeholder: Later will trigger batch extraction!
