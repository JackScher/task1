from abc import ABC
import csv


class Base(ABC):
    def read_file(self):
        with open(self.filename) as myfile:
            head = [next(myfile) for x in range(5)]
            print(''.join(head))

    def write_file(self):
        f = open(self.filename, self.mode)
        f.write(self.default)
        f.close()
        return "Written to 'txt' file."


class TxtFiles(Base):
    def __init__(self, mode, filename):
        self.mode = mode
        self.filename = filename
        self.default = 'Default lorem 0 lorem lorem lorem!!!\n' \
                         'Default lorem 1 lorem lorem lorem!!!\n' \
                         'Default lorem 2 lorem lorem lorem!!!\n' \
                         'Default lorem 3 lorem lorem lorem!!!\n' \
                         'Default lorem 4 lorem lorem lorem!!!\n' \
                         'Default lorem 5 lorem lorem lorem!!!\n' \
                         'Default lorem 6 lorem lorem lorem!!!\n'


class CsvFiles(Base):
    def __init__(self, mode, filename):
        self.mode = mode
        self.filename = filename
        self.default = 'Default lorem 3 lorem lorem lorem!!!\n' \
                         ' lorem 3 lorem lorem lorem!!!\n' \
                         ' lorem 3 lorem lorem \n' \
                         ' lorem 3 lorem \n' \
                         ' lorem 34 \n' \
                         ' lorem \n' \
                         '3'

    def write_file(self):
        with open(self.filename, self.mode) as file:
            writer = csv.writer(file)
            arr = []
            arr.append(self.default)
            writer.writerow(arr)
        return "Written to 'csv' file."
