#!/usr/bin/python3
import os
import py_compile
import sys

def get_names_from_pyc(pyc_file):
    if not os.path.isfile(pyc_file):
        print(f"Error: '{pyc_file}' does not exist.")
        return []

    py_file = os.path.splitext(pyc_file)[0] + '.py'
    if not os.path.isfile(py_file):
        py_compile.compile(pyc_file, cfile=py_file)

    module_name = os.path.splitext(os.path.basename(py_file))[0]
    try:
        module = __import__(module_name)
    except ImportError:
        print(f"Error: Failed to import module '{module_name}'")
        return []

    names = [name for name in dir(module) if not name.startswith("__")]
    return sorted(names)

if __name__ == "__main__":
    pyc_file = "hidden_4.pyc"
    names = get_names_from_pyc(pyc_file)

    for name in names:
        print(name)
