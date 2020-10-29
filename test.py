import unittest
from base import TxtFiles, CsvFiles
from services import ServiceClass
from speaker import Speaker


class TestBase(unittest.TestCase):
    def test_txt_write(self):
        new_txt = TxtFiles('w', 'files/file1.txt')
        expected_date = "Written to 'txt' file."
        self.assertEqual(expected_date, new_txt.write_file())

    def test_csv_write(self):
        new_txt = CsvFiles('w', 'files/file1.csv')
        expected_date = "Written to 'csv' file."
        self.assertEqual(expected_date, new_txt.write_file())


class TestService(unittest.TestCase):
    def test_check(self):
        expected_date = 'txt'
        service = ServiceClass('r', 'files/file1.txt')
        self.assertEqual(expected_date, service.filetype)

    def test_logic(self):
        expected_date = "Written to 'csv' file."
        sv = ServiceClass('w', 'files/file1.csv')
        self.assertEqual(expected_date, sv.logic())

    def test_read_write(self):
        expected_data = "Written to 'csv' file."
        service = ServiceClass('w', 'files/file1.csv')
        new_csv = CsvFiles('w', 'files/file1.csv')
        self.assertEqual(expected_data, service.read_write(new_csv))


class TestSpeaker(unittest.TestCase):
    def test_take_mode(self):
        expected_data = 'r'
        sp = Speaker()
        self.assertEqual(expected_data, sp.take_mode())

    def test_get_all_files(self):
        extpexted_data = ['file1.csv', 'file1.txt']
        sp = Speaker()
        self.assertEqual(extpexted_data, sp.get_all_files())

    def test_chose_file(self):
        expected_data = 'file1.txt'
        arr = ['file1.csv', 'file1.txt']
        sp = Speaker()
        self.assertEqual(expected_data, sp.chose_file(arr))

    def test_create_new_file(self):
        expected_data = 'test_file.txt'
        sp = Speaker()
        self.assertEqual(expected_data, sp.create_new_file())

    def test_filename_dialog_1(self):
        expected_data = 'file1.txt'
        sp = Speaker()
        self.assertEqual(expected_data, sp.filename_dialog_1())

    def test_filename_dialog_0(self):
        expected_data = 'file1.csv'
        sp = Speaker()
        self.assertEqual(expected_data, sp.filename_dialog_0())

    def test_dialog(self):
        expected_data = ['w', 'files/test_file.txt']
        sp = Speaker()
        self.assertEqual(expected_data, sp.dialog())
