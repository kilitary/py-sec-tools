#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: expr
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_expr
else:
    import _ida_expr

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

SWIG_PYTHON_LEGACY_BOOL = _ida_expr.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func


def compile_idc_file(*args) -> "qstring *":
    r"""


    compile_idc_file(nonnul_line) -> str
        nonnul_line: char const *
    """
    return _ida_expr.compile_idc_file(*args)

def compile_idc_text(*args) -> "qstring *":
    r"""


    compile_idc_text(nonnul_line) -> str
        nonnul_line: char const *
    """
    return _ida_expr.compile_idc_text(*args)

def py_get_call_idc_func(*args) -> "size_t":
    r"""
    py_get_call_idc_func() -> size_t
    """
    return _ida_expr.py_get_call_idc_func(*args)

def pyw_register_idc_func(*args) -> "size_t":
    r"""


    pyw_register_idc_func(name, args, py_fp) -> size_t
        name: char const *
        args: char const *
        py_fp: PyObject *
    """
    return _ida_expr.pyw_register_idc_func(*args)

def pyw_unregister_idc_func(*args) -> "bool":
    r"""


    pyw_unregister_idc_func(ctxptr) -> bool
        ctxptr: size_t
    """
    return _ida_expr.pyw_unregister_idc_func(*args)

def pyw_convert_defvals(*args) -> "bool":
    r"""


    pyw_convert_defvals(out, py_seq) -> bool
        out: idc_values_t *
        py_seq: PyObject *
    """
    return _ida_expr.pyw_convert_defvals(*args)

def py_add_idc_func(*args) -> "bool":
    r"""


    py_add_idc_func(name, fp_ptr, args, defvals, flags) -> bool
        name: char const *
        fp_ptr: size_t
        args: char const *
        defvals: idc_values_t const &
        flags: int
    """
    return _ida_expr.py_add_idc_func(*args)

def eval_expr(*args) -> "qstring *":
    r"""


    Compile and calculate an expression.
    
    eval_expr(rv, where, line) -> str
        @param rv: pointer to the result (C++: idc_value_t  *)
        @param where: the current linear address in the addressing space of
                      the program being disassembled. If will be used to
                      resolve names of local variables etc. if not applicable,
                      then should be  BADADDR . (C++: ea_t)
        @param line: the expression to evaluate (C++: const char *)
        @retval: true - ok
        @retval: false - error, see errbuf
    """
    return _ida_expr.eval_expr(*args)

def eval_idc_expr(*args) -> "qstring *":
    r"""


    Same as 'eval_expr()' , but will always use the IDC interpreter
    regardless of the currently installed extlang.
    
    eval_idc_expr(rv, where, line) -> str
        @param rv (C++: idc_value_t  *)
        @param where (C++: ea_t)
        line: char const *
    """
    return _ida_expr.eval_idc_expr(*args)
IDC_LANG_EXT = _ida_expr.IDC_LANG_EXT
"""
IDC script extension.
"""


def idcv_long(*args) -> "error_t":
    r"""


    Convert IDC variable to a long (32/64bit) number.
    
    idcv_long(v) -> error_t
        @param v (C++: idc_value_t  *)
        @return: v = 0 if impossible to convert to long
    """
    return _ida_expr.idcv_long(*args)

def idcv_int64(*args) -> "error_t":
    r"""


    Convert IDC variable to a 64bit number.
    
    idcv_int64(v) -> error_t
        @param v (C++: idc_value_t  *)
        @return: v = 0 if impossible to convert to int64
    """
    return _ida_expr.idcv_int64(*args)

def idcv_num(*args) -> "error_t":
    r"""


    Convert IDC variable to a long number.
    
    idcv_num(v) -> error_t
        @param v (C++: idc_value_t  *)
        @return: v = 0 if IDC variable = "false" string   v = 1 if IDC
                 variable = "true" string   v = number if IDC variable is
                 number or string containing a number   eTypeConflict if IDC
                 variable = empty string
    """
    return _ida_expr.idcv_num(*args)

def idcv_string(*args) -> "error_t":
    r"""


    Convert IDC variable to a text string.
    
    idcv_string(v) -> error_t
        @param v (C++: idc_value_t  *)
    """
    return _ida_expr.idcv_string(*args)

def idcv_float(*args) -> "error_t":
    r"""


    Convert IDC variable to a floating point.
    
    idcv_float(v) -> error_t
        @param v (C++: idc_value_t  *)
    """
    return _ida_expr.idcv_float(*args)

