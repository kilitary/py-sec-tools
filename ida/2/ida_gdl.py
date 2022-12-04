#  Copyright> YEAR:2022 WHO:Sergey Efimov EMAIL:kilitary@gmail.com WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: gdl
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_gdl
else:
    import _ida_gdl

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

SWIG_PYTHON_LEGACY_BOOL = _ida_gdl.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

import ida_range
fcb_normal = _ida_gdl.fcb_normal

fcb_indjump = _ida_gdl.fcb_indjump

fcb_ret = _ida_gdl.fcb_ret

fcb_cndret = _ida_gdl.fcb_cndret

fcb_noret = _ida_gdl.fcb_noret

fcb_enoret = _ida_gdl.fcb_enoret

fcb_extern = _ida_gdl.fcb_extern

fcb_error = _ida_gdl.fcb_error

class node_iterator(object):
    r"""
    Proxy of C++ node_iterator class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self, _g, n) -> node_iterator
            _g: gdl_graph_t const *
            n: int
        """
        _ida_gdl.node_iterator_swiginit(self, _ida_gdl.new_node_iterator(*args))

    def __eq__(self, *args):
        r"""


        __eq__(self, n) -> bool
            n: node_iterator const &
        """
        return _ida_gdl.node_iterator___eq__(self, *args)

    def __ne__(self, *args):
        r"""


        __ne__(self, n) -> bool
            n: node_iterator const &
        """
        return _ida_gdl.node_iterator___ne__(self, *args)

    def __ref__(self, *args):
        r"""
        __ref__(self) -> int
        """
        return _ida_gdl.node_iterator___ref__(self, *args)
    __swig_destroy__ = _ida_gdl.delete_node_iterator

# Register node_iterator in _ida_gdl:
_ida_gdl.node_iterator_swigregister(node_iterator)

