import os
import shutil
import hashlib
import fnmatch

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

        if any(fnmatch.fnmatch(item, pattern) for pattern in ignore_list):
            continue

        if os.path.isfile(source_item):
            source_hash = get_file_hash(source_item)

            message = 'start copy'
            if os.path.exists(destination_item):
                destination_hash = get_file_hash(destination_item)
                if source_hash == destination_hash:
                    continue
                else:
                    message = 'start update'

            print(f'{message}', source_item, destination_item)
            shutil.copy2(source_item, destination_item)
        elif os.path.isdir(source_item):
            copy_files(source_item, destination_item, ignore_list)

ignore_list = [
    'env',
    'bet',
    'venv',
    'test_env',

    '.github',
    '.git',
    '.gitbook',
    '__pycache__/',
    '.idea',
    'media',
    'venv3.6',
    'logs',
    '*.log',
    '*.sock',
    '*.pyc',
]

for source_folder, destination_folder  in [
    # ('Desktop/a79', 'Desktop/a79'),
    # ('Desktop/work', 'Desktop/work'),
    ('Desktop', 'Desktop'),
    ('Documents', 'Documents'),
    ('files', 'files'),
    ('Music', 'Music'),
    ('Pictures', 'Pictures'),
    ('video', 'video')
]:
    # copy_files('/home/fs/' + source_folder, '/run/media/fs/0bda989c-4a6b-4c9a-a4a2-93cf1100eaa8/' + destination_folder, ignore_list)
    # copy_files('/run/media/fs/0bda989c-4a6b-4c9a-a4a2-93cf1100eaa8/' + source_folder, '/run/media/fs/Transcend/DISK/' + destination_folder, ignore_list)
