import os
import sys

# Test if this is a PyInstaller executable or a .py file
if getattr(sys, 'frozen', False):
    IS_EXE = True
    PROG_PATH = os.path.dirname(sys.executable)
    PATH = os.path.join(sys._MEIPASS, __name__.split(".")[0])
else:
    IS_EXE = False
    PROG_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    PATH = PROG_PATH