class gdl_graph_t(object):
    r"""
    Proxy of C++ gdl_graph_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _ida_gdl.delete_gdl_graph_t

    def get_node_label(self, *args):
        r"""


        get_node_label(self, n) -> char *
            @param n (C++: int)
        """
        return _ida_gdl.gdl_graph_t_get_node_label(self, *args)

    def print_graph_attributes(self, *args):
        r"""


        print_graph_attributes(self, fp)
            @param fp (C++: FILE *)
        """
        return _ida_gdl.gdl_graph_t_print_graph_attributes(self, *args)

    def print_node(self, *args):
        r"""


        print_node(self, fp, n) -> bool
            @param fp (C++: FILE *)
            @param n (C++: int)
        """
        return _ida_gdl.gdl_graph_t_print_node(self, *args)

    def print_edge(self, *args):
        r"""


        print_edge(self, fp, i, j) -> bool
            @param fp (C++: FILE *)
            @param i (C++: int)
            @param j (C++: int)
        """
        return _ida_gdl.gdl_graph_t_print_edge(self, *args)

    def print_node_attributes(self, *args):
        r"""


        print_node_attributes(self, fp, n)
            @param fp (C++: FILE *)
            @param n (C++: int)
        """
        return _ida_gdl.gdl_graph_t_print_node_attributes(self, *args)

    def size(self, *args):
        r"""
        size(self) -> int
        """
        return _ida_gdl.gdl_graph_t_size(self, *args)

    def node_qty(self, *args):
        r"""
        node_qty(self) -> int
        """
        return _ida_gdl.gdl_graph_t_node_qty(self, *args)

    def exists(self, *args):
        r"""


        exists(self, node) -> bool
            @param node (C++: int)
        """
        return _ida_gdl.gdl_graph_t_exists(self, *args)

    def entry(self, *args):
        r"""
        entry(self) -> int
        """
        return _ida_gdl.gdl_graph_t_entry(self, *args)

    def exit(self, *args):
        r"""
        exit(self) -> int
        """
        return _ida_gdl.gdl_graph_t_exit(self, *args)

    def nsucc(self, *args):
        r"""


        nsucc(self, node) -> int
            @param node (C++: int)
        """
        return _ida_gdl.gdl_graph_t_nsucc(self, *args)

    def npred(self, *args):
        r"""


        npred(self, node) -> int
            @param node (C++: int)
        """
        return _ida_gdl.gdl_graph_t_npred(self, *args)

    def succ(self, *args):
        r"""


        succ(self, node, i) -> int
            @param node (C++: int)
            @param i (C++: int)
        """
        return _ida_gdl.gdl_graph_t_succ(self, *args)

    def pred(self, *args):
        r"""


        pred(self, node, i) -> int
            @param node (C++: int)
            @param i (C++: int)
        """
        return _ida_gdl.gdl_graph_t_pred(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_gdl.gdl_graph_t_empty(self, *args)

    def get_node_color(self, *args):
        r"""


        get_node_color(self, n) -> bgcolor_t
            @param n (C++: int)
        """
        return _ida_gdl.gdl_graph_t_get_node_color(self, *args)

    def get_edge_color(self, *args):
        r"""


        get_edge_color(self, i, j) -> bgcolor_t
            @param i (C++: int)
            @param j (C++: int)
        """
        return _ida_gdl.gdl_graph_t_get_edge_color(self, *args)

    def nedge(self, *args):
        r"""


        nedge(self, node, ispred) -> size_t
            @param node (C++: int)
            @param ispred (C++: bool)
        """
        return _ida_gdl.gdl_graph_t_nedge(self, *args)

    def edge(self, *args):
        r"""


        edge(self, node, i, ispred) -> int
            @param node (C++: int)
            @param i (C++: int)
            @param ispred (C++: bool)
        """
        return _ida_gdl.gdl_graph_t_edge(self, *args)

    def front(self, *args):
        r"""
        front(self) -> int
        """
        return _ida_gdl.gdl_graph_t_front(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> node_iterator
        """
        return _ida_gdl.gdl_graph_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> node_iterator
        """
        return _ida_gdl.gdl_graph_t_end(self, *args)

    def __init__(self, *args):
        r"""


        __init__(self) -> gdl_graph_t
            self: PyObject *
        """
        if self.__class__ == gdl_graph_t:
            _self = None
        else:
            _self = self
        _ida_gdl.gdl_graph_t_swiginit(self, _ida_gdl.new_gdl_graph_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_gdl.disown_gdl_graph_t(self)
        return weakref.proxy(self)

# Register gdl_graph_t in _ida_gdl:
_ida_gdl.gdl_graph_t_swigregister(gdl_graph_t)


def gen_gdl(*args):
    r"""


    Create GDL file for graph.
    
    gen_gdl(g, fname)
        @param g (C++: const  gdl_graph_t  *)
        @param fname (C++: const char *)
    """
    return _ida_gdl.gen_gdl(*args)

def display_gdl(*args):
    r"""


    Display GDL file by calling wingraph32. The exact name of the grapher
    is taken from the configuration file and set up by
    'setup_graph_subsystem()' .
    
    display_gdl(fname) -> int
        @param fname (C++: const char *)
        @return: error code from os, 0 if ok
    """
    return _ida_gdl.display_gdl(*args)

def gen_flow_graph(*args):
    r"""


    Build and display a flow graph.
    
    gen_flow_graph(filename, title, pfn, ea1, ea2, gflags) -> bool
        @param filename: output file name. the file extension is not used.
                         maybe NULL. (C++: const char *)
        @param title: graph title (C++: const char *)
        @param pfn: function to graph (C++: func_t  *)
        @param ea1: if pfn == NULL, then the address range (C++: ea_t)
        @param ea2: if pfn == NULL, then the address range (C++: ea_t)
        @param gflags: combination of  Flow graph building flags . if none of
                       CHART_GEN_DOT ,  CHART_GEN_GDL ,  CHART_WINGRAPH  is
                       specified, the function will return false (C++: int)
        @return: success. if fails, a warning message is displayed on the
                 screen
    """
    return _ida_gdl.gen_flow_graph(*args)
CHART_PRINT_NAMES = _ida_gdl.CHART_PRINT_NAMES
"""
print labels for each block?
"""

CHART_GEN_DOT = _ida_gdl.CHART_GEN_DOT
"""
generate .dot file (file extension is forced to .dot)
"""

CHART_GEN_GDL = _ida_gdl.CHART_GEN_GDL
"""
generate .gdl file (file extension is forced to .gdl)
"""

CHART_WINGRAPH = _ida_gdl.CHART_WINGRAPH
"""
call grapher to display the graph
"""


def gen_simple_call_chart(*args):
    r"""


    Build and display a simple function call graph.
    
    gen_simple_call_chart(filename, wait, title, gflags) -> bool
        @param filename: output file name. the file extension is not used.
                         maybe NULL. (C++: const char *)
        @param wait: message to display during graph building (C++: const char
                     *)
        @param title: graph title (C++: const char *)
        @param gflags: combination of  CHART_NOLIBFUNCS  and  Flow graph
                       building flags . if none of  CHART_GEN_DOT ,
                       CHART_GEN_GDL ,  CHART_WINGRAPH  is specified, the
                       function will return false. (C++: int)
        @return: success. if fails, a warning message is displayed on the
                 screen
    """
    return _ida_gdl.gen_simple_call_chart(*args)

def gen_complex_call_chart(*args):
    r"""


    Build and display a complex xref graph.
    
    gen_complex_call_chart(filename, wait, title, ea1, ea2, flags, recursion_depth=-1) -> bool
        @param filename: output file name. the file extension is not used.
                         maybe NULL. (C++: const char *)
        @param wait: message to display during graph building (C++: const char
                     *)
        @param title: graph title (C++: const char *)
        @param ea1: address range (C++: ea_t)
        @param ea2: address range (C++: ea_t)
        @param flags: combination of  Call chart building flags  and  Flow
                      graph building flags . if none of  CHART_GEN_DOT ,
                      CHART_GEN_GDL ,  CHART_WINGRAPH  is specified, the
                      function will return false. (C++: int)
        @param recursion_depth: optional limit of recursion (C++: int32)
        @return: success. if fails, a warning message is displayed on the
                 screen
    """
    return _ida_gdl.gen_complex_call_chart(*args)
CHART_NOLIBFUNCS = _ida_gdl.CHART_NOLIBFUNCS
"""
don't include library functions in the graph
"""

CHART_REFERENCING = _ida_gdl.CHART_REFERENCING
"""
references to the addresses in the list
"""

CHART_REFERENCED = _ida_gdl.CHART_REFERENCED
"""
references from the addresses in the list
"""

CHART_RECURSIVE = _ida_gdl.CHART_RECURSIVE
"""
analyze added blocks
"""

CHART_FOLLOW_DIRECTION = _ida_gdl.CHART_FOLLOW_DIRECTION
"""
analyze references to added blocks only in the direction of the
reference who discovered the current block
"""

CHART_IGNORE_XTRN = _ida_gdl.CHART_IGNORE_XTRN

CHART_IGNORE_DATA_BSS = _ida_gdl.CHART_IGNORE_DATA_BSS

CHART_IGNORE_LIB_TO = _ida_gdl.CHART_IGNORE_LIB_TO
"""
ignore references to library functions
"""

CHART_IGNORE_LIB_FROM = _ida_gdl.CHART_IGNORE_LIB_FROM
"""
ignore references from library functions
"""

CHART_PRINT_COMMENTS = _ida_gdl.CHART_PRINT_COMMENTS

CHART_PRINT_DOTS = _ida_gdl.CHART_PRINT_DOTS
"""
print dots if xrefs exist outside of the range recursion depth
"""

class cancellable_graph_t(gdl_graph_t):
    r"""
    Proxy of C++ cancellable_graph_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    cancelled = property(_ida_gdl.cancellable_graph_t_cancelled_get, _ida_gdl.cancellable_graph_t_cancelled_set)

    def __init__(self, *args):
        r"""


        __init__(self) -> cancellable_graph_t
            self: PyObject *
        """
        if self.__class__ == cancellable_graph_t:
            _self = None
        else:
            _self = self
        _ida_gdl.cancellable_graph_t_swiginit(self, _ida_gdl.new_cancellable_graph_t(_self, *args))
    __swig_destroy__ = _ida_gdl.delete_cancellable_graph_t
    def __disown__(self):
        self.this.disown()
        _ida_gdl.disown_cancellable_graph_t(self)
        return weakref.proxy(self)

