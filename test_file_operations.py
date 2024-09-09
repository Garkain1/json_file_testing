import unittest
import os
from file_operations import write_to_file, read_from_file
from test_data import test_data


def get_type_map(data):
    return {k: type(v) for k, v in data.items()}


def check_types(data, type_map):
    for key, expected_type in type_map.items():
        if key in data:
            assert isinstance(data[key], expected_type),\
                f"Expected type {expected_type} for key '{key}', got {type(data[key])}"


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file.json'
        self.test_data = test_data
        self.empty_data = {}

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_and_read_file(self):
        write_to_file(self.test_file, self.test_data)
        result = read_from_file(self.test_file)
        type_map = get_type_map(self.test_data)
        check_types(result, type_map)
        self.assertEqual(result, self.test_data)

    def test_write_and_read_empty_file(self):
        write_to_file(self.test_file, self.empty_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, {})

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent_file.json')

    def test_write_bad_data_into_file(self):
        bad_data = set([1, 2, 3])
        with self.assertRaises(TypeError):
            write_to_file(self.test_file, bad_data)


if __name__ == '__main__':
    unittest.main()
