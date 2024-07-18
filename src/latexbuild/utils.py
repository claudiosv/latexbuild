"""General utility functions that do not fit into another module"""

from pathlib import Path
import uuid


def random_str_uuid(string_length):
    """Returns a random string of length string_length"""
    if not isinstance(string_length, int) or not 1 <= string_length <= 32:
        msg = "string_length must be type int where 1 <= string_length <= 32"
        raise ValueError(msg)
    random = str(uuid.uuid4()).upper().replace("-", "")
    return random[0:string_length]


def random_name_filepath(path_full: Path, length_random=5):
    """
    Take a filepath, add randome characters to its basename,
    and return the new filepath

    :param filename: either a filename or filepath
    :param length_random: length of random string to be generated
    """
    random_str = random_str_uuid(length_random)
    return path_full.with_stem(f"{path_full.stem}{random_str}")


def list_filepathes_with_predicate(path_dir: Path, predicate: str) -> list[Path]:
    """
    List all filepathes in a directory that begin with predicate

    :param path_dir: the directory whose top-level contents you wish to list
    :param predicate: the predicate you want to test the directory's
        found files against
    """
    if not isinstance(path_dir, Path):
        msg = "path_dir must be a Path object"
        raise ValueError(msg)

    if not path_dir.is_dir():
        msg = f"{path_dir} is not a directory"
        raise ValueError(msg)

    return [ f for f in path_dir.glob(f"{predicate}*") if f.is_file() ]

def recursive_apply(inval, func):
    """
    Recursively apply a function to all levels of nested iterables

    :param inval: the object to run the function on
    :param func: the function that will be run on the inval
    """
    if isinstance(inval, dict):
        return {k: recursive_apply(v, func) for k, v in inval.items()}
    elif isinstance(inval, list):
        return [recursive_apply(v, func) for v in inval]
    else:
        return func(inval)