# Register cancellable_graph_t in _ida_gdl:
_ida_gdl.cancellable_graph_t_swigregister(cancellable_graph_t)

class qbasic_block_t(ida_range.range_t):
    r"""
    Proxy of C++ qbasic_block_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> qbasic_block_t
        """
        _ida_gdl.qbasic_block_t_swiginit(self, _ida_gdl.new_qbasic_block_t(*args))
    __swig_destroy__ = _ida_gdl.delete_qbasic_block_t

# Register qbasic_block_t in _ida_gdl:
_ida_gdl.qbasic_block_t_swigregister(qbasic_block_t)


def is_noret_block(*args):
    r"""


    Does this block never return?
    
    is_noret_block(btype) -> bool
        @param btype (C++: fc_block_type_t)
    """
    return _ida_gdl.is_noret_block(*args)

def is_ret_block(*args):
    r"""


    Does this block return?
    
    is_ret_block(btype) -> bool
        @param btype (C++: fc_block_type_t)
    """
    return _ida_gdl.is_ret_block(*args)
FC_PRINT = _ida_gdl.FC_PRINT
"""
print names (used only by display_flow_chart())
"""

FC_NOEXT = _ida_gdl.FC_NOEXT
"""
do not compute external blocks. Use this to prevent jumps leaving the
function from appearing in the flow chart. Unless specified, the
targets of those outgoing jumps will be present in the flow chart
under the form of one-instruction blocks
"""

