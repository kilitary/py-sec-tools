# revised WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: xref
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_xref
else:
    import _ida_xref

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


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

SWIG_PYTHON_LEGACY_BOOL = _ida_xref.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func


def create_switch_xrefs(*args):
    r"""


    create_switch_xrefs(ea, si) -> bool
    This function creates xrefs from the indirect jump.
    
    Usually there is no need to call this function directly because the kernel
    will call it for switch tables
    
    Note: Custom switch information are not supported yet.
    
    @param ea: address of the 'indirect jump' instruction
    @param si: switch information
    
    @return: Boolean
    """
    return _ida_xref.create_switch_xrefs(*args)
class cases_and_targets_t(object):
    r"""
    Proxy of C++ cases_and_targets_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    cases = property(_ida_xref.cases_and_targets_t_cases_get, _ida_xref.cases_and_targets_t_cases_set)
    targets = property(_ida_xref.cases_and_targets_t_targets_get, _ida_xref.cases_and_targets_t_targets_set)

    def __init__(self, *args):
        r"""
        __init__(self) -> cases_and_targets_t
        """
        _ida_xref.cases_and_targets_t_swiginit(self, _ida_xref.new_cases_and_targets_t(*args))
    __swig_destroy__ = _ida_xref.delete_cases_and_targets_t

# Register cases_and_targets_t in _ida_xref:
_ida_xref.cases_and_targets_t_swigregister(cases_and_targets_t)


def calc_switch_cases(*args):
    r"""


    calc_switch_cases(ea, si) -> cases_and_targets_t
    Get information about a switch's cases.
    
    The returned information can be used as follows:
    
        for idx in range(len(results.cases)):
            cur_case = results.cases[idx]
            for cidx in range(len(cur_case)):
                print("case: %d" % cur_case[cidx])
            print("  goto 0x%x" % results.targets[idx])
    
    @param ea: address of the 'indirect jump' instruction
    @param si: switch information
    
    @return: a structure with 2 members: 'cases', and 'targets'.
    """
    return _ida_xref.calc_switch_cases(*args)

def create_switch_table(*args):
    r"""


    create_switch_table(ea, si) -> bool
    Create switch table from the switch information
    
    @param ea: address of the 'indirect jump' instruction
    @param si: switch information
    
    @return: Boolean
    """
    return _ida_xref.create_switch_table(*args)
fl_U = _ida_xref.fl_U

fl_CF = _ida_xref.fl_CF

fl_CN = _ida_xref.fl_CN

fl_JF = _ida_xref.fl_JF

fl_JN = _ida_xref.fl_JN

fl_USobsolete = _ida_xref.fl_USobsolete

fl_F = _ida_xref.fl_F

dr_U = _ida_xref.dr_U

dr_O = _ida_xref.dr_O

dr_W = _ida_xref.dr_W

dr_R = _ida_xref.dr_R

dr_T = _ida_xref.dr_T

dr_I = _ida_xref.dr_I

dr_S = _ida_xref.dr_S

XREF_USER = _ida_xref.XREF_USER
"""
User specified xref. This xref will not be deleted by IDA. This bit
should be combined with the existing xref types ( 'cref_t' & 'dref_t'
) Cannot be used for fl_F xrefs
"""

XREF_TAIL = _ida_xref.XREF_TAIL
"""
Reference to tail byte in extrn symbols.
"""

XREF_BASE = _ida_xref.XREF_BASE
"""
Reference to the base part of an offset.
"""

XREF_MASK = _ida_xref.XREF_MASK
"""
Mask to get xref type.
"""

XREF_PASTEND = _ida_xref.XREF_PASTEND
"""
Reference is past item. This bit may be passed to 'add_dref()'
functions but it won't be saved in the database. It will prevent the
destruction of eventual alignment directives.
"""


def xrefchar(*args):
    r"""


    Get character describing the xref type.
    
    xrefchar(xrtype) -> char
        @param xrtype: combination of  Cross-Reference type flags  and a
                       cref_t  of  dref_t  value (C++: char)
    """
    return _ida_xref.xrefchar(*args)

def add_cref(*args):
    r"""


    Create a code cross-reference.
    
    add_cref(frm, to, type) -> bool
        @param frm: linear address of referencing instruction (C++: ea_t)
        @param to: linear address of referenced instruction (C++: ea_t)
        @param type: cross-reference type (C++: cref_t)
        @return: success
    """
    return _ida_xref.add_cref(*args)

def del_cref(*args):
    r"""


    Delete a code cross-reference.
    
    del_cref(frm, to, expand) -> bool
        @param frm: linear address of referencing instruction (C++: ea_t)
        @param to: linear address of referenced instruction (C++: ea_t)
        @param expand: policy to delete the referenced instruction   1: plan
                       to delete the referenced instruction if it has no more
                       references.   0: don't delete the referenced
                       instruction even if no more cross-references point to
                       it (C++: bool)
        @retval: true - if the referenced instruction will be deleted
    """
    return _ida_xref.del_cref(*args)

def add_dref(*args):
    r"""


    Create a data cross-reference.
    
    add_dref(frm, to, type) -> bool
        @param frm: linear address of referencing instruction or data (C++:
                    ea_t)
        @param to: linear address of referenced data (C++: ea_t)
        @param type: cross-reference type (C++: dref_t)
        @return: success (may fail if user-defined xref exists from->to)
    """
    return _ida_xref.add_dref(*args)

def del_dref(*args):
    r"""


    Delete a data cross-reference.
    
    del_dref(frm, to)
        @param frm: linear address of referencing instruction or data (C++:
                    ea_t)
        @param to: linear address of referenced data (C++: ea_t)
    """
    return _ida_xref.del_dref(*args)
class xrefblk_t(object):
    r"""
    Proxy of C++ xrefblk_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    frm = property(_ida_xref.xrefblk_t_frm_get, _ida_xref.xrefblk_t_frm_set)
    to = property(_ida_xref.xrefblk_t_to_get, _ida_xref.xrefblk_t_to_set)
    iscode = property(_ida_xref.xrefblk_t_iscode_get, _ida_xref.xrefblk_t_iscode_set)
    type = property(_ida_xref.xrefblk_t_type_get, _ida_xref.xrefblk_t_type_set)
    user = property(_ida_xref.xrefblk_t_user_get, _ida_xref.xrefblk_t_user_set)

    def first_from(self, *args):
        r"""


        first_from(self, _from, flags) -> bool
            _from: ea_t
            flags: int
        """
        return _ida_xref.xrefblk_t_first_from(self, *args)

    def first_to(self, *args):
        r"""


        first_to(self, _to, flags) -> bool
            _to: ea_t
            flags: int
        """
        return _ida_xref.xrefblk_t_first_to(self, *args)

    def next_from(self, *args):
        r"""


        next_from(self) -> bool
            _from: ea_t
            _to: ea_t
            flags: int
        """
        return _ida_xref.xrefblk_t_next_from(self, *args)

    def next_to(self, *args):
        r"""


        next_to(self) -> bool
            _from: ea_t
            _to: ea_t
            flags: int
        """
        return _ida_xref.xrefblk_t_next_to(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> xrefblk_t
        """
        _ida_xref.xrefblk_t_swiginit(self, _ida_xref.new_xrefblk_t(*args))
    __swig_destroy__ = _ida_xref.delete_xrefblk_t

# Register xrefblk_t in _ida_xref:
_ida_xref.xrefblk_t_swigregister(xrefblk_t)
XREF_ALL = _ida_xref.XREF_ALL
"""
return all references
"""

XREF_FAR = _ida_xref.XREF_FAR
"""
don't return ordinary flow xrefs
"""

XREF_DATA = _ida_xref.XREF_DATA
"""
return data references only
"""



def get_first_dref_from(*args):
    r"""


    Get first data referenced from the specified address.
    
    get_first_dref_from(frm) -> ea_t
        @param frm: linear address of referencing instruction or data (C++:
                    ea_t)
        @return: linear address of first (lowest) data referenced from the
                 specified address. Return  BADADDR  if the specified
                 instruction/data doesn't reference to anything.
    """
    return _ida_xref.get_first_dref_from(*args)

def get_next_dref_from(*args):
    r"""


    Get next data referenced from the specified address.
    
    get_next_dref_from(frm, current) -> ea_t
        @param frm: linear address of referencing instruction or data (C++:
                    ea_t)
        @param current: linear address of current referenced data. This value
                        is returned by  get_first_dref_from()  or previous
                        call to  get_next_dref_from()  functions. (C++: ea_t)
        @return: linear address of next data or  BADADDR .
    """
    return _ida_xref.get_next_dref_from(*args)

def get_first_dref_to(*args):
    r"""


    Get address of instruction/data referencing to the specified data.
    
    get_first_dref_to(to) -> ea_t
        @param to: linear address of referencing instruction or data (C++:
                   ea_t)
        @return: BADADDR  if nobody refers to the specified data.
    """
    return _ida_xref.get_first_dref_to(*args)

def get_next_dref_to(*args):
    r"""


    Get address of instruction/data referencing to the specified data
    
    get_next_dref_to(to, current) -> ea_t
        @param to: linear address of referencing instruction or data (C++:
                   ea_t)
        @param current: current linear address. This value is returned by
                        get_first_dref_to()  or previous call to
                        get_next_dref_to()  functions. (C++: ea_t)
        @return: BADADDR  if nobody refers to the specified data.
    """
    return _ida_xref.get_next_dref_to(*args)

def get_first_cref_from(*args):
    r"""


    Get first instruction referenced from the specified instruction. If
    the specified instruction passes execution to the next instruction
    then the next instruction is returned. Otherwise the lowest referenced
    address is returned (remember that xrefs are kept sorted!).
    
    get_first_cref_from(frm) -> ea_t
        @param frm: linear address of referencing instruction (C++: ea_t)
        @return: first referenced address. If the specified instruction
                 doesn't reference to other instructions then returns  BADADDR
                 .
    """
    return _ida_xref.get_first_cref_from(*args)

def get_next_cref_from(*args):
    r"""


    Get next instruction referenced from the specified instruction.
    
    get_next_cref_from(frm, current) -> ea_t
        @param frm: linear address of referencing instruction (C++: ea_t)
        @param current: linear address of current referenced instruction This
                        value is returned by  get_first_cref_from()  or
                        previous call to  get_next_cref_from()  functions.
                        (C++: ea_t)
        @return: next referenced address or  BADADDR .
    """
    return _ida_xref.get_next_cref_from(*args)

def get_first_cref_to(*args):
    r"""


    Get first instruction referencing to the specified instruction. If the
    specified instruction may be executed immediately after its previous
    instruction then the previous instruction is returned. Otherwise the
    lowest referencing address is returned. (remember that xrefs are kept
    sorted!).
    
    get_first_cref_to(to) -> ea_t
        @param to: linear address of referenced instruction (C++: ea_t)
        @return: linear address of the first referencing instruction or
                 BADADDR .
    """
    return _ida_xref.get_first_cref_to(*args)

def get_next_cref_to(*args):
    r"""


    Get next instruction referencing to the specified instruction.
    
    get_next_cref_to(to, current) -> ea_t
        @param to: linear address of referenced instruction (C++: ea_t)
        @param current: linear address of current referenced instruction This
                        value is returned by  get_first_cref_to()  or previous
                        call to  get_next_cref_to()  functions. (C++: ea_t)
        @return: linear address of the next referencing instruction or
                 BADADDR .
    """
    return _ida_xref.get_next_cref_to(*args)

def get_first_fcref_from(*args):
    r"""


    get_first_fcref_from(frm) -> ea_t
        @param frm (C++: ea_t)
    """
    return _ida_xref.get_first_fcref_from(*args)

def get_next_fcref_from(*args):
    r"""


    get_next_fcref_from(frm, current) -> ea_t
        @param frm (C++: ea_t)
        @param current (C++: ea_t)
    """
    return _ida_xref.get_next_fcref_from(*args)

def get_first_fcref_to(*args):
    r"""


    get_first_fcref_to(to) -> ea_t
        @param to (C++: ea_t)
    """
    return _ida_xref.get_first_fcref_to(*args)

def get_next_fcref_to(*args):
    r"""


    get_next_fcref_to(to, current) -> ea_t
        @param to (C++: ea_t)
        @param current (C++: ea_t)
    """
    return _ida_xref.get_next_fcref_to(*args)

def has_external_refs(*args):
    r"""


    Has a location external to the function references?
    
    has_external_refs(pfn, ea) -> bool
        @param pfn (C++: func_t  *)
        @param ea (C++: ea_t)
    """
    return _ida_xref.has_external_refs(*args)

def delete_switch_table(*args):
    r"""


    delete_switch_table(jump_ea, si)
        jump_ea: ea_t
        si: switch_info_t const &
    """
    return _ida_xref.delete_switch_table(*args)
class casevec_t(object):
    r"""
    Proxy of C++ qvector< qvector< sval_t > > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self) -> casevec_t
            x: qvector< qvector< long long > > const &
        """
        _ida_xref.casevec_t_swiginit(self, _ida_xref.new_casevec_t(*args))
    __swig_destroy__ = _ida_xref.delete_casevec_t

    def push_back(self, *args):
        r"""


        push_back(self, x)
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_xref.casevec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_xref.casevec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_xref.casevec_t_empty(self, *args)

    def at(self, *args):
        r"""


        at(self, _idx) -> qvector< long long > const &
            _idx: size_t
        """
        return _ida_xref.casevec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_xref.casevec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_xref.casevec_t_clear(self, *args)

    def resize(self, *args):
        r"""


        resize(self, _newsize, x)
            _newsize: size_t
            x: qvector< long long > const &
        

        resize(self, _newsize)
            _newsize: size_t
        """
        return _ida_xref.casevec_t_resize(self, *args)

    def grow(self, *args):
        r"""


        grow(self, x=qvector< long long >())
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_xref.casevec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""


        reserve(self, cnt)
            cnt: size_t
        """
        return _ida_xref.casevec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_xref.casevec_t_truncate(self, *args)

    def swap(self, *args):
        r"""


        swap(self, r)
            r: qvector< qvector< long long > > &
        """
        return _ida_xref.casevec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> qvector< long long > *
        """
        return _ida_xref.casevec_t_extract(self, *args)

    def inject(self, *args):
        r"""


        inject(self, s, len)
            s: qvector< long long > *
            len: size_t
        """
        return _ida_xref.casevec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""


        __eq__(self, r) -> bool
            r: qvector< qvector< long long > > const &
        """
        return _ida_xref.casevec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""


        __ne__(self, r) -> bool
            r: qvector< qvector< long long > > const &
        """
        return _ida_xref.casevec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< qvector< long long > >::iterator
        begin(self) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< qvector< long long > >::iterator
        end(self) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_end(self, *args)

    def insert(self, *args):
        r"""


        insert(self, it, x) -> qvector< qvector< long long > >::iterator
            it: qvector< qvector< long long > >::iterator
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_insert(self, *args)

    def erase(self, *args):
        r"""


        erase(self, it) -> qvector< qvector< long long > >::iterator
            it: qvector< qvector< long long > >::iterator
        

        erase(self, first, last) -> qvector< qvector< long long > >::iterator
            first: qvector< qvector< long long > >::iterator
            last: qvector< qvector< long long > >::iterator
        """
        return _ida_xref.casevec_t_erase(self, *args)

    def find(self, *args):
        r"""


        find(self, x) -> qvector< qvector< long long > >::iterator
            x: qvector< long long > const &
        

        find(self, x) -> qvector< qvector< long long > >::const_iterator
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_find(self, *args)

    def has(self, *args):
        r"""


        has(self, x) -> bool
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_has(self, *args)

    def add_unique(self, *args):
        r"""


        add_unique(self, x) -> bool
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""


        _del(self, x) -> bool
            x: qvector< long long > const &
        """
        return _ida_xref.casevec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_xref.casevec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""


        __getitem__(self, i) -> qvector< long long > const &
            i: size_t
        """
        return _ida_xref.casevec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: qvector< long long > const &
        """
        return _ida_xref.casevec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register casevec_t in _ida_xref:
_ida_xref.casevec_t_swigregister(casevec_t)


#<pycode(py_xref)>

import ida_idaapi
ida_idaapi._listify_types(
        casevec_t)

#</pycode(py_xref)>
