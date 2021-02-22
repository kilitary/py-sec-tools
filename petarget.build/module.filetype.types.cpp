/* Generated code for Python module 'filetype.types'
 * created by Nuitka version 0.6.12.1
 *
 * This code is in part copyright 2021 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module_filetype$types" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_filetype$types;
PyDictObject *moduledict_filetype$types;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[96];

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    loadConstantsBlob(&mod_consts[0], "filetype.types", 96);

    constants_created = true;
}

/* For multiprocessing, we want to be able to initialize the __main__ constants. */
#if (_NUITKA_PLUGIN_MULTIPROCESSING_ENABLED || _NUITKA_PLUGIN_TRACEBACK_ENCRYPTION_ENABLED) && 0
void createMainModuleConstants(void) {
    createModuleConstants();
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_filetype$types(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    checkConstantsBlob(&mod_consts[0], "filetype.types", 96);
}
#endif

// The module code objects.
static PyCodeObject *codeobj_9e6b72c830fca594c59c1b4266a609a9;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[94]); CHECK_OBJECT(module_filename_obj);
    codeobj_9e6b72c830fca594c59c1b4266a609a9 = MAKE_CODEOBJECT(module_filename_obj, 1, CO_NOFREE, mod_consts[95], NULL, NULL, 0, 0, 0);
}

// The module function declarations.


// The module function definitions.


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill

function_impl_code functable_filetype$types[] = {

    NULL
};

static char const *_reduce_compiled_function_argnames[] = {
    "func",
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:reduce_compiled_function", (char **)_reduce_compiled_function_argnames, &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    function_impl_code *current = functable_filetype$types;
    int offset = 0;

    while (*current != NULL) {
        if (*current == function->m_c_code) {
            break;
        }

        current += 1;
        offset += 1;
    }

    if (*current == NULL) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = PyTuple_New(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);

    PyObject *result = PyTuple_New(4);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
    PyTuple_SET_ITEM0(result, 3, function->m_doc != NULL ? function->m_doc : Py_None);

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS | METH_KEYWORDS, NULL};

static char const *_create_compiled_function_argnames[] = {
    "func",
    "code_object_desc",
    "defaults",
    "doc",
    NULL
};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *func;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *doc;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO:create_compiled_function", (char **)_create_compiled_function_argnames, &func, &code_object_desc, &defaults, &doc, NULL)) {
        return NULL;
    }

    int offset = PyLong_AsLong(func);

    if (offset == -1 && ERROR_OCCURRED()) {
        return NULL;
    }

    if (offset > sizeof(functable_filetype$types) || offset < 0) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Wrong offset for compiled function.");
        return NULL;
    }

    PyObject *filename = PyTuple_GET_ITEM(code_object_desc, 0);
    PyObject *function_name = PyTuple_GET_ITEM(code_object_desc, 1);
    PyObject *line = PyTuple_GET_ITEM(code_object_desc, 2);
    int line_int = PyLong_AsLong(line);
    assert(!ERROR_OCCURRED());

    PyObject *argnames = PyTuple_GET_ITEM(code_object_desc, 3);
    PyObject *arg_count = PyTuple_GET_ITEM(code_object_desc, 4);
    int arg_count_int = PyLong_AsLong(arg_count);
    assert(!ERROR_OCCURRED());
    PyObject *flags = PyTuple_GET_ITEM(code_object_desc, 5);
    int flags_int = PyLong_AsLong(flags);
    assert(!ERROR_OCCURRED());

    PyCodeObject *code_object = MAKE_CODEOBJECT(
        filename,
        line_int,
        flags_int,
        function_name,
        argnames,
        NULL, // freevars
        arg_count_int,
        0, // TODO: Missing kw_only_count
        0 // TODO: Missing pos_only_count
    );

    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        functable_filetype$types[offset],
        code_object->co_name,
#if PYTHON_VERSION >= 0x300
        NULL, // TODO: Not transferring qualname yet
#endif
        code_object,
        defaults,
#if PYTHON_VERSION >= 0x300
        NULL, // kwdefaults are done on the outside currently
        NULL, // TODO: Not transferring annotations
#endif
        module_filetype$types,
        doc,
        NULL,
        0
    );

    return (PyObject *)result;
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS | METH_KEYWORDS, NULL
};


#endif

// Actual name might be different when loaded as a package.
NUITKA_MAY_BE_UNUSED static char const *module_full_name = "filetype.types";

