# revised WHERE:RUSSIA WHY:L

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: lines
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_lines
else:
    import _ida_lines

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

SWIG_PYTHON_LEGACY_BOOL = _ida_lines.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

COLOR_ON = _ida_lines.COLOR_ON
"""
Followed by a color code ( 'color_t' ).

Escape character (ON).
"""

COLOR_OFF = _ida_lines.COLOR_OFF
"""
Followed by a color code ( 'color_t' ).

Escape character (OFF).
"""

COLOR_ESC = _ida_lines.COLOR_ESC
"""
Escape character (Quote next character). This is needed to output '\\1'
and '\\2' characters.
"""

COLOR_INV = _ida_lines.COLOR_INV
"""
Escape character (Inverse foreground and background colors). This
escape character has no corresponding 'COLOR_OFF' . Its action
continues until the next 'COLOR_INV' or end of line.
"""

SCOLOR_ON = _ida_lines.SCOLOR_ON
"""
Escape character (ON)
"""

SCOLOR_OFF = _ida_lines.SCOLOR_OFF
"""
Escape character (OFF)
"""

SCOLOR_ESC = _ida_lines.SCOLOR_ESC
"""
Escape character (Quote next character)
"""

SCOLOR_INV = _ida_lines.SCOLOR_INV
"""
Escape character (Inverse colors)
"""

SCOLOR_DEFAULT = _ida_lines.SCOLOR_DEFAULT
"""
Default.
"""

SCOLOR_REGCMT = _ida_lines.SCOLOR_REGCMT
"""
Regular comment.
"""

SCOLOR_RPTCMT = _ida_lines.SCOLOR_RPTCMT
"""
Repeatable comment (defined not here)
"""

SCOLOR_AUTOCMT = _ida_lines.SCOLOR_AUTOCMT
"""
Automatic comment.
"""

SCOLOR_INSN = _ida_lines.SCOLOR_INSN
"""
Instruction.
"""

SCOLOR_DATNAME = _ida_lines.SCOLOR_DATNAME
"""
Dummy Data Name.
"""

SCOLOR_DNAME = _ida_lines.SCOLOR_DNAME
"""
Regular Data Name.
"""

SCOLOR_DEMNAME = _ida_lines.SCOLOR_DEMNAME
"""
Demangled Name.
"""

SCOLOR_SYMBOL = _ida_lines.SCOLOR_SYMBOL
"""
Punctuation.
"""

SCOLOR_CHAR = _ida_lines.SCOLOR_CHAR
"""
Char constant in instruction.
"""

SCOLOR_STRING = _ida_lines.SCOLOR_STRING
"""
String constant in instruction.
"""

SCOLOR_NUMBER = _ida_lines.SCOLOR_NUMBER
"""
Numeric constant in instruction.
"""

SCOLOR_VOIDOP = _ida_lines.SCOLOR_VOIDOP
"""
Void operand.
"""

SCOLOR_CREF = _ida_lines.SCOLOR_CREF
"""
Code reference.
"""

SCOLOR_DREF = _ida_lines.SCOLOR_DREF
"""
Data reference.
"""

SCOLOR_CREFTAIL = _ida_lines.SCOLOR_CREFTAIL
"""
Code reference to tail byte.
"""

SCOLOR_DREFTAIL = _ida_lines.SCOLOR_DREFTAIL
"""
Data reference to tail byte.
"""

SCOLOR_ERROR = _ida_lines.SCOLOR_ERROR
"""
Error or problem.
"""

SCOLOR_PREFIX = _ida_lines.SCOLOR_PREFIX
"""
Line prefix.
"""

SCOLOR_BINPREF = _ida_lines.SCOLOR_BINPREF
"""
Binary line prefix bytes.
"""

SCOLOR_EXTRA = _ida_lines.SCOLOR_EXTRA
"""
Extra line.
"""

SCOLOR_ALTOP = _ida_lines.SCOLOR_ALTOP
"""
Alternative operand.
"""

