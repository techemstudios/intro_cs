import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jimi Hendrix' work?"""
        formatted_name = get_formatted_name('jimi', 'hendrix')
        self.assertEqual(formatted_name, 'Jimi Hendrix')

    def test_first_last_middle_name(self):
        """Do names like 'Marie Francis Curie' work?"""
        formatted_name = get_formatted_name('marie', 'curie', 'francis')
        self.assertEqual(formatted_name, 'Marie Francis Curie')

unittest.main()