// Internal entry point for module code.
PyObject *modulecode_filetype$types(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *module_entry) {
    module_filetype$types = module;

#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 0x300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if (_init_done) {
#ifdef _NUITKA_TRACE
        PRINT_STRING("filetype.types: Skipping module init, already done.\n");
#endif

        return module_filetype$types;
    } else {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();

#if PYTHON_VERSION < 0x300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 0x270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
    PRINT_STRING("filetype.types: Calling setupMetaPathBasedLoader().\n");
#endif
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    PRINT_STRING("filetype.types: Calling createModuleConstants().\n");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    PRINT_STRING("filetype.types: Calling createModuleCodeObjects().\n");
#endif
    createModuleCodeObjects();

    // PRINT_STRING("in initfiletype$types\n");

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.

    moduledict_filetype$types = MODULE_DICT(module_filetype$types);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    {
        PyObject *function_tables = PyObject_GetAttrString((PyObject *)builtin_module, "compiled_function_tables");
        if (function_tables == NULL) {
            DROP_ERROR_OCCURRED();
            function_tables = PyDict_New();
        }
        PyObject_SetAttrString((PyObject *)builtin_module, "compiled_function_tables", function_tables);
        PyObject *funcs = PyTuple_New(2);
        PyTuple_SET_ITEM(funcs, 0, PyCFunction_New(&_method_def_reduce_compiled_function, NULL));
        PyTuple_SET_ITEM(funcs, 1, PyCFunction_New(&_method_def_create_compiled_function, NULL));
        PyDict_SetItemString(function_tables, module_full_name, funcs);
    }
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_filetype$types,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_filetype$types,
            (Nuitka_StringObject *)const_str_plain___package__,
            const_str_empty
        );
#elif 1
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_filetype$types,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_filetype$types,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_filetype$types,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_filetype$types);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

#if PYTHON_VERSION >= 0x300
    UPDATE_STRING_DICT0(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);
