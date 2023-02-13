#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: struct
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_struct
else:
    import _ida_struct

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

SWIG_PYTHON_LEGACY_BOOL = _ida_struct.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class dyn_member_ref_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< member_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data = property(_ida_struct.dyn_member_ref_array_data_get)
    count = property(_ida_struct.dyn_member_ref_array_count_get)

    def __init__(self, *args):
        r"""


        __init__(self, _data, _count) -> dyn_member_ref_array
            _data: member_t *
            _count: size_t
        """
        _ida_struct.dyn_member_ref_array_swiginit(self, _ida_struct.new_dyn_member_ref_array(*args))

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_struct.dyn_member_ref_array___len__(self, *args)

    def __getitem__(self, *args) -> "member_t const &":
        r"""


        __getitem__(self, i) -> member_t
            i: size_t
        """
        return _ida_struct.dyn_member_ref_array___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: member_t const &
        """
        return _ida_struct.dyn_member_ref_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_struct.delete_dyn_member_ref_array

# Register dyn_member_ref_array in _ida_struct:
_ida_struct.dyn_member_ref_array_swigregister(dyn_member_ref_array)

STRUC_SEPARATOR = _ida_struct.STRUC_SEPARATOR
"""
structname.fieldname
"""

class member_t(object):
    r"""
    Proxy of C++ member_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    id = property(_ida_struct.member_t_id_get, _ida_struct.member_t_id_set)
    soff = property(_ida_struct.member_t_soff_get, _ida_struct.member_t_soff_set)
    eoff = property(_ida_struct.member_t_eoff_get, _ida_struct.member_t_eoff_set)
    flag = property(_ida_struct.member_t_flag_get, _ida_struct.member_t_flag_set)
    props = property(_ida_struct.member_t_props_get, _ida_struct.member_t_props_set)

    def unimem(self, *args) -> "bool":
        r"""


        Is a member of a union?
        """
        return _ida_struct.member_t_unimem(self, *args)

    def has_union(self, *args) -> "bool":
        r"""


        Has members of type "union"?
        """
        return _ida_struct.member_t_has_union(self, *args)

    def by_til(self, *args) -> "bool":
        r"""


        Was the member created due to the type system?
        """
        return _ida_struct.member_t_by_til(self, *args)

    def has_ti(self, *args) -> "bool":
        r"""


        Has type information?
        """
        return _ida_struct.member_t_has_ti(self, *args)

    def is_baseclass(self, *args) -> "bool":
        r"""


        Is a base class member?
        """
        return _ida_struct.member_t_is_baseclass(self, *args)

    def is_dupname(self, *args) -> "bool":
        r"""


        Duplicate name was resolved during import?
        """
        return _ida_struct.member_t_is_dupname(self, *args)

    def is_destructor(self, *args) -> "bool":
        r"""


        Is a virtual destructor?
        """
        return _ida_struct.member_t_is_destructor(self, *args)

    def get_soff(self, *args) -> "ea_t":
        r"""


        Get start offset (for unions - returns 0)
        """
        return _ida_struct.member_t_get_soff(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> member_t
        """
        _ida_struct.member_t_swiginit(self, _ida_struct.new_member_t(*args))
    __swig_destroy__ = _ida_struct.delete_member_t

# Register member_t in _ida_struct:
_ida_struct.member_t_swigregister(member_t)
MF_OK = _ida_struct.MF_OK
"""
is the member ok? (always yes)
"""

MF_UNIMEM = _ida_struct.MF_UNIMEM
"""
is a member of a union?
"""

MF_HASUNI = _ida_struct.MF_HASUNI
"""
has members of type "union"?
"""

MF_BYTIL = _ida_struct.MF_BYTIL
"""
the member was created due to the type system
"""

MF_HASTI = _ida_struct.MF_HASTI
"""
has type information?
"""

MF_BASECLASS = _ida_struct.MF_BASECLASS
"""
a special member representing base class
"""

MF_DTOR = _ida_struct.MF_DTOR
"""
a special member representing destructor
"""

MF_DUPNAME = _ida_struct.MF_DUPNAME
"""
duplicate name resolved with _N suffix (N==soff)
"""


class struc_t(object):
    r"""
    Proxy of C++ struc_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    id = property(_ida_struct.struc_t_id_get, _ida_struct.struc_t_id_set)
    memqty = property(_ida_struct.struc_t_memqty_get, _ida_struct.struc_t_memqty_set)
    members = property(_ida_struct.struc_t_members_get, _ida_struct.struc_t_members_set)
    age = property(_ida_struct.struc_t_age_get, _ida_struct.struc_t_age_set)
    props = property(_ida_struct.struc_t_props_get, _ida_struct.struc_t_props_set)

    def is_varstr(self, *args) -> "bool":
        r"""


        Is variable size structure?
        """
        return _ida_struct.struc_t_is_varstr(self, *args)

    def is_union(self, *args) -> "bool":
        r"""


        Is a union?
        """
        return _ida_struct.struc_t_is_union(self, *args)

    def has_union(self, *args) -> "bool":
        r"""


        Has members of type "union"?
        """
        return _ida_struct.struc_t_has_union(self, *args)

    def is_choosable(self, *args) -> "bool":
        r"""


        Is included in chooser list? Use 'set_struc_listed' to change the
        listed status
        """
        return _ida_struct.struc_t_is_choosable(self, *args)

    def from_til(self, *args) -> "bool":
        r"""


        Does structure come from a type library?
        """
        return _ida_struct.struc_t_from_til(self, *args)

    def is_hidden(self, *args) -> "bool":
        r"""


        Is the structure collapsed? Use 'set_struc_hidden' to change the
        hidden status
        """
        return _ida_struct.struc_t_is_hidden(self, *args)

    def is_frame(self, *args) -> "bool":
        r"""


        Is this structure a function frame?
        """
        return _ida_struct.struc_t_is_frame(self, *args)

    def get_alignment(self, *args) -> "int":
        r"""


        See 'SF_ALIGN' .
        """
        return _ida_struct.struc_t_get_alignment(self, *args)

    def is_ghost(self, *args) -> "bool":
        r"""


        Is a ghost copy of a local type?
        """
        return _ida_struct.struc_t_is_ghost(self, *args)

    def set_alignment(self, *args) -> "void":
        r"""


        Do not use; use 'set_struc_align()'
        
        set_alignment(self, shift)
            @param shift (C++: int)
        """
        return _ida_struct.struc_t_set_alignment(self, *args)

    def set_ghost(self, *args) -> "void":
        r"""


        set_ghost(self, _is_ghost)
            @param _is_ghost (C++: bool)
        """
        return _ida_struct.struc_t_set_ghost(self, *args)
    ordinal = property(_ida_struct.struc_t_ordinal_get, _ida_struct.struc_t_ordinal_set)

    def __get_members__(self, *args) -> "dynamic_wrapped_array_t< member_t >":
        r"""
        __get_members__(self) -> dyn_member_ref_array
        """
        return _ida_struct.struc_t___get_members__(self, *args)

    members = property(__get_members__)
    def get_member(self, index):
        return self.members[index]

    __swig_destroy__ = _ida_struct.delete_struc_t

# Register struc_t in _ida_struct:
_ida_struct.struc_t_swigregister(struc_t)
SF_VAR = _ida_struct.SF_VAR
"""
is variable size structure (varstruct)? a variable size structure is
one with the zero size last member. if the last member is a varstruct,
then the current structure is a varstruct too.
"""

SF_UNION = _ida_struct.SF_UNION
"""
varunions are prohibited!

is a union?
"""

SF_HASUNI = _ida_struct.SF_HASUNI
"""
has members of type "union"?
"""

SF_NOLIST = _ida_struct.SF_NOLIST
"""
don't include in the chooser list
"""

SF_TYPLIB = _ida_struct.SF_TYPLIB
"""
the structure comes from type library
"""

SF_HIDDEN = _ida_struct.SF_HIDDEN
"""
the structure is collapsed
"""

SF_FRAME = _ida_struct.SF_FRAME
"""
the structure is a function frame
"""

SF_ALIGN = _ida_struct.SF_ALIGN
"""
alignment (shift amount: 0..31)
"""

SF_GHOST = _ida_struct.SF_GHOST
"""
ghost copy of a local type
"""



def get_struc_qty(*args) -> "size_t":
    r"""


    Get number of known structures.
    """
    return _ida_struct.get_struc_qty(*args)

def get_first_struc_idx(*args) -> "uval_t":
    r"""


    Get index of first structure.
    """
    return _ida_struct.get_first_struc_idx(*args)

def get_last_struc_idx(*args) -> "uval_t":
    r"""


    Get index of last structure.
    """
    return _ida_struct.get_last_struc_idx(*args)

def get_prev_struc_idx(*args) -> "uval_t":
    r"""


    Get previous struct index.
    
    get_prev_struc_idx(idx) -> uval_t
        @param idx (C++: uval_t)
        @return: BADADDR  if resulting index is negative, otherwise idx - 1
    """
    return _ida_struct.get_prev_struc_idx(*args)

def get_next_struc_idx(*args) -> "uval_t":
    r"""


    Get next struct index.
    
    get_next_struc_idx(idx) -> uval_t
        @param idx (C++: uval_t)
        @return: BADADDR  if resulting index is out of bounds, otherwise idx++
    """
    return _ida_struct.get_next_struc_idx(*args)

def get_struc_idx(*args) -> "uval_t":
    r"""


    Get internal number of the structure.
    
    get_struc_idx(id) -> uval_t
        @param id (C++: tid_t)
    """
    return _ida_struct.get_struc_idx(*args)

def get_struc_by_idx(*args) -> "tid_t":
    r"""


    Get struct id by struct number.
    
    get_struc_by_idx(idx) -> tid_t
        @param idx (C++: uval_t)
    """
    return _ida_struct.get_struc_by_idx(*args)

def get_struc(*args) -> "struc_t *":
    r"""


    Get pointer to struct type info.
    
    get_struc(id) -> struc_t
        @param id (C++: tid_t)
    """
    return _ida_struct.get_struc(*args)

def get_struc_id(*args) -> "tid_t":
    r"""


    Get struct id by name.
    
    get_struc_id(name) -> tid_t
        @param name (C++: const char *)
    """
    return _ida_struct.get_struc_id(*args)

def get_struc_name(*args) -> "qstring *":
    r"""


    Get struct name by id
    
    get_struc_name(id, flags=0) -> str
        @param id: struct id (C++: tid_t)
        @param flags: Struct name flags (C++: int)
    """
    return _ida_struct.get_struc_name(*args)
STRNFL_REGEX = _ida_struct.STRNFL_REGEX
"""
apply regular expressions to beautify the name
"""


def get_struc_cmt(*args) -> "qstring *":
    r"""


    Get struct comment.
    
    get_struc_cmt(id, repeatable) -> str
        @param id (C++: tid_t)
        @param repeatable (C++: bool)
    """
    return _ida_struct.get_struc_cmt(*args)

def get_struc_size(*args) -> "asize_t":
    r"""


    Get struct size (also see 'get_struc_size(tid_t)' )
    
    get_struc_size(sptr) -> asize_t
        @param sptr (C++: const  struc_t  *)
    

    get_struc_size(id) -> asize_t
        id: tid_t
    """
    return _ida_struct.get_struc_size(*args)

def get_struc_prev_offset(*args) -> "ea_t":
    r"""


    Get offset of member with largest offset less than 'offset'.
    
    get_struc_prev_offset(sptr, offset) -> ea_t
        @param sptr (C++: const  struc_t  *)
        @param offset (C++: ea_t)
        @return: BADADDR  if no prev offset
    """
    return _ida_struct.get_struc_prev_offset(*args)

def get_struc_next_offset(*args) -> "ea_t":
    r"""


    Get offset of member with smallest offset larger than 'offset'.
    
    get_struc_next_offset(sptr, offset) -> ea_t
        @param sptr (C++: const  struc_t  *)
        @param offset (C++: ea_t)
        @return: BADADDR  if no next offset
    """
    return _ida_struct.get_struc_next_offset(*args)

def get_struc_last_offset(*args) -> "ea_t":
    r"""


    Get offset of last member.
    
    get_struc_last_offset(sptr) -> ea_t
        @param sptr (C++: const  struc_t  *)
        @return: BADADDR  if memqty == 0
    """
    return _ida_struct.get_struc_last_offset(*args)

def get_struc_first_offset(*args) -> "ea_t":
    r"""


    Get offset of first member.
    
    get_struc_first_offset(sptr) -> ea_t
        @param sptr (C++: const  struc_t  *)
        @return: BADADDR  if memqty == 0
    """
    return _ida_struct.get_struc_first_offset(*args)

def get_max_offset(*args) -> "ea_t":
    r"""


    For unions: returns number of members, for structs: returns size of
    structure.
    
    get_max_offset(sptr) -> ea_t
        @param sptr (C++: struc_t  *)
    """
    return _ida_struct.get_max_offset(*args)

def is_varstr(*args) -> "bool":
    r"""


    Is variable size structure?
    
    is_varstr(id) -> bool
        @param id (C++: tid_t)
    """
    return _ida_struct.is_varstr(*args)

def is_union(*args) -> "bool":
    r"""


    Is a union?
    
    is_union(id) -> bool
        @param id (C++: tid_t)
    """
    return _ida_struct.is_union(*args)

def get_member_struc(*args) -> "struc_t *":
    r"""


    Get containing structure of member by its full name "struct.field".
    
    get_member_struc(fullname) -> struc_t
        @param fullname (C++: const char *)
    """
    return _ida_struct.get_member_struc(*args)

def get_sptr(*args) -> "struc_t *":
    r"""


    Get child struct if member is a struct.
    
    get_sptr(mptr) -> struc_t
        @param mptr (C++: const  member_t  *)
    """
    return _ida_struct.get_sptr(*args)

def get_member(*args) -> "member_t *":
    r"""


    Get member at given offset.
    
    get_member(sptr, offset) -> member_t
        @param sptr (C++: const  struc_t  *)
        @param offset (C++: asize_t)
    """
    return _ida_struct.get_member(*args)

def get_member_id(*args) -> "tid_t":
    r"""


    Get member id at given offset.
    
    get_member_id(sptr, offset) -> tid_t
        @param sptr (C++: const  struc_t  *)
        @param offset (C++: asize_t)
    """
    return _ida_struct.get_member_id(*args)

def get_member_by_name(*args) -> "member_t *":
    r"""


    Get a member by its name, like "field44".
    
    get_member_by_name(sptr, membername) -> member_t
        @param sptr (C++: const  struc_t  *)
        @param membername (C++: const char *)
    """
    return _ida_struct.get_member_by_name(*args)

def get_member_by_fullname(*args) -> "struc_t **":
    r"""


    Get a member by its fully qualified name, "struct.field".
    
    get_member_by_fullname(fullname) -> member_t
        @param fullname (C++: const char *)
    """
    return _ida_struct.get_member_by_fullname(*args)

def get_member_fullname(*args) -> "qstring *":
    r"""


    Get a member's fully qualified name, "struct.field".
    
    get_member_fullname(mid) -> str
        @param mid (C++: tid_t)
    """
    return _ida_struct.get_member_fullname(*args)

def get_member_name(*args) -> "qstring *":
    r"""


    Get name of structure member.
    
    get_member_name(mid) -> str
        @param mid (C++: tid_t)
    """
    return _ida_struct.get_member_name(*args)

def get_member_cmt(*args) -> "qstring *":
    r"""


    Get comment of structure member.
    
    get_member_cmt(mid, repeatable) -> str
        @param mid (C++: tid_t)
        @param repeatable (C++: bool)
    """
    return _ida_struct.get_member_cmt(*args)

def get_member_size(*args) -> "asize_t":
    r"""


    Get size of structure member. May return 0 for the last member of
    varstruct. For union members, returns 'member_t::eoff' .
    
    get_member_size(mptr) -> asize_t
        @param mptr (C++: const  member_t  *)
    """
    return _ida_struct.get_member_size(*args)

def is_varmember(*args) -> "bool":
    r"""


    Is variable size member?
    
    is_varmember(mptr) -> bool
        @param mptr (C++: const  member_t  *)
    """
    return _ida_struct.is_varmember(*args)

def get_best_fit_member(*args) -> "member_t *":
    r"""


    Get member that is most likely referenced by the specified offset.
    Useful for offsets > sizeof(struct).
    
    get_best_fit_member(sptr, offset) -> member_t
        @param sptr (C++: const  struc_t  *)
        @param offset (C++: asize_t)
    """
    return _ida_struct.get_best_fit_member(*args)

def get_next_member_idx(*args) -> "ssize_t":
    r"""


    Get the next member idx, if it does not exist, return -1.
    
    get_next_member_idx(sptr, off) -> ssize_t
        @param sptr (C++: const  struc_t  *)
        @param off (C++: asize_t)
    """
    return _ida_struct.get_next_member_idx(*args)

def get_prev_member_idx(*args) -> "ssize_t":
    r"""


    Get the prev member idx, if it does not exist, return -1.
    
    get_prev_member_idx(sptr, off) -> ssize_t
        @param sptr (C++: const  struc_t  *)
        @param off (C++: asize_t)
    """
    return _ida_struct.get_prev_member_idx(*args)

def add_struc(*args) -> "tid_t":
    r"""


    Create a structure type. if idx== 'BADADDR' then add as the last idx.
    if name==NULL then a name will be generated "struct_%d".
    
    add_struc(idx, name, is_union=False) -> tid_t
        @param idx (C++: uval_t)
        @param name (C++: const char *)
        @param is_union (C++: bool)
    """
    return _ida_struct.add_struc(*args)

def del_struc(*args) -> "bool":
    r"""


    Delete a structure type.
    
    del_struc(sptr) -> bool
        @param sptr (C++: struc_t  *)
    """
    return _ida_struct.del_struc(*args)

def set_struc_idx(*args) -> "bool":
    r"""


    Set internal number of struct. Also see 'get_struc_idx()' ,
    'get_struc_by_idx()' .
    
    set_struc_idx(sptr, idx) -> bool
        @param sptr (C++: const  struc_t  *)
        @param idx (C++: uval_t)
    """
    return _ida_struct.set_struc_idx(*args)

def set_struc_align(*args) -> "bool":
    r"""


    Set structure alignment ( 'SF_ALIGN' )
    
    set_struc_align(sptr, shift) -> bool
        @param sptr (C++: struc_t  *)
        @param shift (C++: int)
    """
    return _ida_struct.set_struc_align(*args)

def set_struc_name(*args) -> "bool":
    r"""


    Set structure name.
    
    set_struc_name(id, name) -> bool
        @param id (C++: tid_t)
        @param name (C++: const char *)
    """
    return _ida_struct.set_struc_name(*args)

def set_struc_cmt(*args) -> "bool":
    r"""


    Set structure comment.
    
    set_struc_cmt(id, cmt, repeatable) -> bool
        @param id (C++: tid_t)
        @param cmt (C++: const char *)
        @param repeatable (C++: bool)
    """
    return _ida_struct.set_struc_cmt(*args)
STRUC_ERROR_MEMBER_OK = _ida_struct.STRUC_ERROR_MEMBER_OK

STRUC_ERROR_MEMBER_NAME = _ida_struct.STRUC_ERROR_MEMBER_NAME

STRUC_ERROR_MEMBER_OFFSET = _ida_struct.STRUC_ERROR_MEMBER_OFFSET

STRUC_ERROR_MEMBER_SIZE = _ida_struct.STRUC_ERROR_MEMBER_SIZE

STRUC_ERROR_MEMBER_TINFO = _ida_struct.STRUC_ERROR_MEMBER_TINFO

STRUC_ERROR_MEMBER_STRUCT = _ida_struct.STRUC_ERROR_MEMBER_STRUCT

STRUC_ERROR_MEMBER_UNIVAR = _ida_struct.STRUC_ERROR_MEMBER_UNIVAR

STRUC_ERROR_MEMBER_VARLAST = _ida_struct.STRUC_ERROR_MEMBER_VARLAST

STRUC_ERROR_MEMBER_NESTED = _ida_struct.STRUC_ERROR_MEMBER_NESTED


def add_struc_member(*args) -> "struc_error_t":
    r"""


    Add member to existing structure.
    
    add_struc_member(sptr, fieldname, offset, flag, mt, nbytes) -> struc_error_t
        @param sptr: structure to modify (C++: struc_t  *)
        @param fieldname: if NULL, then "anonymous_#" name will be generated
                          (C++: const char *)
        @param offset: BADADDR  means add to the end of structure (C++: ea_t)
        @param flag: type + representation bits (C++: flags_t)
        @param mt: additional info about member type. must be present for
                   structs, offsets, enums, strings, struct offsets. (C++:
                   const  opinfo_t  *)
        @param nbytes: if == 0 then the structure will be a varstruct. in this
                       case the member should be the last member in the
                       structure (C++: asize_t)
    """
    return _ida_struct.add_struc_member(*args)

def del_struc_member(*args) -> "bool":
    r"""


    Delete member at given offset.
    
    del_struc_member(sptr, offset) -> bool
        @param sptr (C++: struc_t  *)
        @param offset (C++: ea_t)
    """
    return _ida_struct.del_struc_member(*args)

def del_struc_members(*args) -> "int":
    r"""


    Delete members which occupy range of offsets (off1..off2).
    
    del_struc_members(sptr, off1, off2) -> int
        @param sptr (C++: struc_t  *)
        @param off1 (C++: ea_t)
        @param off2 (C++: ea_t)
        @return: number of deleted members or -1 on error
    """
    return _ida_struct.del_struc_members(*args)

def set_member_name(*args) -> "bool":
    r"""


    Set name of member at given offset.
    
    set_member_name(sptr, offset, name) -> bool
        @param sptr (C++: struc_t  *)
        @param offset (C++: ea_t)
        @param name (C++: const char *)
    """
    return _ida_struct.set_member_name(*args)

def set_member_type(*args) -> "bool":
    r"""


    Set type of member at given offset (also see 'add_struc_member()' )
    
    set_member_type(sptr, offset, flag, mt, nbytes) -> bool
        @param sptr (C++: struc_t  *)
        @param offset (C++: ea_t)
        @param flag (C++: flags_t)
        @param mt (C++: const  opinfo_t  *)
        @param nbytes (C++: asize_t)
    """
    return _ida_struct.set_member_type(*args)

def set_member_cmt(*args) -> "bool":
    r"""


    Set member comment.
    
    set_member_cmt(mptr, cmt, repeatable) -> bool
        @param mptr (C++: member_t  *)
        @param cmt (C++: const char *)
        @param repeatable (C++: bool)
    """
    return _ida_struct.set_member_cmt(*args)

def expand_struc(*args) -> "bool":
    r"""


    Expand/Shrink structure type.
    
    expand_struc(sptr, offset, delta, recalc=True) -> bool
        @param sptr (C++: struc_t  *)
        @param offset (C++: ea_t)
        @param delta (C++: adiff_t)
        @param recalc (C++: bool)
    """
    return _ida_struct.expand_struc(*args)

def save_struc(*args) -> "void":
    r"""


    Update struct information in the database (internal function)
    
    save_struc(sptr, may_update_ltypes=True)
        @param sptr (C++: struc_t  *)
        @param may_update_ltypes (C++: bool)
    """
    return _ida_struct.save_struc(*args)

def set_struc_hidden(*args) -> "void":
    r"""


    Hide/unhide a struct type.
    
    set_struc_hidden(sptr, is_hidden)
        @param sptr (C++: struc_t  *)
        @param is_hidden (C++: bool)
    """
    return _ida_struct.set_struc_hidden(*args)

def set_struc_listed(*args) -> "void":
    r"""


    Add/remove a struct type from the struct list.
    
    set_struc_listed(sptr, is_listed)
        @param sptr (C++: struc_t  *)
        @param is_listed (C++: bool)
    """
    return _ida_struct.set_struc_listed(*args)
SMT_BADARG = _ida_struct.SMT_BADARG

SMT_NOCOMPAT = _ida_struct.SMT_NOCOMPAT

SMT_WORSE = _ida_struct.SMT_WORSE

SMT_SIZE = _ida_struct.SMT_SIZE

SMT_ARRAY = _ida_struct.SMT_ARRAY

SMT_OVERLAP = _ida_struct.SMT_OVERLAP

SMT_FAILED = _ida_struct.SMT_FAILED

SMT_OK = _ida_struct.SMT_OK

SMT_KEEP = _ida_struct.SMT_KEEP


def get_member_tinfo(*args) -> "bool":
    r"""


    Get tinfo for given member.
    
    get_member_tinfo(tif, mptr) -> bool
        @param tif (C++: tinfo_t  *)
        @param mptr (C++: const  member_t  *)
    """
    return _ida_struct.get_member_tinfo(*args)

def del_member_tinfo(*args) -> "bool":
    r"""


    Delete tinfo for given member.
    
    del_member_tinfo(sptr, mptr) -> bool
        @param sptr (C++: struc_t  *)
        @param mptr (C++: member_t  *)
    """
    return _ida_struct.del_member_tinfo(*args)

def set_member_tinfo(*args) -> "smt_code_t":
    r"""


    Set tinfo for given member.
    
    set_member_tinfo(sptr, mptr, memoff, tif, flags) -> smt_code_t
        @param sptr: containing struct (C++: struc_t  *)
        @param mptr: target member (C++: member_t  *)
        @param memoff: offset within member (C++: uval_t)
        @param tif: type info (C++: const  tinfo_t  &)
        @param flags: Set member tinfo flags (C++: int)
    """
    return _ida_struct.set_member_tinfo(*args)
SET_MEMTI_MAY_DESTROY = _ida_struct.SET_MEMTI_MAY_DESTROY
"""
may destroy other members
"""

SET_MEMTI_COMPATIBLE = _ida_struct.SET_MEMTI_COMPATIBLE
"""
new type must be compatible with the old
"""

SET_MEMTI_FUNCARG = _ida_struct.SET_MEMTI_FUNCARG
"""
mptr is function argument (cannot create arrays)
"""

SET_MEMTI_BYTIL = _ida_struct.SET_MEMTI_BYTIL
"""
new type was created by the type subsystem
"""

SET_MEMTI_USERTI = _ida_struct.SET_MEMTI_USERTI
"""
user-specified type
"""


def get_or_guess_member_tinfo(*args) -> "bool":
    r"""


    Try to get tinfo for given member - if failed, generate a tinfo using
    information about the member id from the disassembly
    
    get_or_guess_member_tinfo(tif, mptr) -> bool
        @param tif (C++: tinfo_t  *)
        @param mptr (C++: const  member_t  *)
    """
    return _ida_struct.get_or_guess_member_tinfo(*args)

def retrieve_member_info(*args) -> "opinfo_t *":
    r"""


    Get operand type info for member.
    
    retrieve_member_info(buf, mptr) -> opinfo_t
        @param buf (C++: opinfo_t  *)
        @param mptr (C++: const  member_t  *)
    """
    return _ida_struct.retrieve_member_info(*args)

def is_anonymous_member_name(*args) -> "bool":
    r"""


    Is member name prefixed with "anonymous"?
    
    is_anonymous_member_name(name) -> bool
        @param name (C++: const char *)
    """
    return _ida_struct.is_anonymous_member_name(*args)

def is_dummy_member_name(*args) -> "bool":
    r"""


    Is member name an auto-generated name?
    
    is_dummy_member_name(name) -> bool
        @param name (C++: const char *)
    """
    return _ida_struct.is_dummy_member_name(*args)

def get_member_by_id(*args) -> "qstring *, struc_t **":
    r"""


    Check if the specified member id points to a struct member.
    
    get_member_by_id(mid) -> member_t
        @param mid (C++: tid_t)
    """
    return _ida_struct.get_member_by_id(*args)

def is_member_id(*args) -> "bool":
    r"""


    Is a member id?
    
    is_member_id(mid) -> bool
        @param mid (C++: tid_t)
    """
    return _ida_struct.is_member_id(*args)

def is_special_member(*args) -> "bool":
    r"""


    Is a special member with the name beginning with ' '?
    
    is_special_member(id) -> bool
        @param id (C++: tid_t)
    """
    return _ida_struct.is_special_member(*args)
class struct_field_visitor_t(object):
    r"""
    Proxy of C++ struct_field_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def visit_field(self, *args) -> "int":
        r"""


        visit_field(self, sptr, mptr) -> int
            @param sptr (C++: struc_t  *)
            @param mptr (C++: member_t  *)
        """
        return _ida_struct.struct_field_visitor_t_visit_field(self, *args)

    def __init__(self, *args):
        r"""


        __init__(self) -> struct_field_visitor_t
            self: PyObject *
        """
        if self.__class__ == struct_field_visitor_t:
            _self = None
        else:
            _self = self
        _ida_struct.struct_field_visitor_t_swiginit(self, _ida_struct.new_struct_field_visitor_t(_self, *args))
    __swig_destroy__ = _ida_struct.delete_struct_field_visitor_t
    def __disown__(self):
        self.this.disown()
        _ida_struct.disown_struct_field_visitor_t(self)
        return weakref.proxy(self)

# Register struct_field_visitor_t in _ida_struct:
_ida_struct.struct_field_visitor_t_swigregister(struct_field_visitor_t)


def visit_stroff_fields(*args) -> "adiff_t *":
    r"""


    Visit structure fields in a stroff expression or in a reference to a
    struct data variable. This function can be used to enumerate all
    components of an expression like 'a.b.c'.
    
    visit_stroff_fields(sfv, path, disp, appzero) -> flags_t
        @param sfv: visitor object (C++: struct_field_visitor_t  &)
        @param path: struct path (path[0] contains the initial struct id)
                     (C++: const  tid_t  *)
        @param disp: offset into structure (C++: adiff_t *)
        @param appzero: should visit field at offset zero? (C++: bool)
    """
    return _ida_struct.visit_stroff_fields(*args)

def stroff_as_size(*args) -> "bool":
    r"""


    Should display a structure offset expression as the structure size?
    
    stroff_as_size(plen, sptr, value) -> bool
        @param plen (C++: int)
        @param sptr (C++: const  struc_t  *)
        @param value (C++: asize_t)
    """
    return _ida_struct.stroff_as_size(*args)

def get_innermost_member(*args) -> "PyObject *":
    r"""


    get_innermost_member(sptr, offset) -> PyObject *
    Get the innermost member at the given offset
    @param sptr: the starting structure
    @param offset: offset into the starting structure
    @return:
        - None on failure
        - tuple(member_t, struct_t, offset)
          where member_t: a member in SPTR (it is not a structure),
                struct_t: the innermost structure,
                offset:   remaining offset into the returned member
    """
    return _ida_struct.get_innermost_member(*args)

if _BC695:
    get_member_name2=get_member_name
    def get_member_tinfo(*args):
        import ida_typeinf
        if isinstance(args[1], ida_typeinf.tinfo_t):  # 6.95: mptr, tinfo_t
            mptr, tif = args
        else:                                         # 7.00: tinfo_t, mptr
            tif, mptr = args
        return _ida_struct.get_member_tinfo(tif, mptr);
    def get_or_guess_member_tinfo(*args):
        import ida_typeinf
        if isinstance(args[1], ida_typeinf.tinfo_t):  # 6.95: mptr, tinfo_t
            mptr, tif = args
        else:                                         # 7.00: tinfo_t, mptr
            tif, mptr = args
        return _ida_struct.get_or_guess_member_tinfo(tif, mptr);
# note: if needed we might have to re-implement get_member_tinfo()
# and look whether there is a 2nd, 'tinfo_t' parameter (since the
# original get_member_tinfo function has a different signature)
    get_member_tinfo2=get_member_tinfo
# same here
    get_or_guess_member_tinfo2=get_or_guess_member_tinfo
    save_struc2=save_struc
    set_member_tinfo2=set_member_tinfo
