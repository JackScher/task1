from base import TxtFiles
from base import CsvFiles


class ServiceClass:
    def __init__(self, mode, filename):
        self.mode = mode
        self.filename = filename
        self.file_type = self.check_file_type()

    def check_file_type(self):
        try:
            arr = self.filename.split('.')
            file_type = arr[-1]
            return file_type
        except AttributeError:
            return False

    def logic(self):
        if self.file_type == 'txt':
            txt = TxtFiles(self.mode, self.filename)
            return self.read_write(txt)
        elif self.file_type == 'csv':
            csv = CsvFiles(self.mode, self.filename)
            return self.read_write(csv)
        else:
            print('Wrong type or file name')

    def read_write(self, obj):
        if self.mode == 'w':
            res = obj.write_file()
            return res
        if self.mode == 'r':
            obj.read_file()