SCOLOR_HIDNAME = _ida_lines.SCOLOR_HIDNAME
"""
Hidden name.
"""

SCOLOR_LIBNAME = _ida_lines.SCOLOR_LIBNAME
"""
Library function name.
"""

SCOLOR_LOCNAME = _ida_lines.SCOLOR_LOCNAME
"""
Local variable name.
"""

SCOLOR_CODNAME = _ida_lines.SCOLOR_CODNAME
"""
Dummy code name.
"""

SCOLOR_ASMDIR = _ida_lines.SCOLOR_ASMDIR
"""
Assembler directive.
"""

SCOLOR_MACRO = _ida_lines.SCOLOR_MACRO
"""
Macro.
"""

SCOLOR_DSTR = _ida_lines.SCOLOR_DSTR
"""
String constant in data directive.
"""

SCOLOR_DCHAR = _ida_lines.SCOLOR_DCHAR
"""
Char constant in data directive.
"""

SCOLOR_DNUM = _ida_lines.SCOLOR_DNUM
"""
Numeric constant in data directive.
"""

SCOLOR_KEYWORD = _ida_lines.SCOLOR_KEYWORD
"""
Keywords.
"""

SCOLOR_REG = _ida_lines.SCOLOR_REG
"""
Register name.
"""

SCOLOR_IMPNAME = _ida_lines.SCOLOR_IMPNAME
"""
Imported name.
"""

SCOLOR_SEGNAME = _ida_lines.SCOLOR_SEGNAME
"""
Segment name.
"""

SCOLOR_UNKNAME = _ida_lines.SCOLOR_UNKNAME
"""
Dummy unknown name.
"""

SCOLOR_CNAME = _ida_lines.SCOLOR_CNAME
"""
Regular code name.
"""

SCOLOR_UNAME = _ida_lines.SCOLOR_UNAME
"""
Regular unknown name.
"""

SCOLOR_COLLAPSED = _ida_lines.SCOLOR_COLLAPSED
"""
Collapsed line.
"""

SCOLOR_ADDR = _ida_lines.SCOLOR_ADDR
"""
Hidden address mark.
"""

COLOR_SELECTED = _ida_lines.COLOR_SELECTED
"""
Selected.
"""

COLOR_LIBFUNC = _ida_lines.COLOR_LIBFUNC
"""
Library function.
"""

COLOR_REGFUNC = _ida_lines.COLOR_REGFUNC
"""
Regular function.
"""

COLOR_CODE = _ida_lines.COLOR_CODE
"""
Single instruction.
"""

COLOR_DATA = _ida_lines.COLOR_DATA
"""
Data bytes.
"""

COLOR_UNKNOWN = _ida_lines.COLOR_UNKNOWN
"""
Unexplored byte.
"""

COLOR_EXTERN = _ida_lines.COLOR_EXTERN
"""
External name definition segment.
"""

COLOR_CURITEM = _ida_lines.COLOR_CURITEM
"""
Current item.
"""

COLOR_CURLINE = _ida_lines.COLOR_CURLINE
"""
Current line.
"""

COLOR_HIDLINE = _ida_lines.COLOR_HIDLINE
"""
Hidden line.
"""

COLOR_LUMFUNC = _ida_lines.COLOR_LUMFUNC
"""
Lumina function.
"""

COLOR_BG_MAX = _ida_lines.COLOR_BG_MAX
"""
Max color number.
"""


def tag_strlen(*args) -> "ssize_t":
    r"""


    Calculate length of a colored string This function computes the length
    in unicode codepoints of a line
    
    tag_strlen(line) -> ssize_t
        @param line (C++: const char *)
        @return: the number of codepoints in the line, or -1 on error
    """
    return _ida_lines.tag_strlen(*args)

def calc_prefix_color(*args) -> "color_t":
    r"""


    Get prefix color for line at 'ea'
    
    calc_prefix_color(ea) -> color_t
        @param ea (C++: ea_t)
        @return: Line prefix colors
    """
    return _ida_lines.calc_prefix_color(*args)

