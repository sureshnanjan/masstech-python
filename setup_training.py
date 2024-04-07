import os;
import random;
# Make directory structure
directory_paths = 'food\\fruits, food\\fruits\\apples, food\\fruits\\oranges, food\\vegetables'.replace('\\','/').split(',')
def make_dirs(paths):
    for path in paths:
        os.makedirs(dir)

def populate_files(paths):
    for path in paths:
        file_num = random.randrange(1,10)
        if os.path.exists(path):
            for ctr in range(file_num):
                file = os.path.join(path,f'Data-{ctr}.txt')
                with open(file, 'w') as fp:
                    pass

if __name__=='__main__':
    populate_files(directory_paths)


