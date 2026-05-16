# WA Corporation System Control Panel 2.0

![Version](https://img.shields.io/badge/version-2.0-red)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)

### ╔══════════════════════════════════════════════════════════╗
###   WA CORPORATION - NATIVE SYSTEM INTERFACE
### ╚══════════════════════════════════════════════════════════╝

**WA Corporation System Control Panel** is a powerful, retro-styled Windows terminal utility designed for advanced system management, diagnostics, and low-level control.

## ⚠ DISCLAIMER
**FOR EDUCATIONAL AND ADMINISTRATIVE PURPOSES ONLY.**
This tool contains features (in the "Danger Zone") that can cause system instability or data loss. Use at your own risk. WA Corporation is not responsible for any damage caused by this software.

## ⚡ Features
- **File Manager**: Advanced control with ownership hijacking (`takeown` / `icacls`).
- **System Control**: Native power management and diagnostics.
- **Process Manager**: PID-based and image-based process termination.
- **Network Tools**: Interface management and WiFi password recovery.
- **Danger Zone**: 
  - Native Kernel Panic (BSOD) via `RtlSetProcessIsCritical`.
  - Windows Defender hybrid disablement.
  - Event log flushing.
- **Multi-language**: EN, UA, RU, DE support.

## 🛠 Installation & Build
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/WAC-System-Panel.git
   ```
2. Install dependencies:
   ```bash
   pip install colorama
   ```
3. Run:
   ```bash
   python main.py
   ```

## 📦 Building EXE
To create a standalone executable:
```bash
pyinstaller --onefile --uac-admin --console --name "WAC_Panel" main.py
```

## 🌌 Visuals
- Full Retro DOOM 2 / 90s Hacker aesthetic.
- Glitch animations & typewriter effects.
- Box-drawing character interfaces.