def calc_bg_color(*args) -> "bgcolor_t":
    r"""


    Get background color for line at 'ea'
    
    calc_bg_color(ea) -> bgcolor_t
        @param ea (C++: ea_t)
        @return: RGB color
    """
    return _ida_lines.calc_bg_color(*args)

def add_sourcefile(*args) -> "bool":
    r"""


    Mark a range of address as belonging to a source file. An address
    range may belong only to one source file. A source file may be
    represented by several address ranges.
    
    add_sourcefile(ea1, ea2, filename) -> bool
        @param ea1: linear address of start of the address range (C++: ea_t)
        @param ea2: linear address of end of the address range (excluded)
                    (C++: ea_t)
        @param filename: name of source file. (C++: const char *)
        @return: success
    """
    return _ida_lines.add_sourcefile(*args)

def get_sourcefile(*args) -> "char const *":
    r"""


    Get name of source file occupying the given address.
    
    get_sourcefile(ea, bounds=None) -> char const *
        @param ea: linear address (C++: ea_t)
        @param bounds: pointer to the output buffer with the address range for
                       the current file. May be NULL. (C++: range_t  *)
        @return: NULL if source file information is not found, otherwise
                 returns pointer to file name
    """
    return _ida_lines.get_sourcefile(*args)

def del_sourcefile(*args) -> "bool":
    r"""


    Delete information about the source file.
    
    del_sourcefile(ea) -> bool
        @param ea: linear address (C++: ea_t)
        @return: success
    """
    return _ida_lines.del_sourcefile(*args)

def install_user_defined_prefix(*args) -> "bool":
    r"""


    User-defined line-prefixes are displayed just after the autogenerated
    line prefixes in the disassembly listing. There is no need to call
    this function explicitly. Use the 'user_defined_prefix_t' class.
    
    install_user_defined_prefix(prefix_len, udp, owner) -> bool
        @param prefix_len: prefixed length. if 0, then uninstall UDP (C++:
                           size_t)
        @param udp: object to generate user-defined prefix (C++: struct
                    user_defined_prefix_t  *)
        @param owner: pointer to the  plugin_t  that owns UDP if non-NULL,
                      then the object will be uninstalled and destroyed when
                      the plugin gets unloaded (C++: const void *)
    """
    return _ida_lines.install_user_defined_prefix(*args)
class user_defined_prefix_t(object):
    r"""
    Proxy of C++ user_defined_prefix_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""


        __init__(self, prefix_len, owner) -> user_defined_prefix_t
            prefix_len: size_t
            owner: void const *
        """
        if self.__class__ == user_defined_prefix_t:
            _self = None
        else:
            _self = self
        _ida_lines.user_defined_prefix_t_swiginit(self, _ida_lines.new_user_defined_prefix_t(_self, *args))
    __swig_destroy__ = _ida_lines.delete_user_defined_prefix_t

    def get_user_defined_prefix(self, *args) -> "void":
        r"""


        This callback must be overridden by the derived class.
        
        get_user_defined_prefix(self, ea, insn, lnnum, indent, line)
            @param ea: the current address (C++: ea_t)
            @param insn: the current instruction. if the current item is not an
                         instruction, then insn.itype is zero.  - an
                         ida_ua.insn_t, or an address (C++: const insn_t &)
            @param lnnum (C++: int)
            @param indent: see explanations for gen_printf() (C++: int)
            @param line: the line to be generated. the line usually contains color
                         tags. this argument can be examined to decide whether to
                         generate the prefix. (C++: const char *)
        """
        return _ida_lines.user_defined_prefix_t_get_user_defined_prefix(self, *args)
    def __disown__(self):
        self.this.disown()
        _ida_lines.disown_user_defined_prefix_t(self)
        return weakref.proxy(self)

