import os
import unittest

from latexbuild.utils import (
    list_filepathes_with_predicate,
    random_name_filepath,
    random_str_uuid,
    recursive_apply,
)

PATH_FILE = os.path.abspath(__file__)
PATH_TEST = os.path.dirname(PATH_FILE)


class TestRandomStrUuid(unittest.TestCase):
    """Test class for random_str_uuid"""

    def test_correct_length(self):
        l1, l2 = 4, 7
        val1, val2 = random_str_uuid(l1), random_str_uuid(l2)
        len1, len2 = len(val1), len(val2)
        assert l1 == len1
        assert l2 == len2

    def test_random(self):
        l = 7
        v1, v2 = random_str_uuid(l), random_str_uuid(l)
        assert v1 != v2

    def test_below_1(self):
        assert len(random_str_uuid(1)) == 1
        self.assertRaises(ValueError, random_str_uuid, 0)

    def test_above_32(self):
        assert len(random_str_uuid(32)) == 32
        self.assertRaises(ValueError, random_str_uuid, 33)


class TestRandomNameFilepath(unittest.TestCase):
    """Test class for random_name_filepath"""

    PATH = "/hello/world/test.txt"

    def test_correct_length(self):
        len_random = 5
        path_finish = random_name_filepath(self.PATH, len_random)
        assert len(self.PATH) + len_random == len(path_finish)

    def test_extension_still_there(self):
        path_finish = random_name_filepath(self.PATH, 7)
        ext_path_start = os.path.splitext(self.PATH)[-1]
        ext_path_finish = os.path.splitext(path_finish)[-1]
        assert ext_path_start == ext_path_finish

    def test_beginning_still_there(self):
        len_random = 5
        path_finish = random_name_filepath(self.PATH, len_random)
        beg_start = os.path.splitext(self.PATH)[0]
        beg_finish = os.path.splitext(path_finish)[0]
        beg_finish_same = beg_finish[:-len_random]
        assert beg_start == beg_finish_same

    def test_middle_is_random(self):
        len_random = 5
        path_1 = random_name_filepath(self.PATH, len_random)
        path_2 = random_name_filepath(self.PATH, len_random)
        beg_1 = os.path.splitext(path_1)[0][-len_random:]
        beg_2 = os.path.splitext(path_2)[0][-len_random:]
        assert beg_1 != beg_2


class TestListFilepathesWithPredicate(unittest.TestCase):
    """Test class for list_filepathes_with_predicate"""

    def test_this_file(self):
        most_of_this_file = PATH_FILE[:-2]
        files = list_filepathes_with_predicate(PATH_TEST, most_of_this_file)
        assert files == [PATH_FILE]

    def test_not_a_match(self):
        impossible_prefix = "no root therefore impossible"
        files = list_filepathes_with_predicate(PATH_TEST, impossible_prefix)
        assert files == []

    def test_invalid_directory(self):
        self.assertRaises(
            ValueError,
            list_filepathes_with_predicate,
            "notadirectory",
            "anything",
        )


class TestReadFile(unittest.TestCase):
    """Test class for read_file"""

    """This function is too simple to warrant testing at this time"""


class TestRecursiveApply(unittest.TestCase):
    """Test class for recursive_apply"""

    def test_nested_objects(self):
        inval = {
            "hello": {"man": "woman", "dog": "cat"},
            "world": "smartiepants",
            "brownie": [
                "flower",
                {"sugar": "bad"},
                "chocolate",
            ],
        }
        expected_outval = {
            "hello": {"man": "womanTEST", "dog": "catTEST"},
            "world": "smartiepantsTEST",
            "brownie": [
                "flowerTEST",
                {"sugar": "badTEST"},
                "chocolateTEST",
            ],
        }

        def func(s):
            return s + "TEST"

        actual_outval = recursive_apply(inval, lambda s: s + "TEST")
        assert actual_outval == expected_outval


if __name__ == "__main__":
    unittest.main()
