import os


class Speaker:
    def __init__(self):
        self.res = []

    def take_mode(self):
        print("Hello, chose a mode: 1-read, 2-write")
        mode = input()
        if mode == '1':
            return 'r'
        elif mode == '2':
            return 'w'

    def filename_dialog_0(self):
        print('1-take list of files to input into one of it, 2-create a new one')
        choice = input()
        if choice == '1':
            files = self.get_all_files()
            return self.chose_file(files)
        elif choice == '2':
            return self.create_new_file()

    def filename_dialog_1(self):
        files = self.get_all_files()
        return self.chose_file(files)

    def get_all_files(self):
        files = os.listdir('/home/dev/new/files')
        print("There are:")
        for file in files:
            print(file)
        return files

    def chose_file(self, arr):
        print('Chose file:')
        choice = input()
        for file in arr:
            if file == choice:
                return file
        print('Wrong file name')

    def create_new_file(self):
        print("Input file name in format 'file_name.txt/csv'")
        res = input()
        return res

    def dialog(self):
        self.res.append(self.take_mode())
        if self.res[0] == 'r':
            self.res.append('files/' + self.filename_dialog_1())
        elif self.res[0] == 'w':
            self.res.append('files/' + self.filename_dialog_0())
        return self.res