def idcv_object(*args) -> "error_t":
    r"""


    Create an IDC object. The original value of 'v' is discarded (freed).
    
    idcv_object(v, icls=None) -> error_t
        @param v: variable to hold the object. any previous value will be
                  cleaned (C++: idc_value_t  *)
        @param icls: ptr to the desired class. NULL means "object" class this
                     ptr must be returned by  add_idc_class()  or
                     find_idc_class() (C++: const idc_class_t *)
        @return: always eOk
    """
    return _ida_expr.idcv_object(*args)

def move_idcv(*args) -> "error_t":
    r"""


    Move 'src' to 'dst'. This function is more effective than copy_idcv
    since it never copies big amounts of data.
    
    move_idcv(dst, src) -> error_t
        @param dst (C++: idc_value_t  *)
        @param src (C++: idc_value_t  *)
    """
    return _ida_expr.move_idcv(*args)

def copy_idcv(*args) -> "error_t":
    r"""


    Copy 'src' to 'dst'. For idc objects only a reference is copied.
    
    copy_idcv(dst, src) -> error_t
        @param dst (C++: idc_value_t  *)
        @param src (C++: const  idc_value_t  &)
    """
    return _ida_expr.copy_idcv(*args)

def deep_copy_idcv(*args) -> "error_t":
    r"""


    Deep copy an IDC object. This function performs deep copy of idc
    objects. If 'src' is not an object, 'copy_idcv()' will be called
    
    deep_copy_idcv(dst, src) -> error_t
        @param dst (C++: idc_value_t  *)
        @param src (C++: const  idc_value_t  &)
    """
    return _ida_expr.deep_copy_idcv(*args)

def free_idcv(*args) -> "void":
    r"""


    Free storage used by 'VT_STR' / 'VT_OBJ' IDC variables. After this
    call the variable has a numeric value 0
    
    free_idcv(v)
        @param v (C++: idc_value_t  *)
    """
    return _ida_expr.free_idcv(*args)

def swap_idcvs(*args) -> "void":
    r"""


    Swap 2 variables.
    
    swap_idcvs(v1, v2)
        @param v1 (C++: idc_value_t  *)
        @param v2 (C++: idc_value_t  *)
    """
    return _ida_expr.swap_idcvs(*args)

def get_idcv_class_name(*args) -> "qstring *":
    r"""


    Retrieves the IDC object class name.
    
    get_idcv_class_name(obj) -> str
        @param obj: class instance variable (C++: const  idc_value_t  *)
        @return: error code, eOk on success
    """
    return _ida_expr.get_idcv_class_name(*args)

def get_idcv_attr(*args) -> "error_t":
    r"""


    Get an object attribute.
    
    get_idcv_attr(res, obj, attr, may_use_getattr=False) -> error_t
        @param res: buffer for the attribute value (C++: idc_value_t  *)
        @param obj: variable that holds an object reference. if obj is NULL it
                    searches global variables, then user functions (C++: const
                    idc_value_t  *)
        @param attr: attribute name (C++: const char *)
        @param may_use_getattr: may call getattr functions to calculate the
                                attribute if it does not exist (C++: bool)
        @return: error code, eOk on success
    """
    return _ida_expr.get_idcv_attr(*args)

def set_idcv_attr(*args) -> "error_t":
    r"""


    Set an object attribute.
    
    set_idcv_attr(obj, attr, value, may_use_setattr=False) -> error_t
        @param obj: variable that holds an object reference. if obj is NULL
                    then it tries to modify a global variable with the
                    attribute name (C++: idc_value_t  *)
        @param attr: attribute name (C++: const char *)
        @param value: new attribute value (C++: const  idc_value_t  &)
        @param may_use_setattr: may call setattr functions for the class (C++:
                                bool)
        @return: error code, eOk on success
    """
    return _ida_expr.set_idcv_attr(*args)

def del_idcv_attr(*args) -> "error_t":
    r"""


    Delete an object attribute.
    
    del_idcv_attr(obj, attr) -> error_t
        @param obj: variable that holds an object reference (C++: idc_value_t
                    *)
        @param attr: attribute name (C++: const char *)
        @return: error code, eOk on success
    """
    return _ida_expr.del_idcv_attr(*args)

def first_idcv_attr(*args) -> "char const *":
    r"""


    first_idcv_attr(obj) -> char const *
        @param obj (C++: const  idc_value_t  *)
    """
    return _ida_expr.first_idcv_attr(*args)

