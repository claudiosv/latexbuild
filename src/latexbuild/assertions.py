"""
Assert that arguments meet specific criteria

This module organizes functions that assert whether a criteria for
their arguments is met. All functions within this module raise
one or more errors on certain conditions not being bet. If the
assertion is met, the functions will return True
"""

import shutil
from inspect import isclass
from pathlib import Path


def has_file_extension(filepath, ext_required):
    """
    Assert that a filepath has the required file extension

    :param filepath: string filepath presumably containing a file extension
    :param ext_required: the expected file extension
        examples: ".pdf", ".html", ".tex"
    """
    ext = Path(filepath).suffix
    if ext != ext_required:
        msg_tmpl = "The extension for {}, which is {}, does not equal {}"
        msg_format = msg_tmpl.format(filepath, ext, ext_required)
        raise ValueError(msg_format)
    return True


def is_binary(system_binary_str):
    """
    Assert that a string represents a system binary

    Return true if a string represents a system binary
    Raise TypeError if the system_binary_str is not a string
    Raise ValueError if the system_binary_str is not a system binary

    :param system_binary_str: STR string representing a system binary
    """
    if not isinstance(system_binary_str, str):
        msg = f"{system_binary_str} must be of type STR"
        raise TypeError(msg)
    binary_str = shutil.which(system_binary_str)
    if not binary_str:
        msg = f"{system_binary_str} is not valid system binary"
        raise ValueError(msg)
    return True


def list_is_type(ls, t):
    """
    Assert that a list contains only elements of type t

    Return True if list contains elements of type t
    Raise TypeError if t is not a class
    Raise TypeError if ls is not a list
    Raise TypeError if ls contains non-t elements

    :param ls: LIST
    :param t: python class
    """
    if not isclass(t):
        msg = f"{t} is not a class"
        raise TypeError(msg)
    elif not isinstance(ls, list):
        msg = f"{ls} is not a list"
        raise TypeError(msg)
    else:
        ls_bad_types = [i for i in ls if not isinstance(i, t)]
        if len(ls_bad_types) > 0:
            msg = f"{ls_bad_types} are not {t}"
            raise TypeError(msg)
    return True
