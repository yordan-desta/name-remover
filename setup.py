import sys, platform
from cx_Freeze import setup, Executable


def getTargetName():
    myOS = platform.system()
    if myOS == 'Linux':
        return "name_remover"
    elif myOS == 'Windows':
        return "name_remover.exe"
    else:
        return "name_remover.dmg"


base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script="__init__.py", base=base, targetName=getTargetName())

build_exe_options = {"packages": ["re", "sip"],
                     "includes": ["PyQt4.QtCore","PyQt4.QtGui","atexit"]
                     }

setup(name="setup",
      version="1.0",
      description="Name Remover Application",
      options={"build_exe": build_exe_options},
      executables=[exe])