def last_idcv_attr(*args) -> "char const *":
    r"""


    last_idcv_attr(obj) -> char const *
        @param obj (C++: const  idc_value_t  *)
    """
    return _ida_expr.last_idcv_attr(*args)

def next_idcv_attr(*args) -> "char const *":
    r"""


    next_idcv_attr(obj, attr) -> char const *
        @param obj (C++: const  idc_value_t  *)
        @param attr (C++: const char *)
    """
    return _ida_expr.next_idcv_attr(*args)

def prev_idcv_attr(*args) -> "char const *":
    r"""


    prev_idcv_attr(obj, attr) -> char const *
        @param obj (C++: const  idc_value_t  *)
        @param attr (C++: const char *)
    """
    return _ida_expr.prev_idcv_attr(*args)

def print_idcv(*args) -> "qstring *":
    r"""


    Get text representation of 'idc_value_t' .
    
    print_idcv(v, name=None, indent=0) -> str
        @param v (C++: const  idc_value_t  &)
        @param name (C++: const char *)
        @param indent (C++: int)
    """
    return _ida_expr.print_idcv(*args)

def get_idcv_slice(*args) -> "error_t":
    r"""


    Get slice.
    
    get_idcv_slice(res, v, i1, i2, flags=0) -> error_t
        @param res: output variable that will contain the slice (C++:
                    idc_value_t  *)
        @param v: input variable (string or object) (C++: const  idc_value_t
                  *)
        @param i1: slice start index (C++: uval_t)
        @param i2: slice end index (excluded) (C++: uval_t)
        @param flags: IDC variable slice flags  or 0 (C++: int)
        @return: eOk if success
    """
    return _ida_expr.get_idcv_slice(*args)
VARSLICE_SINGLE = _ida_expr.VARSLICE_SINGLE
"""
return single index (i2 is ignored)
"""


def set_idcv_slice(*args) -> "error_t":
    r"""


    Set slice.
    
    set_idcv_slice(v, i1, i2, _in, flags=0) -> error_t
        @param v: variable to modify (string or object) (C++: idc_value_t  *)
        @param i1: slice start index (C++: uval_t)
        @param i2: slice end index (excluded) (C++: uval_t)
        in: idc_value_t const &
        @param flags: IDC variable slice flags  or 0 (C++: int)
        @return: eOk on success
    """
    return _ida_expr.set_idcv_slice(*args)

def add_idc_class(*args) -> "idc_class_t *":
    r"""


    Create a new IDC class.
    
    add_idc_class(name, super=None) -> idc_class_t *
        @param name: name of the new class (C++: const char *)
        @param super: the base class for the new class. if the new class is
                      not based on any other class, pass NULL (C++: const
                      idc_class_t *)
        @return: pointer to the created class. If such a class already exists,
                 a pointer to it will be returned. Pointers to other existing
                 classes may be invalidated by this call.
    """
    return _ida_expr.add_idc_class(*args)

def find_idc_class(*args) -> "idc_class_t *":
    r"""


    Find an existing IDC class by its name.
    
    find_idc_class(name) -> idc_class_t *
        @param name: name of the class (C++: const char *)
        @return: pointer to the class or NULL. The returned pointer is valid
                 until a new call to  add_idc_class()
    """
    return _ida_expr.find_idc_class(*args)

def deref_idcv(*args) -> "idc_value_t *":
    r"""


    Dereference a 'VT_REF' variable.
    
    deref_idcv(v, vref_flags) -> idc_value_t
        @param v: variable to dereference (C++: idc_value_t  *)
        @param vref_flags: Dereference IDC variable flags (C++: int)
        @return: pointer to the dereference result or NULL. If returns NULL,
                 qerrno is set to eExecBadRef "Illegal variable reference"
    """
    return _ida_expr.deref_idcv(*args)
VREF_LOOP = _ida_expr.VREF_LOOP
"""
dereference until we get a non 'VT_REF'
"""

VREF_ONCE = _ida_expr.VREF_ONCE
"""
dereference only once, do not loop
"""

VREF_COPY = _ida_expr.VREF_COPY
"""
copy the result to the input var (v)
"""


def create_idcv_ref(*args) -> "bool":
    r"""


    Create a variable reference. Currently only references to global
    variables can be created.
    
    create_idcv_ref(ref, v) -> bool
        @param ref: ptr to the result (C++: idc_value_t  *)
        @param v: variable to reference (C++: const  idc_value_t  *)
        @return: success
    """
    return _ida_expr.create_idcv_ref(*args)

