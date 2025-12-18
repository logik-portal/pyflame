# Script Template

**Script Version:** 5.0.1  
**Flame Version:** 2025  
**Written by:** Michael Vaglienty  
**Creation Date:** 02.09.22  
**Update Date:** 12.18.25  

**Script Type:** Batch

## Description

Template for flame python script with QT window
<br><br>
Load/Save Config sections can be deleted if config file not needed

## Menus

- Flame Main Menu → Logik → Logik Portal Script Setup → Script Template

## Installation

Copy script into /opt/Autodesk/shared/python/script_template

## Updates

### v5.0.1 [12.18.25]
- Added license to script.
<br>

### v5.0.0 [08.27.25]
- Updated to PyFlameLib v5.0.0.
<br>

### v4.1.0 [04.13.25]
- Updated to PyFlameLib v4.3.0.
<br>

### v4.0.0 [12.29.24]
- Updated to PyFlameLib v4.0.0.
- Removed script path checking method. This is now handled by PyFlameLib: pyflame.verify_script_install().
- PyFlameWindow now creates a PyFlameGridLayout by default that widgets can be added to. This should simplify the process of adding widgets to the window.
- Number of rows and columns in the grid layout can be set using the grid_layout_columns and grid_layout_rows arguments in the PyFlameWindow constructor.
- Overall and individual row height and column width can also be set from the PyFlameWindow constructor.
- Check PyFlameWindow docstring for more information.
- Updated SCRIPT_PATH to use absolute path. Allows script to be installed in different locations.
<br>

### v3.1.1 [04.18.24]
- Replaced QGridLayout with PyFlameGridLayout.
- Moved checking of script path and creating/loading of config to their own functions.
<br>

### v3.1.0 [02.07.24]
- Updates to UI/PySide.
- Updated script versioning to semantic versioning.
<br>

### v3.0 [08.10.23]
- Updated for pyflame lib v2.0.0.