#endif

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_filetype$types);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_FrameObject *frame_9e6b72c830fca594c59c1b4266a609a9;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *tmp_dictset_value;
    PyObject *tmp_dictset_dict;
    PyObject *tmp_dictset_key;
    int tmp_res;
    bool tmp_result;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_2);
    }
    // Frame without reuse.
    frame_9e6b72c830fca594c59c1b4266a609a9 = MAKE_MODULE_FRAME(codeobj_9e6b72c830fca594c59c1b4266a609a9, module_filetype$types);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack(frame_9e6b72c830fca594c59c1b4266a609a9);
    assert(Py_REFCNT(frame_9e6b72c830fca594c59c1b4266a609a9) == 2);

    // Framed code:
    {
        PyObject *tmp_assign_source_3;
        PyObject *tmp_list_element_1;
        PyObject *tmp_called_name_1;
        PyObject *tmp_expression_name_1;
        PyObject *tmp_args_element_name_1;
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
        {
            PyObject *hard_module = PyImport_ImportModule("os");
            if (likely(hard_module != NULL)) {
                tmp_expression_name_1 = PyObject_GetAttr(hard_module, mod_consts[2]);
            } else {
                tmp_expression_name_1 = NULL;
            }
        }

        if (tmp_expression_name_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        tmp_called_name_1 = LOOKUP_ATTRIBUTE(tmp_expression_name_1, mod_consts[3]);
        if (tmp_called_name_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        tmp_args_element_name_1 = module_filename_obj;
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
        tmp_list_element_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_name_1, tmp_args_element_name_1);
        Py_DECREF(tmp_called_name_1);
        if (tmp_list_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_3 = PyList_New(3);
        {
            PyObject *tmp_called_name_2;
            PyObject *tmp_expression_name_2;
            PyObject *tmp_args_element_name_2;
            PyObject *tmp_called_instance_1;
            PyObject *tmp_args_element_name_3;
            PyObject *tmp_called_instance_2;
            PyList_SET_ITEM(tmp_assign_source_3, 0, tmp_list_element_1);
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
            {
                PyObject *hard_module = PyImport_ImportModule("os");
                if (likely(hard_module != NULL)) {
                    tmp_expression_name_2 = PyObject_GetAttr(hard_module, mod_consts[2]);
                } else {
                    tmp_expression_name_2 = NULL;
                }
            }

            if (tmp_expression_name_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 1;

                goto list_build_exception_1;
            }
            tmp_called_name_2 = LOOKUP_ATTRIBUTE(tmp_expression_name_2, mod_consts[4]);
            if (tmp_called_name_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 1;

                goto list_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
            {
                PyObject *hard_module = PyImport_ImportModule("os");
                if (likely(hard_module != NULL)) {
                    tmp_called_instance_1 = PyObject_GetAttr(hard_module, mod_consts[5]);
                } else {
                    tmp_called_instance_1 = NULL;
                }
            }

            if (tmp_called_instance_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_name_2);

                exception_lineno = 1;

                goto list_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
            tmp_args_element_name_2 = CALL_METHOD_WITH_ARGS2(
                tmp_called_instance_1,
                mod_consts[6],
                &PyTuple_GET_ITEM(mod_consts[7], 0)
            );

            if (tmp_args_element_name_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_name_2);

                exception_lineno = 1;

                goto list_build_exception_1;
            }
            tmp_args_element_name_3 = mod_consts[8];
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
            {
                PyObject *call_args[] = {tmp_args_element_name_2, tmp_args_element_name_3};
                tmp_list_element_1 = CALL_FUNCTION_WITH_ARGS2(tmp_called_name_2, call_args);
            }

            Py_DECREF(tmp_called_name_2);
            Py_DECREF(tmp_args_element_name_2);
            if (tmp_list_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 1;

                goto list_build_exception_1;
            }
            PyList_SET_ITEM(tmp_assign_source_3, 1, tmp_list_element_1);
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
            {
                PyObject *hard_module = PyImport_ImportModule("os");
                if (likely(hard_module != NULL)) {
                    tmp_called_instance_2 = PyObject_GetAttr(hard_module, mod_consts[5]);
                } else {
                    tmp_called_instance_2 = NULL;
                }
            }

            if (tmp_called_instance_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 1;

                goto list_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 1;
            tmp_list_element_1 = CALL_METHOD_WITH_ARGS2(
                tmp_called_instance_2,
                mod_consts[6],
                &PyTuple_GET_ITEM(mod_consts[9], 0)
            );

            if (tmp_list_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 1;

                goto list_build_exception_1;
            }
            PyList_SET_ITEM(tmp_assign_source_3, 2, tmp_list_element_1);
        }
        goto list_build_noexception_1;
        // Exception handling pass through code for list_build:
        list_build_exception_1:;
        Py_DECREF(tmp_assign_source_3);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_1:;
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[10], tmp_assign_source_3);
    }
    {
        PyObject *tmp_expression_name_3;
        PyObject *tmp_subscript_name_1;
        tmp_dictset_value = Nuitka_Loader_New(module_entry);
        tmp_dictset_dict = PySys_GetObject((char *)"path_importer_cache");
        if (tmp_dictset_dict == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        tmp_expression_name_3 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[10]);

        if (unlikely(tmp_expression_name_3 == NULL)) {
            tmp_expression_name_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
        }

        assert(!(tmp_expression_name_3 == NULL));
        tmp_subscript_name_1 = mod_consts[11];
        tmp_dictset_key = LOOKUP_SUBSCRIPT_CONST(tmp_expression_name_3, tmp_subscript_name_1, 0);
        if (tmp_dictset_key == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        tmp_res = PyDict_SetItem(tmp_dictset_dict, tmp_dictset_key, tmp_dictset_value);
        Py_DECREF(tmp_dictset_key);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_name_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_name_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[12]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[12]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_1, mod_consts[13], tmp_assattr_name_1);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_name_2;
        PyObject *tmp_assattr_target_2;
        tmp_assattr_name_2 = Py_True;
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[12]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[12]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_2, mod_consts[14], tmp_assattr_name_2);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_name_3;
        PyObject *tmp_assattr_target_3;
        tmp_assattr_name_3 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[10]);

        if (unlikely(tmp_assattr_name_3 == NULL)) {
            tmp_assattr_name_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
        }

        if (tmp_assattr_name_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        tmp_assattr_target_3 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[12]);

        if (unlikely(tmp_assattr_target_3 == NULL)) {
            tmp_assattr_target_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[12]);
        }

        assert(!(tmp_assattr_target_3 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_3, mod_consts[15], tmp_assattr_name_3);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = Py_None;
        UPDATE_STRING_DICT0(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[16], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_import_name_from_1;
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 3;
        tmp_import_name_from_1 = IMPORT_HARD___FUTURE__();
        assert(!(tmp_import_name_from_1 == NULL));
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_5 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_filetype$types,
                mod_consts[17],
                mod_consts[11]
            );
        } else {
            tmp_assign_source_5 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[17]);
        }

        if (tmp_assign_source_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 3;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[17], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_import_name_from_2;
        PyObject *tmp_name_name_1;
        PyObject *tmp_globals_arg_name_1;
        PyObject *tmp_locals_arg_name_1;
        PyObject *tmp_fromlist_name_1;
        PyObject *tmp_level_name_1;
        tmp_name_name_1 = mod_consts[18];
        tmp_globals_arg_name_1 = (PyObject *)moduledict_filetype$types;
        tmp_locals_arg_name_1 = Py_None;
        tmp_fromlist_name_1 = mod_consts[19];
        tmp_level_name_1 = mod_consts[20];
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 5;
        tmp_import_name_from_2 = IMPORT_MODULE5(tmp_name_name_1, tmp_globals_arg_name_1, tmp_locals_arg_name_1, tmp_fromlist_name_1, tmp_level_name_1);
        if (tmp_import_name_from_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 5;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_2)) {
            tmp_assign_source_6 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_2,
                (PyObject *)moduledict_filetype$types,
                mod_consts[21],
                mod_consts[20]
            );
        } else {
            tmp_assign_source_6 = IMPORT_NAME(tmp_import_name_from_2, mod_consts[21]);
        }

        Py_DECREF(tmp_import_name_from_2);
        if (tmp_assign_source_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 5;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_import_name_from_3;
        PyObject *tmp_name_name_2;
        PyObject *tmp_globals_arg_name_2;
        PyObject *tmp_locals_arg_name_2;
        PyObject *tmp_fromlist_name_2;
        PyObject *tmp_level_name_2;
        tmp_name_name_2 = mod_consts[18];
        tmp_globals_arg_name_2 = (PyObject *)moduledict_filetype$types;
        tmp_locals_arg_name_2 = Py_None;
        tmp_fromlist_name_2 = mod_consts[22];
        tmp_level_name_2 = mod_consts[20];
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 6;
        tmp_import_name_from_3 = IMPORT_MODULE5(tmp_name_name_2, tmp_globals_arg_name_2, tmp_locals_arg_name_2, tmp_fromlist_name_2, tmp_level_name_2);
        if (tmp_import_name_from_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_3)) {
            tmp_assign_source_7 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_3,
                (PyObject *)moduledict_filetype$types,
                mod_consts[23],
                mod_consts[20]
            );
        } else {
            tmp_assign_source_7 = IMPORT_NAME(tmp_import_name_from_3, mod_consts[23]);
        }

        Py_DECREF(tmp_import_name_from_3);
        if (tmp_assign_source_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23], tmp_assign_source_7);
    }
    {
        PyObject *tmp_assign_source_8;
        PyObject *tmp_import_name_from_4;
        PyObject *tmp_name_name_3;
        PyObject *tmp_globals_arg_name_3;
        PyObject *tmp_locals_arg_name_3;
        PyObject *tmp_fromlist_name_3;
        PyObject *tmp_level_name_3;
        tmp_name_name_3 = mod_consts[18];
        tmp_globals_arg_name_3 = (PyObject *)moduledict_filetype$types;
        tmp_locals_arg_name_3 = Py_None;
        tmp_fromlist_name_3 = mod_consts[24];
        tmp_level_name_3 = mod_consts[20];
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 7;
        tmp_import_name_from_4 = IMPORT_MODULE5(tmp_name_name_3, tmp_globals_arg_name_3, tmp_locals_arg_name_3, tmp_fromlist_name_3, tmp_level_name_3);
        if (tmp_import_name_from_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 7;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_4)) {
            tmp_assign_source_8 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_4,
                (PyObject *)moduledict_filetype$types,
                mod_consts[25],
                mod_consts[20]
            );
        } else {
            tmp_assign_source_8 = IMPORT_NAME(tmp_import_name_from_4, mod_consts[25]);
        }

        Py_DECREF(tmp_import_name_from_4);
        if (tmp_assign_source_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 7;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[25], tmp_assign_source_8);
    }
    {
        PyObject *tmp_assign_source_9;
        PyObject *tmp_import_name_from_5;
        PyObject *tmp_name_name_4;
        PyObject *tmp_globals_arg_name_4;
        PyObject *tmp_locals_arg_name_4;
        PyObject *tmp_fromlist_name_4;
        PyObject *tmp_level_name_4;
        tmp_name_name_4 = mod_consts[18];
        tmp_globals_arg_name_4 = (PyObject *)moduledict_filetype$types;
        tmp_locals_arg_name_4 = Py_None;
        tmp_fromlist_name_4 = mod_consts[26];
        tmp_level_name_4 = mod_consts[20];
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 8;
        tmp_import_name_from_5 = IMPORT_MODULE5(tmp_name_name_4, tmp_globals_arg_name_4, tmp_locals_arg_name_4, tmp_fromlist_name_4, tmp_level_name_4);
        if (tmp_import_name_from_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 8;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_5)) {
            tmp_assign_source_9 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_5,
                (PyObject *)moduledict_filetype$types,
                mod_consts[27],
                mod_consts[20]
            );
        } else {
            tmp_assign_source_9 = IMPORT_NAME(tmp_import_name_from_5, mod_consts[27]);
        }

        Py_DECREF(tmp_import_name_from_5);
        if (tmp_assign_source_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 8;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;
        PyObject *tmp_import_name_from_6;
        PyObject *tmp_name_name_5;
        PyObject *tmp_globals_arg_name_5;
        PyObject *tmp_locals_arg_name_5;
        PyObject *tmp_fromlist_name_5;
        PyObject *tmp_level_name_5;
        tmp_name_name_5 = mod_consts[18];
        tmp_globals_arg_name_5 = (PyObject *)moduledict_filetype$types;
        tmp_locals_arg_name_5 = Py_None;
        tmp_fromlist_name_5 = mod_consts[28];
        tmp_level_name_5 = mod_consts[20];
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 9;
        tmp_import_name_from_6 = IMPORT_MODULE5(tmp_name_name_5, tmp_globals_arg_name_5, tmp_locals_arg_name_5, tmp_fromlist_name_5, tmp_level_name_5);
        if (tmp_import_name_from_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 9;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_6)) {
            tmp_assign_source_10 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_6,
                (PyObject *)moduledict_filetype$types,
                mod_consts[29],
                mod_consts[20]
            );
        } else {
            tmp_assign_source_10 = IMPORT_NAME(tmp_import_name_from_6, mod_consts[29]);
        }

        Py_DECREF(tmp_import_name_from_6);
        if (tmp_assign_source_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 9;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;
        PyObject *tmp_import_name_from_7;
        PyObject *tmp_name_name_6;
        PyObject *tmp_globals_arg_name_6;
        PyObject *tmp_locals_arg_name_6;
        PyObject *tmp_fromlist_name_6;
        PyObject *tmp_level_name_6;
        tmp_name_name_6 = mod_consts[30];
        tmp_globals_arg_name_6 = (PyObject *)moduledict_filetype$types;
        tmp_locals_arg_name_6 = Py_None;
        tmp_fromlist_name_6 = mod_consts[31];
        tmp_level_name_6 = mod_consts[20];
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 10;
        tmp_import_name_from_7 = IMPORT_MODULE5(tmp_name_name_6, tmp_globals_arg_name_6, tmp_locals_arg_name_6, tmp_fromlist_name_6, tmp_level_name_6);
        if (tmp_import_name_from_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 10;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_7)) {
            tmp_assign_source_11 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_7,
                (PyObject *)moduledict_filetype$types,
                mod_consts[32],
                mod_consts[20]
            );
        } else {
            tmp_assign_source_11 = IMPORT_NAME(tmp_import_name_from_7, mod_consts[32]);
        }

        Py_DECREF(tmp_import_name_from_7);
        if (tmp_assign_source_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 10;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[32], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_called_instance_3;
        tmp_called_instance_3 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

        if (unlikely(tmp_called_instance_3 == NULL)) {
            tmp_called_instance_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
        }

        if (tmp_called_instance_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 14;

            goto frame_exception_exit_1;
        }
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 14;
        tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_3, mod_consts[33]);
        if (tmp_tuple_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 14;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_12 = PyTuple_New(13);
        {
            PyObject *tmp_called_instance_4;
            PyObject *tmp_called_instance_5;
            PyObject *tmp_called_instance_6;
            PyObject *tmp_called_instance_7;
            PyObject *tmp_called_instance_8;
            PyObject *tmp_called_instance_9;
            PyObject *tmp_called_instance_10;
            PyObject *tmp_called_instance_11;
            PyObject *tmp_called_instance_12;
            PyObject *tmp_called_instance_13;
            PyObject *tmp_called_instance_14;
            PyObject *tmp_called_instance_15;
            PyTuple_SET_ITEM(tmp_assign_source_12, 0, tmp_tuple_element_1);
            tmp_called_instance_4 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_4 == NULL)) {
                tmp_called_instance_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 15;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 15;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_4, mod_consts[34]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 15;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 1, tmp_tuple_element_1);
            tmp_called_instance_5 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_5 == NULL)) {
                tmp_called_instance_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 16;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 16;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_5, mod_consts[35]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 16;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 2, tmp_tuple_element_1);
            tmp_called_instance_6 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_6 == NULL)) {
                tmp_called_instance_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 17;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 17;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_6, mod_consts[36]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 17;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 3, tmp_tuple_element_1);
            tmp_called_instance_7 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_7 == NULL)) {
                tmp_called_instance_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 18;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 18;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_7, mod_consts[37]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 18;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 4, tmp_tuple_element_1);
            tmp_called_instance_8 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_8 == NULL)) {
                tmp_called_instance_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 19;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 19;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_8, mod_consts[38]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 19;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 5, tmp_tuple_element_1);
            tmp_called_instance_9 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_9 == NULL)) {
                tmp_called_instance_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 20;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 20;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_9, mod_consts[39]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 20;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 6, tmp_tuple_element_1);
            tmp_called_instance_10 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_10 == NULL)) {
                tmp_called_instance_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 21;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 21;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_10, mod_consts[40]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 21;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 7, tmp_tuple_element_1);
            tmp_called_instance_11 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_11 == NULL)) {
                tmp_called_instance_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_11 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 22;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 22;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_11, mod_consts[41]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 22;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 8, tmp_tuple_element_1);
            tmp_called_instance_12 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_12 == NULL)) {
                tmp_called_instance_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_12 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 23;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 23;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_12, mod_consts[42]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 23;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 9, tmp_tuple_element_1);
            tmp_called_instance_13 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_13 == NULL)) {
                tmp_called_instance_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_13 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 24;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 24;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_13, mod_consts[43]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 24;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 10, tmp_tuple_element_1);
            tmp_called_instance_14 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_14 == NULL)) {
                tmp_called_instance_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_14 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 25;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 25;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_14, mod_consts[44]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 25;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 11, tmp_tuple_element_1);
            tmp_called_instance_15 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_instance_15 == NULL)) {
                tmp_called_instance_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[27]);
            }

            if (tmp_called_instance_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 26;

                goto tuple_build_exception_1;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 26;
            tmp_tuple_element_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_15, mod_consts[45]);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 26;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_assign_source_12, 12, tmp_tuple_element_1);
        }
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_assign_source_12);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[46], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;
        PyObject *tmp_tuple_element_2;
        PyObject *tmp_called_instance_16;
        tmp_called_instance_16 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

        if (unlikely(tmp_called_instance_16 == NULL)) {
            tmp_called_instance_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
        }

        if (tmp_called_instance_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 31;

            goto frame_exception_exit_1;
        }
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 31;
        tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_16, mod_consts[47]);
        if (tmp_tuple_element_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 31;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_13 = PyTuple_New(9);
        {
            PyObject *tmp_called_instance_17;
            PyObject *tmp_called_instance_18;
            PyObject *tmp_called_instance_19;
            PyObject *tmp_called_instance_20;
            PyObject *tmp_called_instance_21;
            PyObject *tmp_called_instance_22;
            PyObject *tmp_called_instance_23;
            PyObject *tmp_called_instance_24;
            PyTuple_SET_ITEM(tmp_assign_source_13, 0, tmp_tuple_element_2);
            tmp_called_instance_17 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_17 == NULL)) {
                tmp_called_instance_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 32;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 32;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_17, mod_consts[48]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 32;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 1, tmp_tuple_element_2);
            tmp_called_instance_18 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_18 == NULL)) {
                tmp_called_instance_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_18 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 33;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 33;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_18, mod_consts[49]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 33;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 2, tmp_tuple_element_2);
            tmp_called_instance_19 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_19 == NULL)) {
                tmp_called_instance_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_19 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 34;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_19, mod_consts[50]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 3, tmp_tuple_element_2);
            tmp_called_instance_20 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_20 == NULL)) {
                tmp_called_instance_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_20 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 35;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 35;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_20, mod_consts[51]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 35;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 4, tmp_tuple_element_2);
            tmp_called_instance_21 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_21 == NULL)) {
                tmp_called_instance_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_21 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 36;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 36;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_21, mod_consts[52]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 36;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 5, tmp_tuple_element_2);
            tmp_called_instance_22 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_22 == NULL)) {
                tmp_called_instance_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_22 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 37;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 37;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_22, mod_consts[53]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 37;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 6, tmp_tuple_element_2);
            tmp_called_instance_23 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_23 == NULL)) {
                tmp_called_instance_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 38;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 38;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_23, mod_consts[54]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 38;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 7, tmp_tuple_element_2);
            tmp_called_instance_24 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_instance_24 == NULL)) {
                tmp_called_instance_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
            }

            if (tmp_called_instance_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 39;

                goto tuple_build_exception_2;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 39;
            tmp_tuple_element_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_24, mod_consts[55]);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 39;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_assign_source_13, 8, tmp_tuple_element_2);
        }
        goto tuple_build_noexception_2;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_2:;
        Py_DECREF(tmp_assign_source_13);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_2:;
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[56], tmp_assign_source_13);
    }
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_tuple_element_3;
        PyObject *tmp_called_instance_25;
        tmp_called_instance_25 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_called_instance_25 == NULL)) {
            tmp_called_instance_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
        }

        if (tmp_called_instance_25 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 44;

            goto frame_exception_exit_1;
        }
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 44;
        tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_25, mod_consts[57]);
        if (tmp_tuple_element_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 44;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_14 = PyTuple_New(7);
        {
            PyObject *tmp_called_instance_26;
            PyObject *tmp_called_instance_27;
            PyObject *tmp_called_instance_28;
            PyObject *tmp_called_instance_29;
            PyObject *tmp_called_instance_30;
            PyObject *tmp_called_instance_31;
            PyTuple_SET_ITEM(tmp_assign_source_14, 0, tmp_tuple_element_3);
            tmp_called_instance_26 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_instance_26 == NULL)) {
                tmp_called_instance_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
            }

            if (tmp_called_instance_26 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 45;

                goto tuple_build_exception_3;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 45;
            tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_26, mod_consts[58]);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 45;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_assign_source_14, 1, tmp_tuple_element_3);
            tmp_called_instance_27 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_instance_27 == NULL)) {
                tmp_called_instance_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
            }

            if (tmp_called_instance_27 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 46;

                goto tuple_build_exception_3;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 46;
            tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_27, mod_consts[59]);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 46;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_assign_source_14, 2, tmp_tuple_element_3);
            tmp_called_instance_28 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_instance_28 == NULL)) {
                tmp_called_instance_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
            }

            if (tmp_called_instance_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 47;

                goto tuple_build_exception_3;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 47;
            tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_28, mod_consts[60]);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 47;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_assign_source_14, 3, tmp_tuple_element_3);
            tmp_called_instance_29 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_instance_29 == NULL)) {
                tmp_called_instance_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
            }

            if (tmp_called_instance_29 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 48;

                goto tuple_build_exception_3;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 48;
            tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_29, mod_consts[61]);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 48;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_assign_source_14, 4, tmp_tuple_element_3);
            tmp_called_instance_30 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_instance_30 == NULL)) {
                tmp_called_instance_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
            }

            if (tmp_called_instance_30 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 49;

                goto tuple_build_exception_3;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 49;
            tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_30, mod_consts[62]);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 49;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_assign_source_14, 5, tmp_tuple_element_3);
            tmp_called_instance_31 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_instance_31 == NULL)) {
                tmp_called_instance_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[23]);
            }

            if (tmp_called_instance_31 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 50;

                goto tuple_build_exception_3;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 50;
            tmp_tuple_element_3 = CALL_METHOD_NO_ARGS(tmp_called_instance_31, mod_consts[63]);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 50;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_assign_source_14, 6, tmp_tuple_element_3);
        }
        goto tuple_build_noexception_3;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_3:;
        Py_DECREF(tmp_assign_source_14);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_3:;
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[64], tmp_assign_source_14);
    }
    {
        PyObject *tmp_assign_source_15;
        PyObject *tmp_tuple_element_4;
        PyObject *tmp_called_instance_32;
        tmp_called_instance_32 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[25]);

        if (unlikely(tmp_called_instance_32 == NULL)) {
            tmp_called_instance_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[25]);
        }

        if (tmp_called_instance_32 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;

            goto frame_exception_exit_1;
        }
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 54;
        tmp_tuple_element_4 = CALL_METHOD_NO_ARGS(tmp_called_instance_32, mod_consts[65]);
        if (tmp_tuple_element_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_15 = PyTuple_New(4);
        {
            PyObject *tmp_called_instance_33;
            PyObject *tmp_called_instance_34;
            PyObject *tmp_called_instance_35;
            PyTuple_SET_ITEM(tmp_assign_source_15, 0, tmp_tuple_element_4);
            tmp_called_instance_33 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[25]);

            if (unlikely(tmp_called_instance_33 == NULL)) {
                tmp_called_instance_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[25]);
            }

            if (tmp_called_instance_33 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto tuple_build_exception_4;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 54;
            tmp_tuple_element_4 = CALL_METHOD_NO_ARGS(tmp_called_instance_33, mod_consts[66]);
            if (tmp_tuple_element_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto tuple_build_exception_4;
            }
            PyTuple_SET_ITEM(tmp_assign_source_15, 1, tmp_tuple_element_4);
            tmp_called_instance_34 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[25]);

            if (unlikely(tmp_called_instance_34 == NULL)) {
                tmp_called_instance_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[25]);
            }

            if (tmp_called_instance_34 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto tuple_build_exception_4;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 54;
            tmp_tuple_element_4 = CALL_METHOD_NO_ARGS(tmp_called_instance_34, mod_consts[67]);
            if (tmp_tuple_element_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto tuple_build_exception_4;
            }
            PyTuple_SET_ITEM(tmp_assign_source_15, 2, tmp_tuple_element_4);
            tmp_called_instance_35 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[25]);

            if (unlikely(tmp_called_instance_35 == NULL)) {
                tmp_called_instance_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[25]);
            }

            if (tmp_called_instance_35 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto tuple_build_exception_4;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 54;
            tmp_tuple_element_4 = CALL_METHOD_NO_ARGS(tmp_called_instance_35, mod_consts[68]);
            if (tmp_tuple_element_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;

                goto tuple_build_exception_4;
            }
            PyTuple_SET_ITEM(tmp_assign_source_15, 3, tmp_tuple_element_4);
        }
        goto tuple_build_noexception_4;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_4:;
        Py_DECREF(tmp_assign_source_15);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_4:;
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[69], tmp_assign_source_15);
    }
    {
        PyObject *tmp_assign_source_16;
        PyObject *tmp_tuple_element_5;
        PyObject *tmp_called_instance_36;
        tmp_called_instance_36 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_instance_36 == NULL)) {
            tmp_called_instance_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
        }

        if (tmp_called_instance_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 58;

            goto frame_exception_exit_1;
        }
        frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 58;
        tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_36, mod_consts[70]);
        if (tmp_tuple_element_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 58;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_16 = PyTuple_New(22);
        {
            PyObject *tmp_called_instance_37;
            PyObject *tmp_called_instance_38;
            PyObject *tmp_called_instance_39;
            PyObject *tmp_called_instance_40;
            PyObject *tmp_called_instance_41;
            PyObject *tmp_called_instance_42;
            PyObject *tmp_called_instance_43;
            PyObject *tmp_called_instance_44;
            PyObject *tmp_called_instance_45;
            PyObject *tmp_called_instance_46;
            PyObject *tmp_called_instance_47;
            PyObject *tmp_called_instance_48;
            PyObject *tmp_called_instance_49;
            PyObject *tmp_called_instance_50;
            PyObject *tmp_called_instance_51;
            PyObject *tmp_called_instance_52;
            PyObject *tmp_called_instance_53;
            PyObject *tmp_called_instance_54;
            PyObject *tmp_called_instance_55;
            PyObject *tmp_called_instance_56;
            PyObject *tmp_called_instance_57;
            PyTuple_SET_ITEM(tmp_assign_source_16, 0, tmp_tuple_element_5);
            tmp_called_instance_37 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_37 == NULL)) {
                tmp_called_instance_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_37 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 59;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 59;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_37, mod_consts[71]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 59;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 1, tmp_tuple_element_5);
            tmp_called_instance_38 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_38 == NULL)) {
                tmp_called_instance_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_38 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 60;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 60;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_38, mod_consts[72]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 60;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 2, tmp_tuple_element_5);
            tmp_called_instance_39 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_39 == NULL)) {
                tmp_called_instance_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_39 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 61;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 61;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_39, mod_consts[73]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 61;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 3, tmp_tuple_element_5);
            tmp_called_instance_40 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_40 == NULL)) {
                tmp_called_instance_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_40 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 62;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 62;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_40, mod_consts[74]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 62;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 4, tmp_tuple_element_5);
            tmp_called_instance_41 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_41 == NULL)) {
                tmp_called_instance_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_41 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 63;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_41, mod_consts[75]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 5, tmp_tuple_element_5);
            tmp_called_instance_42 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_42 == NULL)) {
                tmp_called_instance_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_42 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 64;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 64;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_42, mod_consts[76]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 64;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 6, tmp_tuple_element_5);
            tmp_called_instance_43 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_43 == NULL)) {
                tmp_called_instance_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_43 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 65;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 65;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_43, mod_consts[77]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 65;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 7, tmp_tuple_element_5);
            tmp_called_instance_44 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_44 == NULL)) {
                tmp_called_instance_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_44 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 66;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 66;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_44, mod_consts[78]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 66;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 8, tmp_tuple_element_5);
            tmp_called_instance_45 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_45 == NULL)) {
                tmp_called_instance_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_45 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 67;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_45, mod_consts[79]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 9, tmp_tuple_element_5);
            tmp_called_instance_46 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_46 == NULL)) {
                tmp_called_instance_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_46 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 68;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 68;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_46, mod_consts[80]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 68;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 10, tmp_tuple_element_5);
            tmp_called_instance_47 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_47 == NULL)) {
                tmp_called_instance_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_47 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 69;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_47, mod_consts[81]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 11, tmp_tuple_element_5);
            tmp_called_instance_48 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_48 == NULL)) {
                tmp_called_instance_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_48 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 70;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 70;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_48, mod_consts[82]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 70;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 12, tmp_tuple_element_5);
            tmp_called_instance_49 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_49 == NULL)) {
                tmp_called_instance_49 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_49 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 71;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 71;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_49, mod_consts[83]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 71;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 13, tmp_tuple_element_5);
            tmp_called_instance_50 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_50 == NULL)) {
                tmp_called_instance_50 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_50 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 72;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_50, mod_consts[84]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 14, tmp_tuple_element_5);
            tmp_called_instance_51 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_51 == NULL)) {
                tmp_called_instance_51 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_51 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 73;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_51, mod_consts[85]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 15, tmp_tuple_element_5);
            tmp_called_instance_52 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_52 == NULL)) {
                tmp_called_instance_52 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_52 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 74;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 74;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_52, mod_consts[86]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 74;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 16, tmp_tuple_element_5);
            tmp_called_instance_53 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_53 == NULL)) {
                tmp_called_instance_53 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_53 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 75;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 75;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_53, mod_consts[87]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 75;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 17, tmp_tuple_element_5);
            tmp_called_instance_54 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_54 == NULL)) {
                tmp_called_instance_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_54 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 76;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 76;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_54, mod_consts[88]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 76;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 18, tmp_tuple_element_5);
            tmp_called_instance_55 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_55 == NULL)) {
                tmp_called_instance_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_55 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 77;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_55, mod_consts[89]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 19, tmp_tuple_element_5);
            tmp_called_instance_56 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_56 == NULL)) {
                tmp_called_instance_56 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_56 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 78;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 78;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_56, mod_consts[90]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 78;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 20, tmp_tuple_element_5);
            tmp_called_instance_57 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_instance_57 == NULL)) {
                tmp_called_instance_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
            }

            if (tmp_called_instance_57 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 79;

                goto tuple_build_exception_5;
            }
            frame_9e6b72c830fca594c59c1b4266a609a9->m_frame.f_lineno = 79;
            tmp_tuple_element_5 = CALL_METHOD_NO_ARGS(tmp_called_instance_57, mod_consts[91]);
            if (tmp_tuple_element_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 79;

                goto tuple_build_exception_5;
            }
            PyTuple_SET_ITEM(tmp_assign_source_16, 21, tmp_tuple_element_5);
        }
        goto tuple_build_noexception_5;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_5:;
        Py_DECREF(tmp_assign_source_16);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_5:;
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[92], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;
        PyObject *tmp_list_arg_1;
        PyObject *tmp_left_name_1;
        PyObject *tmp_left_name_2;
        PyObject *tmp_left_name_3;
        PyObject *tmp_left_name_4;
        PyObject *tmp_right_name_1;
        PyObject *tmp_right_name_2;
        PyObject *tmp_right_name_3;
        PyObject *tmp_right_name_4;
        tmp_left_name_4 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[56]);

        if (unlikely(tmp_left_name_4 == NULL)) {
            tmp_left_name_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[56]);
        }

        if (tmp_left_name_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_right_name_1 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[46]);

        if (unlikely(tmp_right_name_1 == NULL)) {
            tmp_right_name_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[46]);
        }

        if (tmp_right_name_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_left_name_3 = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_left_name_4, tmp_right_name_1);
        if (tmp_left_name_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_right_name_2 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[64]);

        if (unlikely(tmp_right_name_2 == NULL)) {
            tmp_right_name_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[64]);
        }

        if (tmp_right_name_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_left_name_3);

            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_left_name_2 = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_left_name_3, tmp_right_name_2);
        Py_DECREF(tmp_left_name_3);
        if (tmp_left_name_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_right_name_3 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[69]);

        if (unlikely(tmp_right_name_3 == NULL)) {
            tmp_right_name_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[69]);
        }

        if (tmp_right_name_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_left_name_2);

            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_left_name_1 = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_left_name_2, tmp_right_name_3);
        Py_DECREF(tmp_left_name_2);
        if (tmp_left_name_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_right_name_4 = GET_STRING_DICT_VALUE(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[92]);

        if (unlikely(tmp_right_name_4 == NULL)) {
            tmp_right_name_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[92]);
        }

        if (tmp_right_name_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_left_name_1);

            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_list_arg_1 = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_left_name_1, tmp_right_name_4);
        Py_DECREF(tmp_left_name_1);
        if (tmp_list_arg_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_17 = PySequence_List(tmp_list_arg_1);
        Py_DECREF(tmp_list_arg_1);
        if (tmp_assign_source_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_filetype$types, (Nuitka_StringObject *)mod_consts[93], tmp_assign_source_17);
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION(frame_9e6b72c830fca594c59c1b4266a609a9);
#endif
    popFrameStack();

    assertFrameObject(frame_9e6b72c830fca594c59c1b4266a609a9);

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_9e6b72c830fca594c59c1b4266a609a9);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_9e6b72c830fca594c59c1b4266a609a9, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_9e6b72c830fca594c59c1b4266a609a9->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_9e6b72c830fca594c59c1b4266a609a9, exception_lineno);
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;

    return module_filetype$types;
    module_exception_exit:
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}

