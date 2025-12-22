# Script Template
# Copyright (c) 2025 Michael Vaglienty
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# License:       GNU General Public License v3.0 (GPL-3.0)
#                https://www.gnu.org/licenses/gpl-3.0.en.html

"""
Script Name: Script Template
Script Version: 5.0.1
Flame Version: 2025
Written by: Michael Vaglienty
Creation Date: 02.09.22
Update Date: 12.18.25

License: GNU General Public License v3.0 (GPL-3.0) - see LICENSE file for details

Script Type: Batch

Description:

    Template for flame python script with QT window

    Load/Save Config sections can be deleted if config file not needed

Menus:

    Flame Main Menu -> Logik -> Logik Portal Script Setup -> Script Template

To install:

    Copy script into /opt/Autodesk/shared/python/script_template

Updates:

    v5.0.1 12.18.25
        - Added license to script.

    v5.0.0 08.27.25
        - Updated to PyFlameLib v5.0.0.

    v4.1.0 04.13.25
        - Updated to PyFlameLib v4.3.0.

    v4.0.0 12.29.24
        - Updated to PyFlameLib v4.0.0.
        - Removed script path checking method. This is now handled by PyFlameLib: pyflame.verify_script_install().
        - PyFlameWindow now creates a PyFlameGridLayout by default that widgets can be added to. This should simplify the process of adding widgets to the window.
          Number of rows and columns in the grid layout can be set using the grid_layout_columns and grid_layout_rows arguments in the PyFlameWindow constructor.
          Overall and individual row height and column width can also be set from the PyFlameWindow constructor.
          Check PyFlameWindow docstring for more information.
        - Updated SCRIPT_PATH to use absolute path. Allows script to be installed in different locations.

    v3.1.1 04.18.24
        - Replaced QGridLayout with PyFlameGridLayout.
        - Moved checking of script path and creating/loading of config to their own functions.

    v3.1.0 02.07.24
        - Updates to UI/PySide.
        - Updated script versioning to semantic versioning.

    v3.0 08.10.23
        - Updated for pyflame lib v2.0.0.
"""

# ==============================================================================
# [Imports]
# ==============================================================================

import os
import flame
from lib.pyflame_lib_script_template import *

# ==============================================================================
# [Constants]
# ==============================================================================

SCRIPT_NAME = 'Script Template'
SCRIPT_VERSION = 'v5.0.1'
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

# ==============================================================================
# [Main Script]
# ==============================================================================

class ScriptTemplate:

    def __init__(self, selection) -> None:

        pyflame.print_title(f'{SCRIPT_NAME} {SCRIPT_VERSION}')

        # Check script path, if path is incorrect, stop script.
        if not pyflame.verify_script_install():
            return

        # Create/Load config file settings.
        self.load_config()

        # Open main window
        self.main_window()

    def load_config(self) -> None:
        """
        Load Config
        ===========

        Loads configuration values from the config file and applies them to `self.settings`.

        If the config file does not exist, it creates the file using the default values
        from the `config_values` dictionary. Otherwise, it loads the existing config values
        and applies them to `self.settings`.
        """

        self.settings = PyFlameConfig(
            config_values={
                'setting_01': 'Some value',
                'setting_02': 'Another value',
                },
            )

    def main_window(self) -> None:
        """
        Main Window
        ===========

        Main window for script.
        """

        def save_config() -> None:
            """
            Save settings to config file and close window.
            """

            self.settings.save_config(
                config_values={
                    'setting_01': self.entry1.text,
                    'setting_02': self.entry2.text,
                    }
                )

            self.window.close()

            PyFlameMessageWindow(
                message='A really cool message goes here.',
                parent=self.window,
                )

        def close_window() -> None:

            self.window.close()

        # ------------------------------------------------------------------------------
        # [Window Elements]
        # ------------------------------------------------------------------------------

        # Window
        self.window = PyFlameWindow(
            title=f'{SCRIPT_NAME} <small>{SCRIPT_VERSION}',
            return_pressed=save_config, # Save config then close window when return/enter is pressed
            escape_pressed=close_window, # Close window when escape is pressed
            grid_layout_columns=5,
            grid_layout_rows=4,
            grid_layout_adjust_column_widths={2: 50},
            parent=None,
            )

        # Labels
        self.label1 = PyFlameLabel(
            text='Enter Something',
            )
        self.label2 = PyFlameLabel(
            text='Enter Something Else',
            )
        self.menu_label = PyFlameLabel(
            text='Menu',
            )

        # Entries
        self.entry1 = PyFlameEntry(
            text=self.settings.setting_01,
            )
        self.entry2 = PyFlameEntry(
            text='',
            )
        self.token_entry = PyFlameEntry(
            text='',
            )

        # Set Entry Tab-key Order
        self.window.tab_order = [
            self.entry1,
            self.entry2,
            self.token_entry,
            ]

        # Menu
        self.menu = PyFlameMenu(
            text='Option 1',
            menu_options=[
                'Option 1',
                'Option 2',
                'Option 3',
                ]
            )

        # Token Menu
        self.token_menu = PyFlameTokenMenu(
            token_dict={
                'token_01': 'Token 1',
                'token_02': 'Token 2',
                },
            token_dest=self.token_entry,
            )

        # Buttons
        self.save_button = PyFlameButton(
            text='Save',
            connect=save_config,
            color=Color.BLUE,
            )
        self.cancel_button = PyFlameButton(
            text='Cancel',
            connect=close_window,
            )

        # ------------------------------------------------------------------------------
        # [Widget Layout]
        # ------------------------------------------------------------------------------

        self.window.grid_layout.addWidget(self.label1, 0, 0)
        self.window.grid_layout.addWidget(self.entry1, 0, 1)

        self.window.grid_layout.addWidget(self.label2, 0, 3)
        self.window.grid_layout.addWidget(self.entry2, 0, 4)


        self.window.grid_layout.addWidget(self.menu_label, 1, 0)
        self.window.grid_layout.addWidget(self.menu, 1, 1)

        self.window.grid_layout.addWidget(self.token_entry, 1, 3)
        self.window.grid_layout.addWidget(self.token_menu, 1, 4)

        self.window.grid_layout.addWidget(self.cancel_button, 3, 3)
        self.window.grid_layout.addWidget(self.save_button, 3, 4)

        # ------------------------------------------------------------------------------

        self.entry1.setFocus()

# ==============================================================================
# [Scopes]
# ==============================================================================

def scope_library(selection):

    for item in selection:
        if isinstance(item, (flame.PyLibrary)):
            return True
    return False

# ==============================================================================
# [Flame Menus]
# ==============================================================================

def get_main_menu_custom_ui_actions():

    return [
        {
            'name': 'Logik',
            'hierarchy': [],
            'actions': []
        },
        {
            'name': 'Logik Portal Script Setup',
            'hierarchy': ['Logik'],
            'order': 2,
            'actions': [
               {
                    'name': 'Script Template',
                    'execute': ScriptTemplate,
                    #'isVisible': scope_library,
                    'minimumVersion': '2025'
               }
           ]
        }
    ]
