#! /usr/bin env python3
# coding: utf-8

import sys
import cx_Freeze as cx


base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = [
    "pygame", "os"
]

include_files = ("resources", "README.md",)

options = {
    'build_exe': {
        'includes': includes,
        'include_files': include_files,
    }
}

executable = cx.Executable(
    base=base,
    script="main.py",
    targetName="mac_gyver.exe",
)

cx.setup(
    name="MacGyver",
    version="0.1",
    description="MacGyver maze game",
    options=options,
    executables=[executable],
)
