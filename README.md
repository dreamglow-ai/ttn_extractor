# TTN Extractor

## Project Overview
TTN Extractor is a simple, robust Windows automation tool for exporting manifest data from the legacy Tunisie TradeNet (TTN) desktop app. It saves hours for exporters with fast, accurate batch extraction to CSV—zero coding, French GUI, one-click workflow.

**Business Need**: 
Manual TTN pulls cost clients ~5,000 TND/year in labor and fines from stale or missing shipment data. TTN Extractor cuts this pain to near-zero by automating the whole process.

## Tech Stack
- Windows 10/11, Python 3.10+ (core only)
- pywinauto (desktop UI automation)
- PyQt5 (GUI)
- pandas (CSV output)
- PyInstaller (for .exe packaging)
- Inno Setup (installer wizard)
- YAML/JSON for config

## Quick Start (for dev)
```bash
# Install dependencies for local dev
pip install pywinauto PyQt5 pandas pyyaml

# To run (main will come in Phase 2)
python ttn_extractor/main.py
```
**Production**: Bundled as .exe, no setup.

## Structure
- `/ttn_extractor/`
    - `/gui/` - PyQt5 GUI code
    - `/core/` - Automation, extraction logic
    - `/presets/` - YAML/JSON for selectors, bureau presets
    - `/logs/` - Extraction logs, debug files
    - `/tests/` - Unit and mock tests

## Field Selector Example
See `presets/selectors.yaml` for how manifest form fields are mapped for extraction.

---

**Documentation, test plan, and user support guide will be expanded in later phases.**
