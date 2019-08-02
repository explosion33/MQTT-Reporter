# MQTT Reporter

A program to report status of programs to an MQTT broker. Used to send data for mining rigs

It currently only transmits "on", but I plan to make it send Mining Data and other system info

Contains an MSI installer and build Files
Installer located in `DIST` folder

change `data.txt` to your settings (empty for privacy reasons)
Also, the password entered into the txt file should be encrypted with a basic letter swap. See key in `main.py` (lines 20-24)

setup.py is used with cxFreeze to create an MSI installer and build files.
Enter `python setup.py bdist_msi` to create build Files and .msi
