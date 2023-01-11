#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: dirtree
"""

from sys import version_info as _swig_python_version_info

if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_dirtree
else:
    import _ida_dirtree

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

SWIG_PYTHON_LEGACY_BOOL = _ida_dirtree.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import sys

_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:
    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class direntry_vec_t(object):
    r"""
    Proxy of C++ qvector< direntry_t > class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    
    def __init__(self, *args):
        r"""


        __init__(self) -> direntry_vec_t
            x: qvector< direntry_t > const &
        """
        _ida_dirtree.direntry_vec_t_swiginit(self, _ida_dirtree.new_direntry_vec_t(*args))
    
    __swig_destroy__ = _ida_dirtree.delete_direntry_vec_t
    
    def push_back(self, *args):
        r"""


        push_back(self, x)
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_push_back(self, *args)
    
    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dirtree.direntry_vec_t_pop_back(self, *args)
    
    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dirtree.direntry_vec_t_size(self, *args)
    
    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dirtree.direntry_vec_t_empty(self, *args)
    
    def at(self, *args):
        r"""


        at(self, _idx) -> direntry_t
            _idx: size_t
        """
        return _ida_dirtree.direntry_vec_t_at(self, *args)
    
    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dirtree.direntry_vec_t_qclear(self, *args)
    
    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dirtree.direntry_vec_t_clear(self, *args)
    
    def resize(self, *args):
        r"""


        resize(self, _newsize, x)
            _newsize: size_t
            x: direntry_t const &
        

        resize(self, _newsize)
            _newsize: size_t
        """
        return _ida_dirtree.direntry_vec_t_resize(self, *args)
    
    def grow(self, *args):
        r"""


        grow(self, x=direntry_t())
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_grow(self, *args)
    
    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dirtree.direntry_vec_t_capacity(self, *args)
    
    def reserve(self, *args):
        r"""


        reserve(self, cnt)
            cnt: size_t
        """
        return _ida_dirtree.direntry_vec_t_reserve(self, *args)
    
    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dirtree.direntry_vec_t_truncate(self, *args)
    
    def swap(self, *args):
        r"""


        swap(self, r)
            r: qvector< direntry_t > &
        """
        return _ida_dirtree.direntry_vec_t_swap(self, *args)
    
    def extract(self, *args):
        r"""
        extract(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_extract(self, *args)
    
    def inject(self, *args):
        r"""


        inject(self, s, len)
            s: direntry_t *
            len: size_t
        """
        return _ida_dirtree.direntry_vec_t_inject(self, *args)
    
    def __eq__(self, *args):
        r"""


        __eq__(self, r) -> bool
            r: qvector< direntry_t > const &
        """
        return _ida_dirtree.direntry_vec_t___eq__(self, *args)
    
    def __ne__(self, *args):
        r"""


        __ne__(self, r) -> bool
            r: qvector< direntry_t > const &
        """
        return _ida_dirtree.direntry_vec_t___ne__(self, *args)
    
    def begin(self, *args):
        r"""
        begin(self) -> direntry_t
        begin(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_begin(self, *args)
    
    def end(self, *args):
        r"""
        end(self) -> direntry_t
        end(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_end(self, *args)
    
    def insert(self, *args):
        r"""


        insert(self, it, x) -> direntry_t
            it: qvector< direntry_t >::iterator
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_insert(self, *args)
    
    def erase(self, *args):
        r"""


        erase(self, it) -> direntry_t
            it: qvector< direntry_t >::iterator
        

        erase(self, first, last) -> direntry_t
            first: qvector< direntry_t >::iterator
            last: qvector< direntry_t >::iterator
        """
        return _ida_dirtree.direntry_vec_t_erase(self, *args)
    
    def find(self, *args):
        r"""


        find(self, x) -> direntry_t
            x: direntry_t const &
        

        find(self, x) -> direntry_t
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_find(self, *args)
    
    def has(self, *args):
        r"""


        has(self, x) -> bool
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_has(self, *args)
    
    def add_unique(self, *args):
        r"""


        add_unique(self, x) -> bool
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_add_unique(self, *args)
    
    def _del(self, *args):
        r"""


        _del(self, x) -> bool
            x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t__del(self, *args)
    
    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dirtree.direntry_vec_t___len__(self, *args)
    
    def __getitem__(self, *args):
        r"""


        __getitem__(self, i) -> direntry_t
            i: size_t
        """
        return _ida_dirtree.direntry_vec_t___getitem__(self, *args)
    
    def __setitem__(self, *args):
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t___setitem__(self, *args)
    
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

# Register direntry_vec_t in _ida_dirtree:
_ida_dirtree.direntry_vec_t_swigregister(direntry_vec_t)

class dirtree_cursor_vec_t(object):
    r"""
    Proxy of C++ qvector< dirtree_cursor_t > class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    
    def __init__(self, *args):
        r"""


        __init__(self) -> dirtree_cursor_vec_t
            x: qvector< dirtree_cursor_t > const &
        """
        _ida_dirtree.dirtree_cursor_vec_t_swiginit(self, _ida_dirtree.new_dirtree_cursor_vec_t(*args))
    
    __swig_destroy__ = _ida_dirtree.delete_dirtree_cursor_vec_t
    
    def push_back(self, *args):
        r"""


        push_back(self, x)
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_push_back(self, *args)
    
    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_pop_back(self, *args)
    
    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_size(self, *args)
    
    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dirtree.dirtree_cursor_vec_t_empty(self, *args)
    
    def at(self, *args):
        r"""


        at(self, _idx) -> dirtree_cursor_t
            _idx: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_at(self, *args)
    
    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_qclear(self, *args)
    
    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_clear(self, *args)
    
    def resize(self, *args):
        r"""


        resize(self, _newsize, x)
            _newsize: size_t
            x: dirtree_cursor_t const &
        

        resize(self, _newsize)
            _newsize: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_resize(self, *args)
    
    def grow(self, *args):
        r"""


        grow(self, x=dirtree_cursor_t())
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_grow(self, *args)
    
    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_capacity(self, *args)
    
    def reserve(self, *args):
        r"""


        reserve(self, cnt)
            cnt: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_reserve(self, *args)
    
    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_truncate(self, *args)
    
    def swap(self, *args):
        r"""


        swap(self, r)
            r: qvector< dirtree_cursor_t > &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_swap(self, *args)
    
    def extract(self, *args):
        r"""
        extract(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_extract(self, *args)
    
    def inject(self, *args):
        r"""


        inject(self, s, len)
            s: dirtree_cursor_t *
            len: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_inject(self, *args)
    
    def __eq__(self, *args):
        r"""


        __eq__(self, r) -> bool
            r: qvector< dirtree_cursor_t > const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t___eq__(self, *args)
    
    def __ne__(self, *args):
        r"""


        __ne__(self, r) -> bool
            r: qvector< dirtree_cursor_t > const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t___ne__(self, *args)
    
    def begin(self, *args):
        r"""
        begin(self) -> dirtree_cursor_t
        begin(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_begin(self, *args)
    
    def end(self, *args):
        r"""
        end(self) -> dirtree_cursor_t
        end(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_end(self, *args)
    
    def insert(self, *args):
        r"""


        insert(self, it, x) -> dirtree_cursor_t
            it: qvector< dirtree_cursor_t >::iterator
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_insert(self, *args)
    
    def erase(self, *args):
        r"""


        erase(self, it) -> dirtree_cursor_t
            it: qvector< dirtree_cursor_t >::iterator
        

        erase(self, first, last) -> dirtree_cursor_t
            first: qvector< dirtree_cursor_t >::iterator
            last: qvector< dirtree_cursor_t >::iterator
        """
        return _ida_dirtree.dirtree_cursor_vec_t_erase(self, *args)
    
    def find(self, *args):
        r"""


        find(self, x) -> dirtree_cursor_t
            x: dirtree_cursor_t const &
        

        find(self, x) -> dirtree_cursor_t
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_find(self, *args)
    
    def has(self, *args):
        r"""


        has(self, x) -> bool
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_has(self, *args)
    
    def add_unique(self, *args):
        r"""


        add_unique(self, x) -> bool
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_add_unique(self, *args)
    
    def _del(self, *args):
        r"""


        _del(self, x) -> bool
            x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t__del(self, *args)
    
    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t___len__(self, *args)
    
    def __getitem__(self, *args):
        r"""


        __getitem__(self, i) -> dirtree_cursor_t
            i: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t___getitem__(self, *args)
    
    def __setitem__(self, *args):
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t___setitem__(self, *args)
    
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

# Register dirtree_cursor_vec_t in _ida_dirtree:
_ida_dirtree.dirtree_cursor_vec_t_swigregister(dirtree_cursor_vec_t)

class direntry_t(object):
    r"""
    Proxy of C++ direntry_t class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    idx = property(_ida_dirtree.direntry_t_idx_get, _ida_dirtree.direntry_t_idx_set)
    isdir = property(_ida_dirtree.direntry_t_isdir_get, _ida_dirtree.direntry_t_isdir_set)
    BADIDX = _ida_dirtree.direntry_t_BADIDX
    
    ROOTIDX = _ida_dirtree.direntry_t_ROOTIDX
    
    def __init__(self, *args):
        r"""


        __init__(self, i=BADIDX, d=False) -> direntry_t
            i: uval_t
            d: bool
        """
        _ida_dirtree.direntry_t_swiginit(self, _ida_dirtree.new_direntry_t(*args))
    
    def valid(self, *args):
        r"""
        valid(self) -> bool
        """
        return _ida_dirtree.direntry_t_valid(self, *args)
    
    def __eq__(self, *args):
        r"""


        __eq__(self, r) -> bool
            r: direntry_t const &
        """
        return _ida_dirtree.direntry_t___eq__(self, *args)
    
    def __ne__(self, *args):
        r"""


        __ne__(self, r) -> bool
            r: direntry_t const &
        """
        return _ida_dirtree.direntry_t___ne__(self, *args)
    
    def __lt__(self, *args):
        r"""


        __lt__(self, r) -> bool
            r: direntry_t const &
        """
        return _ida_dirtree.direntry_t___lt__(self, *args)
    
    __swig_destroy__ = _ida_dirtree.delete_direntry_t

# Register direntry_t in _ida_dirtree:
_ida_dirtree.direntry_t_swigregister(direntry_t)

class dirspec_t(object):
    r"""
    Proxy of C++ dirspec_t class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    flags = property(_ida_dirtree.dirspec_t_flags_get, _ida_dirtree.dirspec_t_flags_set)
    DSF_INODE_EA = _ida_dirtree.dirspec_t_DSF_INODE_EA
    
    DSF_PRIVRANGE = _ida_dirtree.dirspec_t_DSF_PRIVRANGE
    
    nodename = property(_ida_dirtree.dirspec_t_nodename_get, _ida_dirtree.dirspec_t_nodename_set)
    
    def __init__(self, *args):
        r"""


        __init__(self, nm=None, f=0) -> dirspec_t
            nm: char const *
            f: uint32
        """
        if self.__class__ == dirspec_t:
            _self = None
        else:
            _self = self
        _ida_dirtree.dirspec_t_swiginit(self, _ida_dirtree.new_dirspec_t(_self, *args))
    
    __swig_destroy__ = _ida_dirtree.delete_dirspec_t
    
    def get_name(self, *args):
        r"""


        get the entry name. for example, the structure name
        
        get_name(self, inode) -> bool
            @param inode (C++: inode_t)
            @return: false if the entry does not exist.
        """
        return _ida_dirtree.dirspec_t_get_name(self, *args)
    
    def get_inode(self, *args):
        r"""


        get the entry inode in the specified directory
        
        get_inode(self, diridx, name) -> inode_t
            @param diridx (C++: diridx_t)
            @param name (C++: const char *)
            @return: the entry inode
        """
        return _ida_dirtree.dirspec_t_get_inode(self, *args)
    
    def get_attrs(self, *args):
        r"""


        get_attrs(self, inode) -> qstring
            @param inode (C++: inode_t)
        """
        return _ida_dirtree.dirspec_t_get_attrs(self, *args)
    
    def rename_inode(self, *args):
        r"""


        rename the entry
        
        rename_inode(self, inode, newname) -> bool
            @param inode (C++: inode_t)
            @param newname (C++: const char *)
            @return: success
        """
        return _ida_dirtree.dirspec_t_rename_inode(self, *args)
    
    def unlink_inode(self, *args):
        r"""


        event: unlinked an inode
        
        unlink_inode(self, inode)
            @param inode (C++: inode_t)
        """
        return _ida_dirtree.dirspec_t_unlink_inode(self, *args)
    
    def __disown__(self):
        self.this.disown()
        _ida_dirtree.disown_dirspec_t(self)
        return weakref.proxy(self)

# Register dirspec_t in _ida_dirtree:
_ida_dirtree.dirspec_t_swigregister(dirspec_t)

class dirtree_cursor_t(object):
    r"""
    Proxy of C++ dirtree_cursor_t class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    parent = property(_ida_dirtree.dirtree_cursor_t_parent_get, _ida_dirtree.dirtree_cursor_t_parent_set)
    rank = property(_ida_dirtree.dirtree_cursor_t_rank_get, _ida_dirtree.dirtree_cursor_t_rank_set)
    
    def __init__(self, *args):
        r"""


        __init__(self, _parent=BADIDX, _rank=size_t(-1)) -> dirtree_cursor_t
            _parent: diridx_t
            _rank: size_t
        """
        _ida_dirtree.dirtree_cursor_t_swiginit(self, _ida_dirtree.new_dirtree_cursor_t(*args))
    
    def valid(self, *args):
        r"""
        valid(self) -> bool
        """
        return _ida_dirtree.dirtree_cursor_t_valid(self, *args)
    
    def is_root_cursor(self, *args):
        r"""
        is_root_cursor(self) -> bool
        """
        return _ida_dirtree.dirtree_cursor_t_is_root_cursor(self, *args)
    
    def set_root_cursor(self, *args):
        r"""
        set_root_cursor(self)
        """
        return _ida_dirtree.dirtree_cursor_t_set_root_cursor(self, *args)
    
    @staticmethod
    def root_cursor(*args):
        r"""
        root_cursor() -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_t_root_cursor(*args)
    
    def __eq__(self, *args):
        r"""


        __eq__(self, r) -> bool
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___eq__(self, *args)
    
    def __ne__(self, *args):
        r"""


        __ne__(self, r) -> bool
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___ne__(self, *args)
    
    def __lt__(self, *args):
        r"""


        __lt__(self, r) -> bool
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___lt__(self, *args)
    
    def __gt__(self, *args):
        r"""


        __gt__(self, r) -> bool
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___gt__(self, *args)
    
    def __le__(self, *args):
        r"""


        __le__(self, r) -> bool
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___le__(self, *args)
    
    def __ge__(self, *args):
        r"""


        __ge__(self, r) -> bool
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___ge__(self, *args)
    
    def compare(self, *args):
        r"""


        compare(self, r) -> int
            r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t_compare(self, *args)
    
    __swig_destroy__ = _ida_dirtree.delete_dirtree_cursor_t

# Register dirtree_cursor_t in _ida_dirtree:
_ida_dirtree.dirtree_cursor_t_swigregister(dirtree_cursor_t)

def dirtree_cursor_t_root_cursor(*args):
    r"""
    dirtree_cursor_t_root_cursor() -> dirtree_cursor_t
    """
    return _ida_dirtree.dirtree_cursor_t_root_cursor(*args)

class dirtree_selection_t(dirtree_cursor_vec_t):
    r"""
    Proxy of C++ dirtree_selection_t class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    
    def __init__(self, *args):
        r"""
        __init__(self) -> dirtree_selection_t
        """
        _ida_dirtree.dirtree_selection_t_swiginit(self, _ida_dirtree.new_dirtree_selection_t(*args))
    
    __swig_destroy__ = _ida_dirtree.delete_dirtree_selection_t

# Register dirtree_selection_t in _ida_dirtree:
_ida_dirtree.dirtree_selection_t_swigregister(dirtree_selection_t)

class dirtree_iterator_t(object):
    r"""
    Proxy of C++ dirtree_iterator_t class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    pattern = property(_ida_dirtree.dirtree_iterator_t_pattern_get, _ida_dirtree.dirtree_iterator_t_pattern_set)
    cursor = property(_ida_dirtree.dirtree_iterator_t_cursor_get, _ida_dirtree.dirtree_iterator_t_cursor_set)
    
    def __init__(self, *args):
        r"""
        __init__(self) -> dirtree_iterator_t
        """
        _ida_dirtree.dirtree_iterator_t_swiginit(self, _ida_dirtree.new_dirtree_iterator_t(*args))
    
    __swig_destroy__ = _ida_dirtree.delete_dirtree_iterator_t

# Register dirtree_iterator_t in _ida_dirtree:
_ida_dirtree.dirtree_iterator_t_swigregister(dirtree_iterator_t)

DTE_OK = _ida_dirtree.DTE_OK

DTE_ALREADY_EXISTS = _ida_dirtree.DTE_ALREADY_EXISTS

DTE_NOT_FOUND = _ida_dirtree.DTE_NOT_FOUND

DTE_NOT_DIRECTORY = _ida_dirtree.DTE_NOT_DIRECTORY

DTE_NOT_EMPTY = _ida_dirtree.DTE_NOT_EMPTY

DTE_BAD_PATH = _ida_dirtree.DTE_BAD_PATH

DTE_CANT_RENAME = _ida_dirtree.DTE_CANT_RENAME

DTE_OWN_CHILD = _ida_dirtree.DTE_OWN_CHILD

DTE_MAX_DIR = _ida_dirtree.DTE_MAX_DIR

DTE_LAST = _ida_dirtree.DTE_LAST

class dirtree_t(object):
    r"""
    Proxy of C++ dirtree_t class.
    """
    
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    
    def __init__(self, *args):
        r"""


        __init__(self, ds) -> dirtree_t
            ds: dirspec_t *
        """
        _ida_dirtree.dirtree_t_swiginit(self, _ida_dirtree.new_dirtree_t(*args))
    
    __swig_destroy__ = _ida_dirtree.delete_dirtree_t
    
    @staticmethod
    def errstr(*args):
        r"""


        errstr(err) -> char const *
            err: enum dterr_t
        """
        return _ida_dirtree.dirtree_t_errstr(*args)
    
    def chdir(self, *args):
        r"""


        Change current directory
        
        chdir(self, path) -> dterr_t
            @param path: new current directory (C++: const char *)
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_chdir(self, *args)
    
    def getcwd(self, *args):
        r"""


        Get current directory
        """
        return _ida_dirtree.dirtree_t_getcwd(self, *args)
    
    def get_abspath(self, *args):
        r"""


        Get absolute path pointed by the cursorsee also 'resolve_cursor()'
        
        get_abspath(self, cursor) -> qstring
            @param cursor (C++: const  dirtree_cursor_t  &)
            @return: path. empty path means wrong directory part of RELPATH
        

        get_abspath(self, relpath) -> qstring
            relpath: char const *
            @return: path. empty path means wrong directory part of RELPATH
        """
        return _ida_dirtree.dirtree_t_get_abspath(self, *args)
    
    def resolve_cursor(self, *args):
        r"""


        Resolve cursorsee also 'get_abspath()'
        
        resolve_cursor(self, cursor) -> direntry_t
            @param cursor: to analyze (C++: const  dirtree_cursor_t  &)
            @return: directory entry; if the cursor is bad, the resolved entry
                     will be invalid.
        """
        return _ida_dirtree.dirtree_t_resolve_cursor(self, *args)
    
    def resolve_path(self, *args):
        r"""


        Resolve path
        
        resolve_path(self, path) -> direntry_t
            @param path: to analyze (C++: const char *)
            @return: directory entry
        """
        return _ida_dirtree.dirtree_t_resolve_path(self, *args)
    
    def isdir(self, *args):
        r"""


        Is a directory?
        
        isdir(self, de) -> bool
            de: direntry_t const &
            @return: true if the specified path is a directory
        

        isdir(self, path) -> bool
            path: char const *
            @return: true if the specified path is a directory
        """
        return _ida_dirtree.dirtree_t_isdir(self, *args)
    
    def isfile(self, *args):
        r"""


        Is a file?
        
        isfile(self, de) -> bool
            de: direntry_t const &
            @return: true if the specified path is a file
        

        isfile(self, path) -> bool
            path: char const *
            @return: true if the specified path is a file
        """
        return _ida_dirtree.dirtree_t_isfile(self, *args)
    
    def get_entry_name(self, *args):
        r"""


        Get entry name
        
        get_entry_name(self, de) -> qstring
            @param de: directory entry (C++: const  direntry_t  &)
            @return: name
        """
        return _ida_dirtree.dirtree_t_get_entry_name(self, *args)
    
    def get_dir_size(self, *args):
        r"""


        Get dir size
        
        get_dir_size(self, diridx) -> ssize_t
            @param diridx: directory index (C++: diridx_t)
            @return: number of entries under this directory; if error, return -1
        """
        return _ida_dirtree.dirtree_t_get_dir_size(self, *args)
    
    def get_entry_attrs(self, *args):
        r"""


        Get entry attributes
        
        get_entry_attrs(self, de) -> qstring
            @param de: directory entry (C++: const  direntry_t  &)
            @return: name
        """
        return _ida_dirtree.dirtree_t_get_entry_attrs(self, *args)
    
    def findfirst(self, *args):
        r"""


        Start iterating over files in a directory
        
        findfirst(self, ff, pattern) -> bool
            @param ff: directory iterator. it will be initialized by the function
                       (C++: dirtree_iterator_t  *)
            @param pattern: pattern to search for (C++: const char *)
            @return: success
        """
        return _ida_dirtree.dirtree_t_findfirst(self, *args)
    
    def findnext(self, *args):
        r"""


        Continue iterating over files in a directory
        
        findnext(self, ff) -> bool
            @param ff: directory iterator (C++: dirtree_iterator_t  *)
            @return: success
        """
        return _ida_dirtree.dirtree_t_findnext(self, *args)
    
    def mkdir(self, *args):
        r"""


        Create a directory.
        
        mkdir(self, path) -> dterr_t
            @param path: directory to create (C++: const char *)
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_mkdir(self, *args)
    
    def rmdir(self, *args):
        r"""


        Remove a directory.
        
        rmdir(self, path) -> dterr_t
            @param path: directory to delete (C++: const char *)
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_rmdir(self, *args)
    
    def link(self, *args):
        r"""


        Add a file item into a directory.
        
        link(self, path) -> dterr_t
            @param path: path to item to add to a directory (C++: const char *)
            @return: dterr_t  error code
        

        link(self, inode) -> dterr_t
            inode: inode_t
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_link(self, *args)
    
    def unlink(self, *args):
        r"""


        Remove a file item from a directory.
        
        unlink(self, path) -> dterr_t
            @param path: path to item remove from a directory (C++: const char *)
            @return: dterr_t  error code
        

        unlink(self, inode) -> dterr_t
            inode: inode_t
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_unlink(self, *args)
    
    def rename(self, *args):
        r"""


        Rename a directory entry.This function can also rename the item
        
        rename(self, _from, to) -> dterr_t
            @param _from: source path (C++: const char *)
            @param to: destination path (C++: const char *)
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_rename(self, *args)
    
    def get_rank(self, *args):
        r"""


        Get ordering rank of an item.
        
        get_rank(self, diridx, de) -> ssize_t
            @param diridx: index of the parent directory (C++: diridx_t)
            @param de: directory entry (C++: const  direntry_t  &)
            @return: number in a range of [0..n) where n is the number of entries
                     in the parent directory. -1 if error
        """
        return _ida_dirtree.dirtree_t_get_rank(self, *args)
    
    def change_rank(self, *args):
        r"""


        Change ordering rank of an item.All subdirectories go before all file
        entries.
        
        change_rank(self, path, rank_delta) -> dterr_t
            @param path: path to the item (C++: const char *)
            @param rank_delta (C++: ssize_t)
            @return: dterr_t  error code
        """
        return _ida_dirtree.dirtree_t_change_rank(self, *args)
    
    def get_parent_cursor(self, *args):
        r"""


        Get parent cursor.
        
        get_parent_cursor(self, cursor) -> dirtree_cursor_t
            @param cursor: a valid ditree cursor (C++: const  dirtree_cursor_t  &)
            @return: cursor's parent
        """
        return _ida_dirtree.dirtree_t_get_parent_cursor(self, *args)
    
    def load(self, *args):
        r"""


        Load the tree structure from the netnode. If dirspec_t::nodename is
        empty, the operation will be considered a success. In addition,
        calling 'load()' more than once will not do anything, and will be
        considered a success.dirspec_t::nodename.
        """
        return _ida_dirtree.dirtree_t_load(self, *args)
    
    def save(self, *args):
        r"""


        Save the tree structure to the netnode.dirspec_t::nodename.
        """
        return _ida_dirtree.dirtree_t_save(self, *args)
    
    def get_nodename(self, *args):
        r"""


        netnode name
        """
        return _ida_dirtree.dirtree_t_get_nodename(self, *args)
    
    def set_nodename(self, *args):
        r"""


        set_nodename(self, nm)
            @param nm (C++: const char *)
        """
        return _ida_dirtree.dirtree_t_set_nodename(self, *args)
    
    def notify_dirtree(self, *args):
        r"""


        Notify dirtree about a change of an inode.
        
        notify_dirtree(self, added, inode)
            @param added (C++: bool)
            @param inode: inode in question (C++: inode_t)
        """
        return _ida_dirtree.dirtree_t_notify_dirtree(self, *args)

# Register dirtree_t in _ida_dirtree:
_ida_dirtree.dirtree_t_swigregister(dirtree_t)

def dirtree_t_errstr(*args):
    r"""


    dirtree_t_errstr(err) -> char const *
        err: enum dterr_t
    """
    return _ida_dirtree.dirtree_t_errstr(*args)

DIRTREE_LOCAL_TYPES = _ida_dirtree.DIRTREE_LOCAL_TYPES

DIRTREE_STRUCTS = _ida_dirtree.DIRTREE_STRUCTS

DIRTREE_ENUMS = _ida_dirtree.DIRTREE_ENUMS

DIRTREE_FUNCS = _ida_dirtree.DIRTREE_FUNCS

DIRTREE_NAMES = _ida_dirtree.DIRTREE_NAMES

DIRTREE_IMPORTS = _ida_dirtree.DIRTREE_IMPORTS

DIRTREE_IDAPLACE_BOOKMARKS = _ida_dirtree.DIRTREE_IDAPLACE_BOOKMARKS

DIRTREE_STRUCTS_BOOKMARKS = _ida_dirtree.DIRTREE_STRUCTS_BOOKMARKS

DIRTREE_ENUMS_BOOKMARKS = _ida_dirtree.DIRTREE_ENUMS_BOOKMARKS

DIRTREE_END = _ida_dirtree.DIRTREE_END

def get_std_dirtree(*args):
    r"""


    get_std_dirtree(id) -> dirtree_t
        @param id (C++: dirtree_id_t)
    """
    return _ida_dirtree.get_std_dirtree(*args)
