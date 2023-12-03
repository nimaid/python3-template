#!/usr/bin/env python3

import os
import sys
import re
import shutil
import keyboard

PROG_FILE = os.path.realpath(__file__)
PATH = os.path.dirname(PROG_FILE)


# Main class
class Python3TemplateInit:
    def __init__(self,
                 name,
                 simple_name,
                 author,
                 description,
                 version
                 ):
        self.name = name
        self.simple_name = simple_name
        self.author = author
        self.description = description
        self.version = version
        
        self.file_list = {
            "build": {
                "main": "build.bat",
                "template": "build.bat.template"
            },
            "env": {
                "main": "environment.yml",
                "template": "environment.yml.template"
            },
            "program": {
                "main": f"{self.name}.py",
                "template": "name.py.template"
            },
            "version": {
                "main": "version.yml",
                "template": "version.yml.template"
            }
        }

    def copy_all_files(self):
        for v,k in enumerate(self.file_list):
            shutil.copy(self.file_list[k]["template"], self.file_list[k]["main"])

    @staticmethod
    def replace_key_in_file(file_in, key, value):
        delim_start = "{["
        delim_end = "]}"
        
        full_key = f"{delim_start}{key}{delim_end}"
        
        with open(file_in, "r") as f:
            file_text = f.read()
        
        new_text = file_text.replace(full_key, value)
        
        with open(file_in, "w") as f:
            f.write(new_text)
    
    def replace_key_in_all_files(self, key, value):
        for v,k in enumerate(self.file_list):
            self.replace_key_in_file(self.file_list[k]["main"], key, value)
    
    def cleanup(self):
        # Delete source templates
        for v,k in enumerate(self.file_list):
            os.remove(self.file_list[k]["template"])
        # Suicide
        os.remove(PROG_FILE)
    
    def run(self):
        print()
        print("Project Info Summary")
        print("--------------------")
        print(f"Name: {self.name}")
        print(f"Simple Name: {self.simple_name}")
        print(f"Author: {self.author}")
        print(f"Description: {self.description}")
        print(f"Version: {self.version}")
        print()
        
        print("Project File Renaming")
        print("---------------------")
        for v,k in enumerate(self.file_list):
            template = self.file_list[k]["template"]
            new_file = self.file_list[k]["main"]
            print(f"{template} --> {new_file}")
        print()
        
        print("Press [Enter] to continue, any other button to quit...")
        if keyboard.read_key() != "enter":
            exit(1)
        print()
        
        # Copy new files
        self.copy_all_files()
        
        # Replace the keys in the new files
        self.replace_key_in_all_files("name", self.name)
        self.replace_key_in_all_files("simple_name", self.simple_name)
        self.replace_key_in_all_files("author", self.author)
        self.replace_key_in_all_files("description", self.description)
        self.replace_key_in_all_files("version", self.version)
        
        # Delete old files
        self.cleanup()


# General purpose text stripper
def strip_all(input_text):
    return input_text.strip().strip("\n").strip("\r").strip()


# Interactive prompt
def user_prompt(prompt_text):
    prompt_text_stripped = strip_all(prompt_text)
    user_input = input(f"{prompt_text_stripped}: ")
    return strip_all(user_input)


# Tests if a version number is valid
def version_is_valid(version_number):
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", version_number):
        return True
    else:
        return False


def main(args):
    print()
    name = user_prompt("Project name (short, no spaces)")
    simple_name = user_prompt("User-friendly name")
    author = user_prompt("Project author")
    description = user_prompt("Project description")
    
    is_valid_version = False
    default_version = "1.0.0.0"
    while not is_valid_version:
        version = user_prompt(f"Starting version number [default: {default_version}]")
        if version == "":
            version = default_version
            is_valid_version = True
        elif not version_is_valid(version):
            print("  ERROR: Version number must be in the format #.#.#.#")
            print("  (four decimal numbers seperated by three periods)")
            print("  Please enter a valid version number, or press")
            print("  enter to accept the default value.")
        else:
            is_valid_version = True
    
    python_3_template_init = Python3TemplateInit(
        name=name, 
        simple_name=simple_name,
        author=author,
        description=description,
        version=version)
    
    python_3_template_init.run()


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
