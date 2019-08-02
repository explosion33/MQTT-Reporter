"Program to build project into exexutable and installer"
import sys
from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "program",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]main.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     "icon.ico",                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

base = None
if sys.platform == "win32": base = "Win32GUI"

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}

executables = [Executable("main.py", shortcutName='MQTTStatus', shortcutDir='DesktopFolder', icon='icon.ico', base=base)]

setup(
    name = 'MQTTStatus',
    author = 'Ethan Armstrong',
    options={
        "build_exe": {
            "packages":["paho.mqtt.client", "time", "json", "ast", "os", "sys"],
            "include_files":["icon.ico", "data.txt"]
            }},
    executables = executables,
    version = "1.1"
)