def add_idc_gvar(*args) -> "idc_value_t *":
    r"""


    Add global IDC variable.
    
    add_idc_gvar(name) -> idc_value_t
        @param name: name of the global variable (C++: const char *)
        @return: pointer to the created variable or existing variable. NB: the
                 returned pointer is valid until a new global var is added.
    """
    return _ida_expr.add_idc_gvar(*args)

def find_idc_gvar(*args) -> "idc_value_t *":
    r"""


    Find an existing global IDC variable by its name.
    
    find_idc_gvar(name) -> idc_value_t
        @param name: name of the global variable (C++: const char *)
        @return: pointer to the variable or NULL. NB: the returned pointer is
                 valid until a new global var is added. FIXME: it is difficult
                 to use this function in a thread safe manner
    """
    return _ida_expr.find_idc_gvar(*args)
class idc_value_t(object):
    r"""
    Proxy of C++ idc_value_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    vtype = property(_ida_expr.idc_value_t_vtype_get, _ida_expr.idc_value_t_vtype_set)
    num = property(_ida_expr.idc_value_t_num_get, _ida_expr.idc_value_t_num_set)
    e = property(_ida_expr.idc_value_t_e_get, _ida_expr.idc_value_t_e_set)
    obj = property(_ida_expr.idc_value_t_obj_get, _ida_expr.idc_value_t_obj_set)
    funcidx = property(_ida_expr.idc_value_t_funcidx_get, _ida_expr.idc_value_t_funcidx_set)
    pvoid = property(_ida_expr.idc_value_t_pvoid_get, _ida_expr.idc_value_t_pvoid_set)
    i64 = property(_ida_expr.idc_value_t_i64_get, _ida_expr.idc_value_t_i64_set)
    reserve = property(_ida_expr.idc_value_t_reserve_get, _ida_expr.idc_value_t_reserve_set)

    def __init__(self, *args):
        r"""


        __init__(self, n=0) -> idc_value_t
            n: sval_t
        

        __init__(self, r) -> idc_value_t
            r: idc_value_t const &
        

        __init__(self, _str) -> idc_value_t
            _str: char const *
        """
        _ida_expr.idc_value_t_swiginit(self, _ida_expr.new_idc_value_t(*args))
    __swig_destroy__ = _ida_expr.delete_idc_value_t

    def clear(self, *args) -> "void":
        r"""


        See 'free_idcv()'
        """
        return _ida_expr.idc_value_t_clear(self, *args)

    def qstr(self, *args) -> "qstring const &":
        r"""


        'VT_STR'
        """
        return _ida_expr.idc_value_t_qstr(self, *args)

    def c_str(self, *args) -> "char const *":
        r"""


        'VT_STR'
        """
        return _ida_expr.idc_value_t_c_str(self, *args)

    def u_str(self, *args) -> "uchar const *":
        r"""


        'VT_STR'
        """
        return _ida_expr.idc_value_t_u_str(self, *args)

    def swap(self, *args) -> "void":
        r"""


        Set this = r and v = this.
        
        swap(self, v)
            @param v (C++: idc_value_t  &)
        """
        return _ida_expr.idc_value_t_swap(self, *args)

    def is_zero(self, *args) -> "bool":
        r"""


        Does value represent the integer 0?
        """
        return _ida_expr.idc_value_t_is_zero(self, *args)

    def is_integral(self, *args) -> "bool":
        r"""


        Does value represent a whole number?
        """
        return _ida_expr.idc_value_t_is_integral(self, *args)

    def is_convertible(self, *args) -> "bool":
        r"""


        Convertible types are 'VT_LONG' , 'VT_FLOAT' , 'VT_INT64' , and
        'VT_STR' .
        """
        return _ida_expr.idc_value_t_is_convertible(self, *args)

    def _create_empty_string(self, *args) -> "void":
        r"""
        _create_empty_string(self)
        """
        return _ida_expr.idc_value_t__create_empty_string(self, *args)

    def create_empty_string(self, *args) -> "void":
        r"""
        create_empty_string(self)
        """
        return _ida_expr.idc_value_t_create_empty_string(self, *args)

    def set_string(self, *args) -> "void":
        r"""


        set_string(self, _str, len)
            _str: char const *
            len: size_t
        

        set_string(self, _str)
            _str: char const *
        """
        return _ida_expr.idc_value_t_set_string(self, *args)

    def set_long(self, *args) -> "void":
        r"""


        set_long(self, v)
            v: sval_t
        """
        return _ida_expr.idc_value_t_set_long(self, *args)

    def set_pvoid(self, *args) -> "void":
        r"""


        set_pvoid(self, p)
            p: void *
        """
        return _ida_expr.idc_value_t_set_pvoid(self, *args)

    def set_int64(self, *args) -> "void":
        r"""


        set_int64(self, v)
            v: int64
        """
        return _ida_expr.idc_value_t_set_int64(self, *args)

    def set_float(self, *args) -> "void":
        r"""


        set_float(self, f)
            f: fpvalue_t const &
        """
        return _ida_expr.idc_value_t_set_float(self, *args)

    str = property(lambda self: self.c_str(), lambda self, v: self.set_string(v))


# Register idc_value_t in _ida_expr:
_ida_expr.idc_value_t_swigregister(idc_value_t)
VT_LONG = _ida_expr.VT_LONG
"""
Integer (see 'idc_value_t::num' )
"""

VT_FLOAT = _ida_expr.VT_FLOAT
"""
Floating point (see 'idc_value_t::e' )
"""

VT_WILD = _ida_expr.VT_WILD
"""
Function with arbitrary number of arguments. The actual number of
arguments will be passed in 'idc_value_t::num' . This value should not
be used for 'idc_value_t' .
"""

VT_OBJ = _ida_expr.VT_OBJ
"""
Object (see idc_value_t::obj)
"""

VT_FUNC = _ida_expr.VT_FUNC
"""
Function (see 'idc_value_t::funcidx' )
"""

VT_STR = _ida_expr.VT_STR
"""
String (see qstr() and similar functions)
"""

VT_PVOID = _ida_expr.VT_PVOID
"""
void *
"""

VT_INT64 = _ida_expr.VT_INT64
"""
i64
"""

VT_REF = _ida_expr.VT_REF
"""
Reference.
"""


class idc_global_t(object):
    r"""
    Proxy of C++ idc_global_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_ida_expr.idc_global_t_name_get, _ida_expr.idc_global_t_name_set)
    value = property(_ida_expr.idc_global_t_value_get, _ida_expr.idc_global_t_value_set)

    def __init__(self, *args):
        r"""


        __init__(self) -> idc_global_t
            n: char const *
        """
        _ida_expr.idc_global_t_swiginit(self, _ida_expr.new_idc_global_t(*args))
    __swig_destroy__ = _ida_expr.delete_idc_global_t

