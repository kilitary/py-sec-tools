#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: entry
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_entry
else:
    import _ida_entry

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """
    Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass
    """
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """
    Meta class to enforce nondynamic attributes (no new attributes) for a class
    """
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

SWIG_PYTHON_LEGACY_BOOL = _ida_entry.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func


def get_entry_qty(*args) -> "size_t":
    r"""


    Get number of entry points.
    """
    return _ida_entry.get_entry_qty(*args)
AEF_UTF8 = _ida_entry.AEF_UTF8
"""
the name is given in UTF-8 (default)
"""

AEF_IDBENC = _ida_entry.AEF_IDBENC
"""
the name is given in the IDB encoding; non-ASCII bytes will be decoded
accordingly Specifying AEF_IDBENC also implies AEF_NODUMMY
"""

AEF_NODUMMY = _ida_entry.AEF_NODUMMY
"""
it begins with a dummy suffix. See also AEF_IDBENC

automatically prepend the name with '_' if
"""


def add_entry(*args) -> "bool":
    r"""


    Add an entry point to the list of entry points.
    
    add_entry(ord, ea, name, makecode, flags=0) -> bool
        @param ord: ordinal number if ordinal number is equal to 'ea' then
                    ordinal is not used (C++: uval_t)
        @param ea: linear address (C++: ea_t)
        @param name: name of entry point. If the specified location already
                     has a name, the old name will be appended to the regular
                     comment. If name == NULL, then the old name will be
                     retained. (C++: const char *)
        @param makecode: should the kernel convert bytes at the entry point to
                         instruction(s) (C++: bool)
        @param flags: See AEF_* (C++: int)
        @return: success (currently always true)
    """
    return _ida_entry.add_entry(*args)

def get_entry_ordinal(*args) -> "uval_t":
    r"""


    Get ordinal number of an entry point.
    
    get_entry_ordinal(idx) -> uval_t
        @param idx: internal number of entry point. Should be in the range 0..
                    get_entry_qty() -1 (C++: size_t)
        @return: ordinal number or 0.
    """
    return _ida_entry.get_entry_ordinal(*args)

def get_entry(*args) -> "ea_t":
    r"""


    Get entry point address by its ordinal
    
    get_entry(ord) -> ea_t
        @param ord: ordinal number of entry point (C++: uval_t)
        @return: address or  BADADDR
    """
    return _ida_entry.get_entry(*args)

def get_entry_name(*args) -> "qstring *":
    r"""


    Get name of the entry point by its ordinal.
    
    get_entry_name(ord) -> str
        @param ord: ordinal number of entry point (C++: uval_t)
        @return: size of entry name or -1
    """
    return _ida_entry.get_entry_name(*args)

def rename_entry(*args) -> "bool":
    r"""


    Rename entry point.
    
    rename_entry(ord, name, flags=0) -> bool
        @param ord: ordinal number of the entry point (C++: uval_t)
        @param name: name of entry point. If the specified location already
                     has a name, the old name will be appended to a repeatable
                     comment. (C++: const char *)
        @param flags: See AEF_* (C++: int)
        @return: success
    """
    return _ida_entry.rename_entry(*args)

def set_entry_forwarder(*args) -> "bool":
    r"""


    Set forwarder name for ordinal.
    
    set_entry_forwarder(ord, name, flags=0) -> bool
        @param ord: ordinal number of the entry point (C++: uval_t)
        @param name: forwarder name for entry point. (C++: const char *)
        @param flags: See AEF_* (C++: int)
        @return: success
    """
    return _ida_entry.set_entry_forwarder(*args)

def get_entry_forwarder(*args) -> "qstring *":
    r"""


    Get forwarder name for the entry point by its ordinal.
    
    get_entry_forwarder(ord) -> str
        @param ord: ordinal number of entry point (C++: uval_t)
        @return: size of entry forwarder name or -1
    """
    return _ida_entry.get_entry_forwarder(*args)
