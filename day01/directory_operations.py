import os


def show_all_files():
    root = os.path.join('.', 'data')
    print(root)
    for directory, subdir_list, file_list in os.walk(root):
        print('Directory:', directory)
        for name in subdir_list:
            print('Subdirectory:', name)
            for name in file_list:
                print('File:', name)
    print()


if __name__ == '__main__':
    show_all_files()
