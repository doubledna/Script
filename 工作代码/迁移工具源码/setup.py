# -*- coding: GBK -*-
from distutils.core import setup
import py2exe

setup(windows=[{"script":"gui.py"}],options = { "py2exe":{"dll_excludes":["MSVCP90.dll"],"includes":["sip"]}})

