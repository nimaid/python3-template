import os
import sys
import argparse
from enum import Enum

# Test if this is a PyInstaller executable or a .py file
if getattr(sys, 'frozen', False):
    IS_EXE = True
    PROG_FILE = sys.executable
    PROG_PATH = os.path.dirname(PROG_FILE)
    PATH = sys._MEIPASS
else:
    IS_EXE = False
    PROG_FILE = os.path.realpath(__file__)
    PROG_PATH = os.path.dirname(PROG_FILE)
    PATH = PROG_PATH

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
            print("The equation is {} + {}".format(self.first, self.second))
            return self.add()
        elif self.opcode == self.OpCodes.SUB.value:
            print("The equation is {} - {}".format(self.first, self.second))
            return self.sub()
        elif self.opcode == self.OpCodes.MULT.value:
            print("The equation is {} * {}".format(self.first, self.second))
            return self.mult()
        elif self.opcode == self.OpCodes.DIV.value:
            print("The equation is {} / {}".format(self.first, self.second))
            return self.div()
        else:
            raise argparse.ArgumentTypeError("Invalid opcode: \"{}\"".format(self.opcode))
    
    def run(self):
        print("The answer is {}".format(self.operate()))



# A helper function for the argument parser
def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)

# Parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser(
        description="A template for Python 3 scripts, by nimaid.\n\nDefault parameters are shown in [brackets].",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-1", "--first", dest="first_arg", type=float, required=True,
        help="the first argument")
    parser.add_argument("-2", "--second", dest="second_arg", type=float, required=False, default=1.0,
        help="the second argument [1]")
    parser.add_argument("-o", "--operaton", dest="opcode", type=str, required=False, default="+",
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