# Register user_defined_prefix_t in _ida_lines:
_ida_lines.user_defined_prefix_t_swigregister(user_defined_prefix_t)
cvar = _ida_lines.cvar
COLOR_DEFAULT = cvar.COLOR_DEFAULT
"""
Default.
"""
COLOR_REGCMT = cvar.COLOR_REGCMT
COLOR_RPTCMT = cvar.COLOR_RPTCMT
COLOR_AUTOCMT = cvar.COLOR_AUTOCMT
COLOR_INSN = cvar.COLOR_INSN
COLOR_DATNAME = cvar.COLOR_DATNAME
COLOR_DNAME = cvar.COLOR_DNAME
COLOR_DEMNAME = cvar.COLOR_DEMNAME
COLOR_SYMBOL = cvar.COLOR_SYMBOL
COLOR_CHAR = cvar.COLOR_CHAR
COLOR_STRING = cvar.COLOR_STRING
COLOR_NUMBER = cvar.COLOR_NUMBER
COLOR_VOIDOP = cvar.COLOR_VOIDOP
COLOR_CREF = cvar.COLOR_CREF
COLOR_DREF = cvar.COLOR_DREF
COLOR_CREFTAIL = cvar.COLOR_CREFTAIL
COLOR_DREFTAIL = cvar.COLOR_DREFTAIL
COLOR_ERROR = cvar.COLOR_ERROR
COLOR_PREFIX = cvar.COLOR_PREFIX
COLOR_BINPREF = cvar.COLOR_BINPREF
COLOR_EXTRA = cvar.COLOR_EXTRA
COLOR_ALTOP = cvar.COLOR_ALTOP
COLOR_HIDNAME = cvar.COLOR_HIDNAME
COLOR_LIBNAME = cvar.COLOR_LIBNAME
COLOR_LOCNAME = cvar.COLOR_LOCNAME
COLOR_CODNAME = cvar.COLOR_CODNAME
COLOR_ASMDIR = cvar.COLOR_ASMDIR
COLOR_MACRO = cvar.COLOR_MACRO
COLOR_DSTR = cvar.COLOR_DSTR
COLOR_DCHAR = cvar.COLOR_DCHAR
COLOR_DNUM = cvar.COLOR_DNUM
COLOR_KEYWORD = cvar.COLOR_KEYWORD
COLOR_REG = cvar.COLOR_REG
COLOR_IMPNAME = cvar.COLOR_IMPNAME
COLOR_SEGNAME = cvar.COLOR_SEGNAME
COLOR_UNKNAME = cvar.COLOR_UNKNAME
COLOR_CNAME = cvar.COLOR_CNAME
COLOR_UNAME = cvar.COLOR_UNAME
COLOR_COLLAPSED = cvar.COLOR_COLLAPSED
COLOR_FG_MAX = cvar.COLOR_FG_MAX
COLOR_ADDR = cvar.COLOR_ADDR
COLOR_OPND1 = cvar.COLOR_OPND1
COLOR_OPND2 = cvar.COLOR_OPND2
COLOR_OPND3 = cvar.COLOR_OPND3
COLOR_OPND4 = cvar.COLOR_OPND4
COLOR_OPND5 = cvar.COLOR_OPND5
COLOR_OPND6 = cvar.COLOR_OPND6
COLOR_OPND7 = cvar.COLOR_OPND7
COLOR_OPND8 = cvar.COLOR_OPND8
COLOR_RESERVED1 = cvar.COLOR_RESERVED1
COLOR_LUMINA = cvar.COLOR_LUMINA

VEL_POST = _ida_lines.VEL_POST

VEL_CMT = _ida_lines.VEL_CMT


def add_extra_line(*args) -> "bool":
    r"""


    Add anterior/posterior non-comment line(s).
    
    add_extra_line(ea, isprev, format) -> bool
        @param ea: linear address (C++: ea_t)
        @param isprev: do we add anterior lines? (0-no, posterior) (C++: bool)
        @param format: printf() style format string. may contain \n to denote
                       new lines. (C++: const char *)
        @return: true if success
    """
    return _ida_lines.add_extra_line(*args)

