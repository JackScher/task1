import os


class Speaker:
    def __init__(self):
        self.res = []
        self.mode = {
            '1': 'r',
            '2': 'w',
        }

    def take_mode(self):
        print('Hello, chose a mode: 1-read, 2-write')
        choice = input()
        if choice in self.mode:
            return self.mode[choice]
        else:
            print('wrong num.')
            return self.take_mode()

    def filename_dialog_0(self):
        print('1-take list of files to input into one of it, 2-create a new one')
        choice = input()
        if choice == '1':
            files = self.get_all_files()
            if len(files) == 0:
                return self.filename_dialog_0()
            return self.chose_file(files)
        elif choice == '2':
            path = self.get_current_path()
            return path + self.create_new_file()
        else:
            print('wrong num.')
            return self.filename_dialog_0()

    def filename_dialog_1(self):
        files = self.get_all_files()
        if len(files) == 0:
            return self.dialog()
        return self.chose_file(files)

    def get_all_files(self):
        cur_path = self.get_current_path()
        files = os.listdir(cur_path)
        if len(files) != 0:
            print("There are:")
            for file in files:
                print(file)
            return files
        else:
            print('no files')
            return files

    def chose_file(self, arr):
        path = self.get_current_path()
        print('Chose file:')
        choice = input()
        if choice in arr:
            return path + choice

    def create_new_file(self):
        print("Input file name in format 'file_name.txt/csv'")
        res = input()
        return res

    def get_current_path(self):
        curr_dir = os.path.abspath(os.curdir)
        return curr_dir + '/files/'

    def check_dir(self):
        curr_path = self.get_current_path()
        return os.path.exists(curr_path)

    def create_dir(self):
        exist_dir = self.check_dir()
        curr_path = self.get_current_path()
        if not exist_dir:
            os.mkdir(curr_path)

    def dialog(self):
        self.create_dir()
        self.res = []
        self.res.append(self.take_mode())
        if self.res[0] == 'r':
            self.res.append(self.filename_dialog_1())
        elif self.res[0] == 'w':
            self.res.append(self.filename_dialog_0())
        return self.res
