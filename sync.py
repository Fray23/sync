import os
import shutil
import hashlib

def get_file_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def copy_files(source_dir, destination_dir, ignore_list):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        if item in ignore_list:
            continue

        if os.path.isfile(source_item):
            source_hash = get_file_hash(source_item)

            if os.path.exists(destination_item):
                destination_hash = get_file_hash(destination_item)
                if source_hash == destination_hash:
                    continue

            print('start copy', source_item, destination_item)
            shutil.copy2(source_item, destination_item)
        elif os.path.isdir(source_item):
            copy_files(source_item, destination_item, ignore_list)

ignore_list = [
    'env',
]

for source_folder, destination_folder  in [
    ('', ''),
]:
    copy_files(source_folder, destination_folder, ignore_list)