def add_extra_cmt(*args) -> "bool":
    r"""


    Add anterior/posterior comment line(s).
    
    add_extra_cmt(ea, isprev, format) -> bool
        @param ea: linear address (C++: ea_t)
        @param isprev: do we add anterior lines? (0-no, posterior) (C++: bool)
        @param format: printf() style format string. may contain \n to denote
                       new lines. The resulting string should not contain
                       comment characters (;), the kernel will add them
                       automatically. (C++: const char *)
        @return: true if success
    """
    return _ida_lines.add_extra_cmt(*args)

def add_pgm_cmt(*args) -> "bool":
    r"""


    Add anterior comment line(s) at the start of program.
    
    add_pgm_cmt(format) -> bool
        @param format: printf() style format string. may contain \n to denote
                       new lines. The resulting string should not contain
                       comment characters (;), the kernel will add them
                       automatically. (C++: const char *)
        @return: true if success
    """
    return _ida_lines.add_pgm_cmt(*args)

def generate_disasm_line(*args) -> "qstring *":
    r"""


    generate_disasm_line(ea, flags=0) -> str
        ea: ea_t
        flags: int
    """
    return _ida_lines.generate_disasm_line(*args)
GENDSM_FORCE_CODE = _ida_lines.GENDSM_FORCE_CODE

GENDSM_MULTI_LINE = _ida_lines.GENDSM_MULTI_LINE

GENDSM_REMOVE_TAGS = _ida_lines.GENDSM_REMOVE_TAGS


def get_first_free_extra_cmtidx(*args) -> "int":
    r"""


    get_first_free_extra_cmtidx(ea, start) -> int
        ea: ea_t
        start: int
    """
    return _ida_lines.get_first_free_extra_cmtidx(*args)

def update_extra_cmt(*args) -> "void":
    r"""


    update_extra_cmt(ea, what, str)
        ea: ea_t
        what: int
        str: char const *
    """
    return _ida_lines.update_extra_cmt(*args)

def del_extra_cmt(*args) -> "void":
    r"""


    del_extra_cmt(ea, what)
        ea: ea_t
        what: int
    """
    return _ida_lines.del_extra_cmt(*args)

def get_extra_cmt(*args) -> "int":
    r"""


    get_extra_cmt(ea, what) -> ssize_t
        ea: ea_t
        what: int
    """
    return _ida_lines.get_extra_cmt(*args)

def delete_extra_cmts(*args) -> "void":
    r"""


    delete_extra_cmts(ea, what)
        ea: ea_t
        what: int
    """
    return _ida_lines.delete_extra_cmts(*args)

def create_encoding_helper(*args) -> "encoder_t *":
    r"""


    create_encoding_helper(encidx=-1, nr=nr_once) -> encoder_t *
        encidx: int
        nr: enum encoder_t::notify_recerr_t
    """
    return _ida_lines.create_encoding_helper(*args)

def tag_remove(*args) -> "PyObject *":
    r"""


    Remove color escape sequences from a string.
    
    tag_remove(nonnul_instr) -> PyObject *
        nonnul_instr: char const *
        @return: length of resulting string, -1 if error
    """
    return _ida_lines.tag_remove(*args)

def set_user_defined_prefix(*args) -> "PyObject *":
    r"""


    set_user_defined_prefix(width, pycb) -> PyObject *
    Deprecated. Please use install_user_defined_prefix() instead
    """
    return _ida_lines.set_user_defined_prefix(*args)

def tag_addr(*args) -> "PyObject *":
    r"""


    Insert an address mark into a string.
    
    tag_addr(ea) -> PyObject *
        @param ea: address to include (C++: ea_t)
    """
    return _ida_lines.tag_addr(*args)

