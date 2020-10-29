from base import TxtFiles
from base import CsvFiles


class ServiceClass:
    def __init__(self, mode, filename):
        self.mode = mode
        self.filename = filename
        self.filetype = self.check()

    def check(self):
        arr = self.filename.split('.')
        file_type = arr[-1]
        return file_type

    def logic(self):
        if self.filetype == 'txt':
            txt = TxtFiles(self.mode, self.filename)
            return self.read_write(txt)
        elif self.filetype == 'csv':
            csv = CsvFiles(self.mode, self.filename)
            return self.read_write(csv)
        else:
            print('Wrong type')

    def read_write(self, obj):
        if self.mode == 'w':
            res = obj.write_file()
            return res
        if self.mode == 'r':
            obj.read_file()
