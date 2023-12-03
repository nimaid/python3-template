#!/usr/bin/env python3

# ---- IMPORTS ----

import os
import sys
import argparse
import yaml
from enum import Enum


# ---- STANDARD CLASSES / GLOBALS ----

# A class to abstract useful variables which convey execution context
class ContextVars:
    def __init__(self):
        self.IS_EXE = None
        self.PROG_FILE = None
        self.PROG_PATH = None
        self.PATH = None
        self.get_pyinstaller_vars()

        self.VERSION_FILE = None
        self.VERSION = None
        self.DESCRIPTION = None
        self.TITLE = None
        self.LONG_TITLE = None
        self.COPYRIGHT = None
        self.get_versionfile_vars()

        self.USER_DIR = None
        self.PLATFORM = None
        self.APPDATA_DIR = None
        self.DATA_DIR = None
        self.get_platform_vars()
    
    # Test if this is a PyInstaller executable or a .py file
    def get_pyinstaller_vars(self):
        if getattr(sys, 'frozen', False):
            self.IS_EXE = True
            self.PROG_FILE = sys.executable
            self.PROG_PATH = os.path.dirname(self.PROG_FILE)
            self.PATH = sys._MEIPASS
        else:
            self.IS_EXE = False
            self.PROG_FILE = os.path.realpath(__file__)
            self.PROG_PATH = os.path.dirname(self.PROG_FILE)
            self.PATH = self.PROG_PATH

    # Read program version file
    def get_versionfile_vars(self):
        self.VERSION_FILE = os.path.join(self.PATH, "version.yml")
        with open(self.VERSION_FILE, "r") as f:
            version_file_dict = yaml.safe_load(f)
            
            self.VERSION = version_file_dict["Version"]
            self.DESCRIPTION = version_file_dict["FileDescription"]
            self.TITLE = version_file_dict["InternalName"]
            self.LONG_TITLE = version_file_dict["ProductName"]
            self.COPYRIGHT = version_file_dict["LegalCopyright"]
    
    # Platform codes
    class PlatformCodes(Enum):
        WINDOWS = "win32"
        LINUX = "linux"
        MAC = "darwin"
        UNKNOWN = "unknown"
    
    # Set platform dependent variables
    def get_platform_vars(self):
        self.USER_DIR = os.path.expanduser("~")
        
        if sys.platform == self.PlatformCodes.WINDOWS.value:
            self.PLATFORM = self.PlatformCodes.WINDOWS
            self.APPDATA_DIR = os.path.join(self.USER_DIR, "AppData", "Roaming")
        elif sys.platform == self.PlatformCodes.LINUX.value:
            self.PLATFORM = self.PlatformCodes.LINUX
            self.APPDATA_DIR = os.path.join(self.USER_DIR, ".local", "share")
        elif sys.platform == self.PlatformCodes.MAC.value:
            self.PLATFORM = self.PlatformCodes.MAC
            self.APPDATA_DIR = os.path.join(self.USER_DIR, "Library", "Application Support")
        else:
            self.PLATFORM = self.PlatformCodes.UNKNOWN
            # Unknown platform, save to wherever os.path thinks the home dir is
            self.APPDATA_DIR = self.USER_DIR
        
        self.DATA_DIR = os.path.join(self.APPDATA_DIR, self.TITLE)


# Make a global ContextVar object to use in the main code
CONTEXT = ContextVars()


# Define commonly used helper functions (mainly for argument parsing)
class Helpers:
    # General purpose text input stripper
    @staticmethod
    def strip_all(input_text):
        return input_text.strip().strip("\n").strip("\r").strip()

    # Makes sure a string represents a valid, existing file
    # This can be used with argparse as a valid argument type
    @staticmethod
    def file_path(string):
        if os.path.isfile(string):
            return string
        else:
            raise FileNotFoundError(string)


# ---- MAIN CLASSES ----

# Main class
class Python3Template:
    def __init__(self,
                 first,
                 second,
                 opcode
                 ):
        self.first = first
        self.second = second
        self.opcode = opcode.strip()
        
        if self.opcode not in self.OpCodes.VALID_OPTIONS.value:
            raise argparse.ArgumentTypeError("The operation code must be either \"+\", \"-\", \"*\", or \"/\"")
        if self.opcode == self.OpCodes.DIV.value and self.second == 0:
            raise ZeroDivisionError("Cannot divide by zero!")

    class OpCodes(Enum):
        ADD = "+"
        SUB = "-"
        MULT = "*"
        DIV = "/"
        VALID_OPTIONS = "+-*/"
    
    def add(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def mult(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second
    
    def operate(self):
        if self.opcode == self.OpCodes.ADD.value:
            print(f"The equation is {self.first} + {self.second}")
            return self.add()
        elif self.opcode == self.OpCodes.SUB.value:
            print(f"The equation is {self.first} - {self.second}")
            return self.sub()
        elif self.opcode == self.OpCodes.MULT.value:
            print(f"The equation is {self.first} * {self.second}")
            return self.mult()
        elif self.opcode == self.OpCodes.DIV.value:
            print(f"The equation is {self.first} / {self.second}")
            return self.div()
        else:
            raise argparse.ArgumentTypeError(f"Invalid opcode: \"{self.opcode}\"")
    
    def run(self):
        result = self.operate()
        print(f"The answer is {result}")


# ---- PROGRAM EXECUTION ----

# Parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser(
        description=f"{CONTEXT.DESCRIPTION}\n\nDefault parameters are shown in [brackets].",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-1", "--first", dest="first_arg", type=float, required=True,
        help="the first argument")
    parser.add_argument("-2", "--second", dest="second_arg", type=float, required=False, default=1.0,
        help="the second argument [1]")
    parser.add_argument("-o", "--operation", dest="opcode", type=str, required=False, default="+",
        help="the operation to perform on the arguments, either \"+\", \"-\", \"*\", or \"/\" [+]")
    
    return parser.parse_args()


def main(args):
    args = parse_args(args)
    
    python_3_template = Python3Template(
        first=args.first_arg, 
        second=args.second_arg, 
        opcode=args.opcode)
    
    python_3_template.run()


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
