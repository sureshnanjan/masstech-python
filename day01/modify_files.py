import datetime
import os

root = os.path.join('.', 'data')
for directory, subdir_list, file_list in os.walk(root):
    print("Inside the loop")
    for name in file_list:
        print("found files")
        source_name = os.path.join(directory, name)
        timestamp = os.path.getmtime(source_name)
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')
        target_name = os.path.join(directory, f'{modified_date}_{name}')
        print(f'Renaming: {source_name} to: {target_name}')
        os.rename(source_name, target_name)