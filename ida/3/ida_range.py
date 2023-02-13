#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: range
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_range
else:
    import _ida_range

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

SWIG_PYTHON_LEGACY_BOOL = _ida_range.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class rangevec_base_t(object):
    r"""
    Proxy of C++ qvector< range_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self) -> rangevec_base_t
            x: qvector< range_t > const &
        """
        _ida_range.rangevec_base_t_swiginit(self, _ida_range.new_rangevec_base_t(*args))
    __swig_destroy__ = _ida_range.delete_rangevec_base_t

    def push_back(self, *args) -> "range_t &":
        r"""


        push_back(self, x)
            x: range_t const &
        """
        return _ida_range.rangevec_base_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_range.rangevec_base_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_range.rangevec_base_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_range.rangevec_base_t_empty(self, *args)

    def at(self, *args) -> "range_t const &":
        r"""


        at(self, _idx) -> range_t
            _idx: size_t
        """
        return _ida_range.rangevec_base_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_range.rangevec_base_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_range.rangevec_base_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""


        resize(self, _newsize, x)
            _newsize: size_t
            x: range_t const &
        

        resize(self, _newsize)
            _newsize: size_t
        """
        return _ida_range.rangevec_base_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""


        grow(self, x=range_t())
            x: range_t const &
        """
        return _ida_range.rangevec_base_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_range.rangevec_base_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""


        reserve(self, cnt)
            cnt: size_t
        """
        return _ida_range.rangevec_base_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_range.rangevec_base_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""


        swap(self, r)
            r: qvector< range_t > &
        """
        return _ida_range.rangevec_base_t_swap(self, *args)

    def extract(self, *args) -> "range_t *":
        r"""
        extract(self) -> range_t
        """
        return _ida_range.rangevec_base_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""


        inject(self, s, len)
            s: range_t *
            len: size_t
        """
        return _ida_range.rangevec_base_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""


        __eq__(self, r) -> bool
            r: qvector< range_t > const &
        """
        return _ida_range.rangevec_base_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""


        __ne__(self, r) -> bool
            r: qvector< range_t > const &
        """
        return _ida_range.rangevec_base_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< range_t >::const_iterator":
        r"""
        begin(self) -> range_t
        begin(self) -> range_t
        """
        return _ida_range.rangevec_base_t_begin(self, *args)

    def end(self, *args) -> "qvector< range_t >::const_iterator":
        r"""
        end(self) -> range_t
        end(self) -> range_t
        """
        return _ida_range.rangevec_base_t_end(self, *args)

    def insert(self, *args) -> "qvector< range_t >::iterator":
        r"""


        insert(self, it, x) -> range_t
            it: qvector< range_t >::iterator
            x: range_t const &
        """
        return _ida_range.rangevec_base_t_insert(self, *args)

    def erase(self, *args) -> "qvector< range_t >::iterator":
        r"""


        erase(self, it) -> range_t
            it: qvector< range_t >::iterator
        

        erase(self, first, last) -> range_t
            first: qvector< range_t >::iterator
            last: qvector< range_t >::iterator
        """
        return _ida_range.rangevec_base_t_erase(self, *args)

    def find(self, *args) -> "qvector< range_t >::const_iterator":
        r"""


        find(self, x) -> range_t
            x: range_t const &
        

        find(self, x) -> range_t
            x: range_t const &
        """
        return _ida_range.rangevec_base_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""


        has(self, x) -> bool
            x: range_t const &
        """
        return _ida_range.rangevec_base_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""


        add_unique(self, x) -> bool
            x: range_t const &
        """
        return _ida_range.rangevec_base_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""


        _del(self, x) -> bool
            x: range_t const &
        """
        return _ida_range.rangevec_base_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_range.rangevec_base_t___len__(self, *args)

    def __getitem__(self, *args) -> "range_t const &":
        r"""


        __getitem__(self, i) -> range_t
            i: size_t
        """
        return _ida_range.rangevec_base_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: range_t const &
        """
        return _ida_range.rangevec_base_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register rangevec_base_t in _ida_range:
_ida_range.rangevec_base_t_swigregister(rangevec_base_t)

class array_of_rangesets(object):
    r"""
    Proxy of C++ qvector< rangeset_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self) -> array_of_rangesets
            x: qvector< rangeset_t > const &
        """
        _ida_range.array_of_rangesets_swiginit(self, _ida_range.new_array_of_rangesets(*args))
    __swig_destroy__ = _ida_range.delete_array_of_rangesets

    def push_back(self, *args) -> "rangeset_t &":
        r"""


        push_back(self, x)
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_range.array_of_rangesets_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_range.array_of_rangesets_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_range.array_of_rangesets_empty(self, *args)

    def at(self, *args) -> "rangeset_t const &":
        r"""


        at(self, _idx) -> rangeset_t
            _idx: size_t
        """
        return _ida_range.array_of_rangesets_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_range.array_of_rangesets_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_range.array_of_rangesets_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""


        resize(self, _newsize, x)
            _newsize: size_t
            x: rangeset_t const &
        

        resize(self, _newsize)
            _newsize: size_t
        """
        return _ida_range.array_of_rangesets_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""


        grow(self, x=rangeset_t())
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_range.array_of_rangesets_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""


        reserve(self, cnt)
            cnt: size_t
        """
        return _ida_range.array_of_rangesets_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_range.array_of_rangesets_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""


        swap(self, r)
            r: qvector< rangeset_t > &
        """
        return _ida_range.array_of_rangesets_swap(self, *args)

    def extract(self, *args) -> "rangeset_t *":
        r"""
        extract(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""


        inject(self, s, len)
            s: rangeset_t *
            len: size_t
        """
        return _ida_range.array_of_rangesets_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""


        __eq__(self, r) -> bool
            r: qvector< rangeset_t > const &
        """
        return _ida_range.array_of_rangesets___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""


        __ne__(self, r) -> bool
            r: qvector< rangeset_t > const &
        """
        return _ida_range.array_of_rangesets___ne__(self, *args)

    def begin(self, *args) -> "qvector< rangeset_t >::const_iterator":
        r"""
        begin(self) -> rangeset_t
        begin(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_begin(self, *args)

    def end(self, *args) -> "qvector< rangeset_t >::const_iterator":
        r"""
        end(self) -> rangeset_t
        end(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_end(self, *args)

    def insert(self, *args) -> "qvector< rangeset_t >::iterator":
        r"""


        insert(self, it, x) -> rangeset_t
            it: qvector< rangeset_t >::iterator
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_insert(self, *args)

    def erase(self, *args) -> "qvector< rangeset_t >::iterator":
        r"""


        erase(self, it) -> rangeset_t
            it: qvector< rangeset_t >::iterator
        

        erase(self, first, last) -> rangeset_t
            first: qvector< rangeset_t >::iterator
            last: qvector< rangeset_t >::iterator
        """
        return _ida_range.array_of_rangesets_erase(self, *args)

    def find(self, *args) -> "qvector< rangeset_t >::const_iterator":
        r"""


        find(self, x) -> rangeset_t
            x: rangeset_t const &
        

        find(self, x) -> rangeset_t
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_find(self, *args)

    def has(self, *args) -> "bool":
        r"""


        has(self, x) -> bool
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""


        add_unique(self, x) -> bool
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""


        _del(self, x) -> bool
            x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_range.array_of_rangesets___len__(self, *args)

    def __getitem__(self, *args) -> "rangeset_t const &":
        r"""


        __getitem__(self, i) -> rangeset_t
            i: size_t
        """
        return _ida_range.array_of_rangesets___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: rangeset_t const &
        """
        return _ida_range.array_of_rangesets___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register array_of_rangesets in _ida_range:
_ida_range.array_of_rangesets_swigregister(array_of_rangesets)


#<pycode(py_range)>
import ida_idaapi
#</pycode(py_range)>

class range_t(object):
    r"""
    Proxy of C++ range_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    start_ea = property(_ida_range.range_t_start_ea_get, _ida_range.range_t_start_ea_set)
    end_ea = property(_ida_range.range_t_end_ea_get, _ida_range.range_t_end_ea_set)

    def __init__(self, *args):
        r"""


        __init__(self) -> range_t
            ea1: ea_t
            ea2: ea_t
        """
        _ida_range.range_t_swiginit(self, _ida_range.new_range_t(*args))

    def compare(self, *args) -> "int":
        r"""


        Compare two 'range_t' instances, based on the start_ea.
        
        compare(self, r) -> int
            @param r (C++: const  range_t  &)
        """
        return _ida_range.range_t_compare(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""


        __eq__(self, r) -> bool
            r: range_t const &
        """
        return _ida_range.range_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""


        __ne__(self, r) -> bool
            r: range_t const &
        """
        return _ida_range.range_t___ne__(self, *args)

    def __gt__(self, *args) -> "bool":
        r"""


        __gt__(self, r) -> bool
            r: range_t const &
        """
        return _ida_range.range_t___gt__(self, *args)

    def __lt__(self, *args) -> "bool":
        r"""


        __lt__(self, r) -> bool
            r: range_t const &
        """
        return _ida_range.range_t___lt__(self, *args)

    def contains(self, *args) -> "bool":
        r"""


        Is 'ea' in the address range?
        
        contains(self, ea) -> bool
            @param ea (C++: ea_t)
        

        contains(self, r) -> bool
            r: range_t const &
        """
        return _ida_range.range_t_contains(self, *args)

    def overlaps(self, *args) -> "bool":
        r"""


        Is there an ea in 'r' that is also in this 'range_t' ?
        
        overlaps(self, r) -> bool
            @param r (C++: const  range_t  &)
        """
        return _ida_range.range_t_overlaps(self, *args)

    def clear(self, *args) -> "void":
        r"""


        Set 'start_ea' , 'end_ea' to 0.
        """
        return _ida_range.range_t_clear(self, *args)

    def empty(self, *args) -> "bool":
        r"""


        Is the size of the 'range_t' <= 0?
        """
        return _ida_range.range_t_empty(self, *args)

    def size(self, *args) -> "asize_t":
        r"""


        Get 'end_ea' - 'start_ea' .
        """
        return _ida_range.range_t_size(self, *args)

    def intersect(self, *args) -> "void":
        r"""


        Assign the 'range_t' to the intersection between the 'range_t' and
        'r'.
        
        intersect(self, r)
            @param r (C++: const  range_t  &)
        """
        return _ida_range.range_t_intersect(self, *args)

    def extend(self, *args) -> "void":
        r"""


        Ensure that the 'range_t' includes 'ea'.
        
        extend(self, ea)
            @param ea (C++: ea_t)
        """
        return _ida_range.range_t_extend(self, *args)

    def _print(self, *args) -> "size_t":
        r"""
        _print(self) -> size_t
        """
        return _ida_range.range_t__print(self, *args)

    startEA = ida_idaapi._make_badattr_property("startEA", "start_ea")
    endEA = ida_idaapi._make_badattr_property("endEA", "end_ea")

    __swig_destroy__ = _ida_range.delete_range_t

# Register range_t in _ida_range:
_ida_range.range_t_swigregister(range_t)

def range_t_print(*args) -> "size_t":
    r"""


    Helper function. Should not be called directly!
    
    range_t_print(cb) -> str
        cb: range_t const *
    """
    return _ida_range.range_t_print(*args)

class rangevec_t(rangevec_base_t):
    r"""
    Proxy of C++ rangevec_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> rangevec_t
        """
        _ida_range.rangevec_t_swiginit(self, _ida_range.new_rangevec_t(*args))
    __swig_destroy__ = _ida_range.delete_rangevec_t

# Register rangevec_t in _ida_range:
_ida_range.rangevec_t_swigregister(rangevec_t)

RANGE_KIND_UNKNOWN = _ida_range.RANGE_KIND_UNKNOWN

RANGE_KIND_FUNC = _ida_range.RANGE_KIND_FUNC

RANGE_KIND_SEGMENT = _ida_range.RANGE_KIND_SEGMENT

RANGE_KIND_HIDDEN_RANGE = _ida_range.RANGE_KIND_HIDDEN_RANGE

class rangeset_t(object):
    r"""
    Proxy of C++ rangeset_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self) -> rangeset_t
            range: range_t const &
        

        __init__(self, ivs) -> rangeset_t
            ivs: rangeset_t const &
        """
        _ida_range.rangeset_t_swiginit(self, _ida_range.new_rangeset_t(*args))

    def swap(self, *args) -> "void":
        r"""


        Set this = 'r' and 'r' = this. See 'qvector::swap()'
        
        swap(self, r)
            @param r (C++: rangeset_t  &)
        """
        return _ida_range.rangeset_t_swap(self, *args)

    def add(self, *args) -> "bool":
        r"""


        Add an address range to the set. If 'range' intersects an existing
        element e, then e is extended to include 'range', and any superfluous
        elements (subsets of e) are removed.
        
        add(self, range) -> bool
            @param range: address range to add. cannot be empty (C++: const
                          range_t  &)
            @return: false if no elements were added (the set was unchanged)
        

        add(self, start, _end) -> bool
            start: ea_t
            _end: ea_t
            @return: false if no elements were added (the set was unchanged)
        

        add(self, aset) -> bool
            aset: rangeset_t const &
            @return: false if no elements were added (the set was unchanged)
        """
        return _ida_range.rangeset_t_add(self, *args)

    def sub(self, *args) -> "bool":
        r"""


        Subtract an address range from the set. All subsets of 'range' will be
        removed, and all elements that intersect 'range' will be
        truncated/split so they do not include 'range'.
        
        sub(self, range) -> bool
            @param range: address range to subtract. cannot be empty. (C++: const
                          range_t  &)
            @return: false if nothing was subtracted (the set was unchanged)
        

        sub(self, ea) -> bool
            ea: ea_t
            @return: false if nothing was subtracted (the set was unchanged)
        

        sub(self, aset) -> bool
            aset: rangeset_t const &
            @return: false if nothing was subtracted (the set was unchanged)
        """
        return _ida_range.rangeset_t_sub(self, *args)

    def includes(self, *args) -> "bool":
        r"""


        Is every ea in 'range' contained in the rangeset?
        
        includes(self, range) -> bool
            @param range (C++: const  range_t  &)
        """
        return _ida_range.rangeset_t_includes(self, *args)

    def _print(self, *args) -> "size_t":
        r"""
        _print(self) -> size_t
        """
        return _ida_range.rangeset_t__print(self, *args)

    def getrange(self, *args) -> "range_t const &":
        r"""


        Get the 'range_t' at index 'idx'.
        
        getrange(self, idx) -> range_t
            @param idx (C++: int)
        """
        return _ida_range.rangeset_t_getrange(self, *args)

    def lastrange(self, *args) -> "range_t const &":
        r"""


        Get the last 'range_t' in the set.
        """
        return _ida_range.rangeset_t_lastrange(self, *args)

    def nranges(self, *args) -> "size_t":
        r"""


        Get the number of 'range_t' elements in the set.
        """
        return _ida_range.rangeset_t_nranges(self, *args)

    def empty(self, *args) -> "bool":
        r"""


        Does the set have zero elements.
        """
        return _ida_range.rangeset_t_empty(self, *args)

    def clear(self, *args) -> "void":
        r"""


        Delete all elements from the set. See 'qvector::clear()'
        """
        return _ida_range.rangeset_t_clear(self, *args)

    def has_common(self, *args) -> "bool":
        r"""


        Is there an ea in 'range' that is also in the rangeset?
        
        has_common(self, range) -> bool
            @param range (C++: const  range_t  &)
        

        has_common(self, aset) -> bool
            aset: rangeset_t const &
        """
        return _ida_range.rangeset_t_has_common(self, *args)

    def contains(self, *args) -> "bool":
        r"""


        Does an element of the rangeset contain 'ea'? See
        range_t::contains(ea_t)
        
        contains(self, ea) -> bool
            @param ea (C++: ea_t)
        

        contains(self, aset) -> bool
            aset: rangeset_t const &
        """
        return _ida_range.rangeset_t_contains(self, *args)

    def intersect(self, *args) -> "bool":
        r"""


        Set the rangeset to its intersection with 'aset'.
        
        intersect(self, aset) -> bool
            @param aset (C++: const  rangeset_t  &)
            @return: false if the set was unchanged
        """
        return _ida_range.rangeset_t_intersect(self, *args)

    def is_subset_of(self, *args) -> "bool":
        r"""


        Is every element in the rangeset contained in an element of 'aset'?
        
        is_subset_of(self, aset) -> bool
            @param aset (C++: const  rangeset_t  &)
        """
        return _ida_range.rangeset_t_is_subset_of(self, *args)

    def is_equal(self, *args) -> "bool":
        r"""


        Do this rangeset and 'aset' have identical elements?
        
        is_equal(self, aset) -> bool
            @param aset (C++: const  rangeset_t  &)
        """
        return _ida_range.rangeset_t_is_equal(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""


        __eq__(self, aset) -> bool
            aset: rangeset_t const &
        """
        return _ida_range.rangeset_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""


        __ne__(self, aset) -> bool
            aset: rangeset_t const &
        """
        return _ida_range.rangeset_t___ne__(self, *args)

    def begin(self, *args) -> "rangeset_t::iterator":
        r"""


        Get an iterator that points to the first element in the set.
        """
        return _ida_range.rangeset_t_begin(self, *args)

    def end(self, *args) -> "rangeset_t::iterator":
        r"""


        Get an iterator that points to the end of the set. (This is NOT the
        last element)
        """
        return _ida_range.rangeset_t_end(self, *args)

    def find_range(self, *args) -> "range_t const *":
        r"""


        Get the element from the set that contains 'ea'.
        
        find_range(self, ea) -> range_t
            @param ea (C++: ea_t)
            @return: NULL if there is no such element
        """
        return _ida_range.rangeset_t_find_range(self, *args)

    def cached_range(self, *args) -> "range_t const *":
        r"""


        When searching the rangeset, we keep a cached element to help speed up
        searches.
        """
        return _ida_range.rangeset_t_cached_range(self, *args)

    def next_addr(self, *args) -> "ea_t":
        r"""


        Get the smallest ea_t value greater than 'ea' contained in the
        rangeset.
        
        next_addr(self, ea) -> ea_t
            @param ea (C++: ea_t)
        """
        return _ida_range.rangeset_t_next_addr(self, *args)

    def prev_addr(self, *args) -> "ea_t":
        r"""


        Get the largest ea_t value less than 'ea' contained in the rangeset.
        
        prev_addr(self, ea) -> ea_t
            @param ea (C++: ea_t)
        """
        return _ida_range.rangeset_t_prev_addr(self, *args)

    def next_range(self, *args) -> "ea_t":
        r"""


        Get the smallest ea_t value greater than 'ea' that is not in the same
        range as 'ea'.
        
        next_range(self, ea) -> ea_t
            @param ea (C++: ea_t)
        """
        return _ida_range.rangeset_t_next_range(self, *args)

    def prev_range(self, *args) -> "ea_t":
        r"""


        Get the largest ea_t value less than 'ea' that is not in the same
        range as 'ea'.
        
        prev_range(self, ea) -> ea_t
            @param ea (C++: ea_t)
        """
        return _ida_range.rangeset_t_prev_range(self, *args)

    def __getitem__(self, idx):
        return self.getrange(idx)

    __len__ = nranges
    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_range.delete_rangeset_t

# Register rangeset_t in _ida_range:
_ida_range.rangeset_t_swigregister(rangeset_t)


if _BC695:
    import sys
    sys.modules["ida_area"] = sys.modules["ida_range"]
    area_t = range_t
    areaset_t = rangeset_t
    def __set_startEA(inst, v):
        inst.start_ea = v
    range_t.startEA = property(lambda self: self.start_ea, __set_startEA)
    def __set_endEA(inst, v):
        inst.end_ea = v
    range_t.endEA = property(lambda self: self.end_ea, __set_endEA)
