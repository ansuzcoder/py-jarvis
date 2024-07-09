"""
Allow JARVIS to perform actions
such as opening applications
"""


import sys
import os
import subprocess as sp


paths = {
    "Opera": "your path to Opera",
    "Discord": "your path to Discord",
    "Obsidian": "your path to Obsidian",
    "Calculator": "C:\\Windows\\System32\\calc.exe"
}


def open_cmd():
    """
    Open command line
    """
    os.system('start cmd')


def open_camera():
    """
    Open device camera
    """
    sp.run("start microsoft.windows.camera:", shell=True)


def open_calculator():
    """
    Open calculator
    """
    sp.Popen(paths['Calculator'])


def open_obsidian():
    """
    Run Obsidian Notes
    """
    os.startfile(paths["Obsidian"])


def open_discord():
    """
    Run Discord
    """
    os.startfile(paths["Discord"])