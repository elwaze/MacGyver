#! /usr/bin env python3
# coding: utf-8

from cx_Freeze import setup, Executable

setup(
    name="MacGyver",
    version="0.1",
    description="MacGyver game",
    executables=[Executable("brouillon.py")],
)
