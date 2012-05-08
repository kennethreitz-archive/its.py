# -*- coding: utf-8 -*-

"""
is.py
~~~~~

System environment flags.
"""


import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
py2 = (_ver[0] == 2)

#: Python 3.x?
py3 = (_ver[0] == 3)

#: Python 3.0.x
py30 = (py3 and _ver[1] == 0)

#: Python 3.1.x
py31 = (py3 and _ver[1] == 1)

#: Python 3.2.x
py32 = (py3 and _ver[1] == 2)

#: Python 3.3.x
py33 = (py3 and _ver[1] == 3)

#: Python 3.4.x
py34 = (py3 and _ver[1] == 4)

#: Python 2.7.x
py27 = (py2 and _ver[1] == 7)

#: Python 2.6.x
py26 = (py2 and _ver[1] == 6)

#: Python 2.5.x
py25 = (py2 and _ver[1] == 5)

#: Python 2.4.x
py24 = (py2 and _ver[1] == 4)   # I'm assuming this is not by choice.


# ---------
# Platforms
# ---------


# Syntax sugar.
_ver = sys.version.lower()

pypy = ('pypy' in _ver)
jython = ('jython' in _ver)
ironpython = ('iron' in _ver)

# Assume CPython, if nothing else.
cpython = not any((pypy, jython, ironpython))

# Windows-based system.
windows = 'win32' in str(sys.platform).lower()

# Standard Linux 2+ system.
linux = ('linux' in str(sys.platform).lower())
osx = ('darwin' in str(sys.platform).lower())
hpux = ('hpux' in str(sys.platform).lower())   # Complete guess.
solaris = ('solaris' in str(sys.platform).lower())   # Complete guess.

