its.py
======

Python runtime environment flags.

Usage
-----

Usage is super simple::

    Python 2.7.3 (default, Apr 24 2012, 20:23:13)
    [GCC 4.2.1 Compatible Apple Clang 3.1 (tags/Apple/clang-318.0.58)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import its

    >>> its.py2
    True

    >>> its.py26
    False

    >>> its.py27
    True

    >>> its.pypy
    False

    >>> its.osx
    True
    
    >>> its.bit64
    True
    
    >>> its.little_endian
    True



Installation
------------

Installation is simple with pip::

    $ pip install its

