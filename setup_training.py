import os;
import random;

# Make directory structure
directory_paths = r'food\fruits, food\fruits\apples, food\fruits\oranges, food\vegetables'.split(',')


def make_dirs(paths):
    if not os.path.exists('data'):
        os.mkdir('data')
    for path in paths:
        os.makedirs(os.path.join("data", path.lstrip().rstrip()),exist_ok=True)


def populate_files(paths):
    for path in paths:
        path = os.path.join('data',path.lstrip().rstrip())
        file_num = random.randrange(1, 10)
        if os.path.exists(path):
            for ctr in range(file_num):
                file = os.path.join(path, f'Data-{ctr}.txt')
                with open(file, 'w') as fp:
                    pass


if __name__ == '__main__':
    make_dirs(directory_paths)
    populate_files(directory_paths)
