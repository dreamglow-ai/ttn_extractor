# TTN Extractor

## Project Overview
TTN Extractor is a simple, robust Windows automation tool for exporting manifest data from the legacy Tunisie TradeNet (TTN) desktop app. It saves hours for exporters with fast, accurate batch extraction to CSV—zero coding, French GUI, one-click workflow.

**Business Need**: Tunisian exporters spend 2-3 hours daily manually copying manifest data from TTN dialogs. This tool automates the extraction process with 99%+ accuracy.

**Tech Stack**: Python, pywinauto (UI automation), PyQt6 (French GUI), pandas (CSV export), YAML/JSON configs.

## Quick Start
1. Install Python 3.8+
2. Run: `pip install -r requirements.txt`
3. Launch: `python ttn_extractor/gui/main.py`
4. Select bureau/année presets, click \"Extraire\"

## Project Structure
\`\`\`
ttn_extractor/
├── gui/          # French UI (PyQt6)
├── core/         # Automation & extraction logic
├── presets/      # YAML selectors & JSON presets
├── logs/         # Session logs
└── tests/        # Test suites
\`\`\`
