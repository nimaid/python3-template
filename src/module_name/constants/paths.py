import os
import sys

# Test if this is a PyInstaller executable or a .py file
if getattr(sys, 'frozen', False):
    IS_EXE = True
    PATH = os.path.join(sys._MEIPASS, __name__.split(".")[1])
else:
    IS_EXE = False
    PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
