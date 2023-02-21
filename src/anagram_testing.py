import unittest
import tempfile
import os
# ikke ferdig.
from anagram_class import Anagrams

class TestAnagrams(unittest.TestCase):
    def test_anagram_finder(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('listen\nsilent\nenlist\nbadword\nanotherword\nstale\n')
            filename = f.name
            
        expected_output = ['listen', 'stale', 'least','silent']
        finder = Anagrams(filename)
        finder.read_file()
        output = finder.get_anagrams()

        self.assertEqual(output, expected_output)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            finder = Anagrams('nonexistent_file.txt')
            finder.get_anagrams()

    def test_invalid_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('not a valid file')
            filename = f.name

        with self.assertRaises(ValueError):
            finder = Anagrams(filename)
            finder.get_anagrams()

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            filename = f.name

        finder = Anagrams(filename)
        output = finder.get_anagrams()

        self.assertEqual(output, [])

        os.unlink(filename)