# Register idc_global_t in _ida_expr:
_ida_expr.idc_global_t_swigregister(idc_global_t)

eExecThrow = _ida_expr.eExecThrow
"""
See return value of 'idc_func_t' .
"""


def find_idc_func(*args) -> "qstring *":
    r"""


    find_idc_func(prefix, n=0) -> str
        @param prefix (C++: const char *)
        @param n (C++: int)
    """
    return _ida_expr.find_idc_func(*args)
HF_DEFAULT = _ida_expr.HF_DEFAULT

HF_KEYWORD1 = _ida_expr.HF_KEYWORD1

HF_KEYWORD2 = _ida_expr.HF_KEYWORD2

HF_KEYWORD3 = _ida_expr.HF_KEYWORD3

HF_STRING = _ida_expr.HF_STRING

HF_COMMENT = _ida_expr.HF_COMMENT

HF_PREPROC = _ida_expr.HF_PREPROC

HF_NUMBER = _ida_expr.HF_NUMBER

HF_MAX = _ida_expr.HF_MAX

class highlighter_cbs_t(object):
    r"""
    Proxy of C++ highlighter_cbs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _ida_expr.delete_highlighter_cbs_t

    def set_style(self, *args) -> "void":
        r"""


        set_style(self, arg0, arg1, arg2)
            arg0: int32
            arg1: int32
            arg2: enum syntax_highlight_style
        """
        return _ida_expr.highlighter_cbs_t_set_style(self, *args)

    def prev_block_state(self, *args) -> "int32":
        r"""
        prev_block_state(self) -> int32
        """
        return _ida_expr.highlighter_cbs_t_prev_block_state(self, *args)

    def cur_block_state(self, *args) -> "int32":
        r"""
        cur_block_state(self) -> int32
        """
        return _ida_expr.highlighter_cbs_t_cur_block_state(self, *args)

    def set_block_state(self, *args) -> "void":
        r"""


        set_block_state(self, arg0)
            arg0: int32
        """
        return _ida_expr.highlighter_cbs_t_set_block_state(self, *args)

    def __init__(self, *args):
        r"""


        __init__(self) -> highlighter_cbs_t
            self: PyObject *
        """
        if self.__class__ == highlighter_cbs_t:
            _self = None
        else:
            _self = self
        _ida_expr.highlighter_cbs_t_swiginit(self, _ida_expr.new_highlighter_cbs_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_expr.disown_highlighter_cbs_t(self)
        return weakref.proxy(self)

# Register highlighter_cbs_t in _ida_expr:
_ida_expr.highlighter_cbs_t_swigregister(highlighter_cbs_t)


def set_header_path(*args) -> "bool":
    r"""


    Set or append a header path. IDA looks for the include files in the
    appended header paths, then in the ida executable directory.
    
    set_header_path(path, add) -> bool
        @param path: list of directories to add (separated by ';') may be
                     NULL, in this case nothing is added (C++: const char *)
        @param add: true: append. false: remove old paths. (C++: bool)
        @retval: true - success
        @retval: false - no memory
    """
    return _ida_expr.set_header_path(*args)

def get_idc_filename(*args) -> "char const *":
    r"""


    Get full name of IDC file name. Search for file in list of include
    directories, IDCPATH directory and system directories.
    
    get_idc_filename(file) -> str
        @param file: file name without full path (C++: const char *)
        @return: NULL is file not found. otherwise returns pointer to buf
    """
    return _ida_expr.get_idc_filename(*args)

def exec_system_script(*args) -> "bool":
    r"""


    Compile and execute "main" function from system file.
    
    exec_system_script(file, complain_if_no_file=True) -> bool
        @param file: file name with IDC function(s). The file will be searched
                     using  get_idc_filename() . (C++: const char *)
        @param complain_if_no_file: 1: display warning if the file is not
                                    found   0: don't complain if file doesn't
                                    exist (C++: bool)
        @retval: 1 - ok, file is compiled and executed
        @retval: 0 - failure, compilation or execution error, warning is
                     displayed
    """
    return _ida_expr.exec_system_script(*args)
CPL_DEL_MACROS = _ida_expr.CPL_DEL_MACROS
"""
delete macros at the end of compilation
"""

CPL_USE_LABELS = _ida_expr.CPL_USE_LABELS
"""
allow program labels in the script
"""

CPL_ONLY_SAFE = _ida_expr.CPL_ONLY_SAFE
"""
allow calls of only thread-safe functions
"""


def compile_idc_snippet(*args) -> "qstring *":
    r"""


    Compile text with IDC statements.
    
    compile_idc_snippet(func, text, resolver=None, only_safe_funcs=False) -> str
        @param func: name of the function to create out of the snippet (C++:
                     const char *)
        @param text: text to compile (C++: const char *)
        @param resolver: callback object to get values of undefined variables
                         This object will be called if IDC function contains
                         references to undefined variables. May be NULL. (C++:
                         idc_resolver_t  *)
        @param only_safe_funcs: if true, any calls to functions without
                                EXTFUN_SAFE  flag will lead to a compilation
                                error. (C++: bool)
        @retval: true - ok
        @retval: false - error, see errbuf
    """
    return _ida_expr.compile_idc_snippet(*args)

def exec_idc_script(*args) -> "qstring *":
    r"""


    Compile and execute IDC function(s) from file.
    
    exec_idc_script(result, path, func, args, argsnum) -> str
        @param result: ptr to  idc_value_t  to hold result of the function. If
                       execution fails, this variable will contain the
                       exception information. You may pass NULL if you are not
                       interested in the returned value. (C++: idc_value_t  *)
        @param path: text file containing text of IDC functions (C++: const
                     char *)
        @param func: function name to execute (C++: const char *)
        @param args: array of parameters (C++: const  idc_value_t)
        @param argsnum: number of parameters to pass to 'fname' This number
                        should be equal to number of parameters the function
                        expects. (C++: size_t)
        @retval: true - ok
        @retval: false - error, see errbuf
    """
    return _ida_expr.exec_idc_script(*args)

def throw_idc_exception(*args) -> "error_t":
    r"""


    Create an idc execution exception object. This helper function can be
    used to return an exception from C++ code to IDC. In other words this
    function can be called from 'idc_func_t()' callbacks. Sample usage: if
    ( !ok ) return throw_idc_exception(r, "detailed error msg");
    
    throw_idc_exception(r, desc) -> error_t
        @param r: object to hold the exception object (C++: idc_value_t  *)
        @param desc: exception description (C++: const char *)
        @return: eExecThrow
    """
    return _ida_expr.throw_idc_exception(*args)
class idc_values_t(object):
    r"""
    Proxy of C++ qvector< idc_value_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self) -> idc_values_t
            x: qvector< idc_value_t > const &
        """
        _ida_expr.idc_values_t_swiginit(self, _ida_expr.new_idc_values_t(*args))
    __swig_destroy__ = _ida_expr.delete_idc_values_t

    def push_back(self, *args) -> "idc_value_t &":
        r"""


        push_back(self, x)
            x: idc_value_t const &
        """
        return _ida_expr.idc_values_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_expr.idc_values_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_expr.idc_values_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_expr.idc_values_t_empty(self, *args)

    def at(self, *args) -> "idc_value_t const &":
        r"""


        at(self, _idx) -> idc_value_t
            _idx: size_t
        """
        return _ida_expr.idc_values_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_expr.idc_values_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_expr.idc_values_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""


        resize(self, _newsize, x)
            _newsize: size_t
            x: idc_value_t const &
        

        resize(self, _newsize)
            _newsize: size_t
        """
        return _ida_expr.idc_values_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""


        grow(self, x=idc_value_t())
            x: idc_value_t const &
        """
        return _ida_expr.idc_values_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_expr.idc_values_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""


        reserve(self, cnt)
            cnt: size_t
        """
        return _ida_expr.idc_values_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_expr.idc_values_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""


        swap(self, r)
            r: qvector< idc_value_t > &
        """
        return _ida_expr.idc_values_t_swap(self, *args)

    def extract(self, *args) -> "idc_value_t *":
        r"""
        extract(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""


        inject(self, s, len)
            s: idc_value_t *
            len: size_t
        """
        return _ida_expr.idc_values_t_inject(self, *args)

    def begin(self, *args) -> "qvector< idc_value_t >::const_iterator":
        r"""
        begin(self) -> idc_value_t
        begin(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_begin(self, *args)

    def end(self, *args) -> "qvector< idc_value_t >::const_iterator":
        r"""
        end(self) -> idc_value_t
        end(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_end(self, *args)

    def insert(self, *args) -> "qvector< idc_value_t >::iterator":
        r"""


        insert(self, it, x) -> idc_value_t
            it: qvector< idc_value_t >::iterator
            x: idc_value_t const &
        """
        return _ida_expr.idc_values_t_insert(self, *args)

    def erase(self, *args) -> "qvector< idc_value_t >::iterator":
        r"""


        erase(self, it) -> idc_value_t
            it: qvector< idc_value_t >::iterator
        

        erase(self, first, last) -> idc_value_t
            first: qvector< idc_value_t >::iterator
            last: qvector< idc_value_t >::iterator
        """
        return _ida_expr.idc_values_t_erase(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_expr.idc_values_t___len__(self, *args)

    def __getitem__(self, *args) -> "idc_value_t const &":
        r"""


        __getitem__(self, i) -> idc_value_t
            i: size_t
        """
        return _ida_expr.idc_values_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""


        __setitem__(self, i, v)
            i: size_t
            v: idc_value_t const &
        """
        return _ida_expr.idc_values_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register idc_values_t in _ida_expr:
_ida_expr.idc_values_t_swigregister(idc_values_t)


#<pycode(py_expr)>
try:
    import types
    import ctypes
# Callback for IDC func callback (On Windows, we use stdcall)
# typedef error_t idaapi idc_func_t(idc_value_t *argv,idc_value_t *r);
    try:
        _IDCFUNC_CB_T = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
    except:
        _IDCFUNC_CB_T = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

# A trampoline function that is called from idcfunc_t that will
# call the Python callback with the argv and r properly serialized to python
    call_idc_func__ = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(_ida_expr.py_get_call_idc_func())
except:
    def call_idc_func__(*args):
        warning("IDC extensions need ctypes library in order to work")
        return 0
    _IDCFUNC_CB_T = None

# --------------------------------------------------------------------------
EXTFUN_BASE  = 0x0001
"""
requires open database
"""
EXTFUN_NORET = 0x0002
"""
does not return. the interpreter may clean up its state before calling it.
"""
EXTFUN_SAFE  = 0x0004
"""
thread safe function. may be called
"""

# --------------------------------------------------------------------------
class _IdcFunction(object):
    """
    Internal class that calls pyw_call_idc_func() with a context
    """
    def __init__(self, ctxptr):
        self.ctxptr = ctxptr
# Take a reference to the ctypes callback
# (note: this will create a circular reference)
        self.cb = _IDCFUNC_CB_T(self)

    fp_ptr = property(lambda self: ctypes.cast(self.cb, ctypes.c_void_p).value)

    def __call__(self, args, res):
        return call_idc_func__(self.ctxptr, args, res)


# --------------------------------------------------------------------------
# Dictionary to remember IDC function names along with the context pointer
# retrieved by using the internal pyw_register_idc_func()
__IDC_FUNC_CTXS = {}

def del_idc_func(name):
    """


        Unregisters the specified IDC function
    
        @param name: IDC function name to unregister
    
        @return: Boolean
    """
    global __IDC_FUNC_CTXS

# Get the context
    f = __IDC_FUNC_CTXS.get(name, None)

    if f is None:
        return False # Not registered

# Break circular reference
    del f.cb

# Delete the name from the dictionary
    del __IDC_FUNC_CTXS[name]

# Delete the context and unregister the function
    return _ida_expr.pyw_unregister_idc_func(f.ctxptr)

# --------------------------------------------------------------------------
def add_idc_func(name, fp, args, defvals=(), flags=0):
    """


        Extends the IDC language by exposing a new IDC function that is backed up by a Python function
    
        @param name: IDC function name to expose
        @param fp: Python callable that will receive the arguments and return a tuple.
        @param args: Arguments. A tuple of idaapi.VT_XXX constants
        @param defvals: default argument values (optional)
        @param flags: IDC function flags. A combination of EXTFUN_XXX constants (optional)
    
        @return: Boolean
    """
    global __IDC_FUNC_CTXS

# Get the context
    f = __IDC_FUNC_CTXS.get(name, None)

# Registering a function that is already registered?
    if f is not None:
# Unregister it first
        del_idc_func(name)

# Convert the tupple argument info to a string
    args = "".join([chr(x) for x in args])

# make sure we don't have an obvious discrepancy between
# the number of args, and the provided default values
    if len(defvals) > len(args):
        return False

    vdefvals = idc_values_t()
    if not _ida_expr.pyw_convert_defvals(vdefvals, defvals):
        return False

# Create a context
    ctxptr = _ida_expr.pyw_register_idc_func(name, args, fp)
    if ctxptr == 0:
        return False

# Bind the context with the IdcFunc object
    f = _IdcFunction(ctxptr)

# Remember the Python context
    __IDC_FUNC_CTXS[name] = f

# Register IDC function with a callback
    return _ida_expr.py_add_idc_func(
                name,
                f.fp_ptr,
                args,
                vdefvals,
                flags)

#</pycode(py_expr)>


if _BC695:
    Compile=compile_idc_file
    CompileEx=compile_idc_file
    CompileLine=compile_idc_text
    VT_STR2=VT_STR
    VarCopy=copy_idcv
    VarDelAttr=del_idcv_attr
    VarDeref=deref_idcv
    VarFirstAttr=first_idcv_attr
    def VarGetAttr(obj, attr, res, may_use_getattr=False):
        return get_idcv_attr(res, obj, attr, may_use_getattr)
    VarGetClassName=get_idcv_class_name
    VarGetSlice=get_idcv_slice
    VarInt64=idcv_int64
    VarLastAttr=last_idcv_attr
    VarMove=move_idcv
    VarNextAttr=next_idcv_attr
    VarObject=idcv_object
    VarPrevAttr=prev_idcv_attr
    VarPrint=print_idcv
    VarRef=create_idcv_ref
    VarSetAttr=set_idcv_attr
    VarSetSlice=set_idcv_slice
    VarString2=idcv_string
    VarSwap=swap_idcvs
    def calc_idc_expr(where, expr, res):
        return eval_idc_expr(res, where, expr)
    def calcexpr(where, expr, res):
        return eval_expr(res, where, expr)
    def dosysfile(complain_if_no_file, fname):
        return exec_system_script(fname, complain_if_no_file)
    def execute(line):
        return eval_idc_snippet(None, line)
    py_set_idc_func_ex=py_add_idc_func
    def set_idc_func_ex(name, fp=None, args=(), flags=0):
        return add_idc_func(name, fp, args, (), flags)