FC_RESERVED = _ida_gdl.FC_RESERVED

FC_APPND = _ida_gdl.FC_APPND
"""
multirange flowchart (set by append_to_flowchart)
"""

FC_CHKBREAK = _ida_gdl.FC_CHKBREAK
"""
build_qflow_chart() may be aborted by user
"""

FC_CALL_ENDS = _ida_gdl.FC_CALL_ENDS
"""
call instructions terminate basic blocks
"""

FC_NOPREDS = _ida_gdl.FC_NOPREDS
"""
do not compute predecessor lists
"""

class qflow_chart_t(cancellable_graph_t):
    r"""
    Proxy of C++ qflow_chart_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    title = property(_ida_gdl.qflow_chart_t_title_get, _ida_gdl.qflow_chart_t_title_set)
    bounds = property(_ida_gdl.qflow_chart_t_bounds_get, _ida_gdl.qflow_chart_t_bounds_set)
    pfn = property(_ida_gdl.qflow_chart_t_pfn_get, _ida_gdl.qflow_chart_t_pfn_set)
    flags = property(_ida_gdl.qflow_chart_t_flags_get, _ida_gdl.qflow_chart_t_flags_set)
    nproper = property(_ida_gdl.qflow_chart_t_nproper_get, _ida_gdl.qflow_chart_t_nproper_set)

    def __init__(self, *args):
        r"""


        __init__(self) -> qflow_chart_t
            _title: char const *
            _pfn: func_t *
            _ea1: ea_t
            _ea2: ea_t
            _flags: int
        """
        _ida_gdl.qflow_chart_t_swiginit(self, _ida_gdl.new_qflow_chart_t(*args))
    __swig_destroy__ = _ida_gdl.delete_qflow_chart_t

    def create(self, *args):
        r"""


        create(self, _title, _pfn, _ea1, _ea2, _flags)
            @param _title (C++: const char *)
            @param _pfn (C++: func_t  *)
            @param _ea1 (C++: ea_t)
            @param _ea2 (C++: ea_t)
            @param _flags (C++: int)
        

        create(self, _title, ranges, _flags)
            @param _title (C++: const char *)
            ranges: rangevec_t const &
            @param _flags (C++: int)
        """
        return _ida_gdl.qflow_chart_t_create(self, *args)

    def append_to_flowchart(self, *args):
        r"""


        append_to_flowchart(self, ea1, ea2)
            @param ea1 (C++: ea_t)
            @param ea2 (C++: ea_t)
        """
        return _ida_gdl.qflow_chart_t_append_to_flowchart(self, *args)

    def refresh(self, *args):
        r"""
        refresh(self)
        """
        return _ida_gdl.qflow_chart_t_refresh(self, *args)

    def calc_block_type(self, *args):
        r"""


        calc_block_type(self, blknum) -> fc_block_type_t
            @param blknum (C++: size_t)
        """
        return _ida_gdl.qflow_chart_t_calc_block_type(self, *args)

    def is_ret_block(self, *args):
        r"""


        is_ret_block(self, blknum) -> bool
            @param blknum (C++: size_t)
        """
        return _ida_gdl.qflow_chart_t_is_ret_block(self, *args)

    def is_noret_block(self, *args):
        r"""


        is_noret_block(self, blknum) -> bool
            @param blknum (C++: size_t)
        """
        return _ida_gdl.qflow_chart_t_is_noret_block(self, *args)

    def print_node_attributes(self, *args):
        r"""


        print_node_attributes(self, fp, n)
            @param fp (C++: FILE *)
            @param n (C++: int)
        """
        return _ida_gdl.qflow_chart_t_print_node_attributes(self, *args)

    def nsucc(self, *args):
        r"""


        nsucc(self, node) -> int
            @param node (C++: int)
        """
        return _ida_gdl.qflow_chart_t_nsucc(self, *args)

    def npred(self, *args):
        r"""


        npred(self, node) -> int
            @param node (C++: int)
        """
        return _ida_gdl.qflow_chart_t_npred(self, *args)

    def succ(self, *args):
        r"""


        succ(self, node, i) -> int
            @param node (C++: int)
            @param i (C++: int)
        """
        return _ida_gdl.qflow_chart_t_succ(self, *args)

    def pred(self, *args):
        r"""


        pred(self, node, i) -> int
            @param node (C++: int)
            @param i (C++: int)
        """
        return _ida_gdl.qflow_chart_t_pred(self, *args)

    def get_node_label(self, *args):
        r"""


        get_node_label(self, n) -> char *
            @param n (C++: int)
        """
        return _ida_gdl.qflow_chart_t_get_node_label(self, *args)

    def size(self, *args):
        r"""
        size(self) -> int
        """
        return _ida_gdl.qflow_chart_t_size(self, *args)

    def print_names(self, *args):
        r"""
        print_names(self) -> bool
        """
        return _ida_gdl.qflow_chart_t_print_names(self, *args)

    def __getitem__(self, *args):
        r"""


        __getitem__(self, n) -> qbasic_block_t
            n: int
        """
        return _ida_gdl.qflow_chart_t___getitem__(self, *args)

# Register qflow_chart_t in _ida_gdl:
_ida_gdl.qflow_chart_t_swigregister(qflow_chart_t)


#<pycode(py_gdl)>
import types

import _ida_idaapi
import ida_idaapi
# -----------------------------------------------------------------------
class BasicBlock(object):
    """
    Basic block class. It is returned by the Flowchart class
    """
    def __init__(self, id, bb, fc):
        self._fc = fc

        self.id = id
        """
        Basic block ID
        """

        self.start_ea = bb.start_ea
        """
        start_ea of basic block
        """

        self.end_ea = bb.end_ea
        """
        end_ea of basic block
        """

        self.type  = self._fc._q.calc_block_type(self.id)
        """
        Block type (check fc_block_type_t enum)
        """


    def preds(self):
        """
        Iterates the predecessors list
        """
        q = self._fc._q
        for i in range(0, self._fc._q.npred(self.id)):
            yield self._fc[q.pred(self.id, i)]


    def succs(self):
        """
        Iterates the successors list
        """
        q = self._fc._q
        for i in range(0, q.nsucc(self.id)):
            yield self._fc[q.succ(self.id, i)]

    try:
        if _BC695:
            startEA = property(lambda self: self.start_ea, lambda self, ea: setattr(self, "start_ea", ea))
            endEA = property(lambda self: self.end_ea, lambda self, ea: setattr(self, "end_ea", ea))
        else:
            startEA = ida_idaapi._make_badattr_property("startEA", "start_ea")
            endEA = ida_idaapi._make_badattr_property("endEA", "end_ea")
    except:
        pass # BC695 not defined at compile-time

# -----------------------------------------------------------------------
class FlowChart(object):
    """
    Flowchart class used to determine basic blocks.
    Check ex_gdl_qflow_chart.py for sample usage.
    """
    def __init__(self, f=None, bounds=None, flags=0):
        """


                Constructor
                @param f: A func_t type, use get_func(ea) to get a reference
                @param bounds: A tuple of the form (start, end). Used if "f" is None
                @param flags: one of the FC_xxxx flags.
        """
        if (f is None) and (bounds is None or type(bounds) != tuple):
            raise Exception("Please specifiy either a function or start/end pair")

        if bounds is None:
            bounds = (_ida_idaapi.BADADDR, _ida_idaapi.BADADDR)

# Create the flowchart
        self._q = qflow_chart_t("", f, bounds[0], bounds[1], flags)

    size = property(lambda self: self._q.size())
    """
    Number of blocks in the flow chart
    """


    def refresh(self):
        """
        Refreshes the flow chart
        """
        self._q.refresh()


    def _getitem(self, index):
        return BasicBlock(index, self._q[index], self)


    def __iter__(self):
        return (self._getitem(index) for index in range(0, self.size))


    def __getitem__(self, index):
        """
        Returns a basic block

        @return: BasicBlock
        """
        if index >= self.size:
            raise KeyError
        else:
            return self._getitem(index)

FC_PREDS = 0 # obsolete bit, do not use

#</pycode(py_gdl)>