def tag_skipcode(*args) -> "int":
    r"""


    Skip one color code. This function should be used if you are
    interested in color codes and want to analyze all of them. Otherwise
    'tag_skipcodes()' function is better since it will skip all colors at
    once. This function will skip the current color code if there is one.
    If the current symbol is not a color code, it will return the input.
    
    tag_skipcode(line) -> int
        @param line (C++: const char *)
        @return: moved pointer
    """
    return _ida_lines.tag_skipcode(*args)

def tag_skipcodes(*args) -> "int":
    r"""


    Move the pointer past all color codes.
    
    tag_skipcodes(line) -> int
        @param line: can't be NULL (C++: const char *)
        @return: moved pointer, can't be NULL
    """
    return _ida_lines.tag_skipcodes(*args)

def tag_advance(*args) -> "int":
    r"""


    Move pointer to a 'line' to 'cnt' positions right. Take into account
    escape sequences.
    
    tag_advance(line, cnt) -> int
        @param line: pointer to string (C++: const char *)
        @param cnt: number of positions to move right (C++: int)
        @return: moved pointer
    """
    return _ida_lines.tag_advance(*args)

def generate_disassembly(*args) -> "PyObject *":
    r"""


    generate_disassembly(ea, max_lines, as_stack, notags) -> PyObject *
    Generate disassembly lines (many lines) and put them into a buffer
    
    @param ea: address to generate disassembly for
    @param max_lines: how many lines max to generate
    @param as_stack: Display undefined items as 2/4/8 bytes
    @return:
        - None on failure
        - tuple(most_important_line_number, tuple(lines)) : Returns a tuple containing
          the most important line number and a tuple of generated lines
    """
    return _ida_lines.generate_disassembly(*args)

#<pycode(py_lines)>
import _ida_idaapi
import _ida_lines

# ---------------- Color escape sequence defitions -------------------------
COLOR_ADDR_SIZE = 16 if _ida_idaapi.BADADDR == 0xFFFFFFFFFFFFFFFF else 8
"""
Size of a tagged address (see 'COLOR_ADDR' )
"""
SCOLOR_FG_MAX   = '\x28'             #  Max color number
cvar = _ida_lines.cvar
SCOLOR_OPND1    = chr(cvar.COLOR_ADDR+1)  #  Instruction operand 1
SCOLOR_OPND2    = chr(cvar.COLOR_ADDR+2)  #  Instruction operand 2
SCOLOR_OPND3    = chr(cvar.COLOR_ADDR+3)  #  Instruction operand 3
SCOLOR_OPND4    = chr(cvar.COLOR_ADDR+4)  #  Instruction operand 4
SCOLOR_OPND5    = chr(cvar.COLOR_ADDR+5)  #  Instruction operand 5
SCOLOR_OPND6    = chr(cvar.COLOR_ADDR+6)  #  Instruction operand 6
SCOLOR_UTF8     = chr(cvar.COLOR_ADDR+10) #  Following text is UTF-8 encoded

# ---------------- Line prefix colors --------------------------------------
PALETTE_SIZE   =  (cvar.COLOR_FG_MAX+_ida_lines.COLOR_BG_MAX)

def requires_color_esc(c):
    """


        Checks if the given character requires escaping
        @param c: character (string of one char)
        @return: Boolean
    """
    t = ord(c[0])
    return c >= COLOR_ON and c <= COLOR_INV

def COLSTR(str, tag):
    """


        Utility function to create a colored line
        @param str: The string
        @param tag: Color tag constant. One of SCOLOR_XXXX
    """
    return SCOLOR_ON + tag + str + SCOLOR_OFF + tag

#</pycode(py_lines)>


if _BC695:
    COLOR_UTF8=cvar.COLOR_ADDR+10 # old value of COLOR_UTF8; shouldn't trigger anything
    add_long_cmt=add_extra_cmt
    describe=add_extra_line



E_PREV = cvar.E_PREV
E_NEXT = cvar.E_NEXT
