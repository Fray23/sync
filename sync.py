import os
import shutil

def copy_files(source_dir, destination_dir, ignore_list):
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        if item in ignore_list:
            continue

        print('copy ', source_dir, destination_dir)

        if os.path.isfile(source_item):
            if not os.path.exists(destination_item):
                # Копируем файл, если он не существует в папке назначения
                shutil.copy2(source_item, destination_item)
        elif os.path.isdir(source_item):
            if not os.path.exists(destination_item):
                # Создаем директорию, если она не существует в папке назначения
                shutil.copytree(source_item, destination_item, symlinks=True, ignore=shutil.ignore_patterns(*ignore_list))

ignore_list = [
    'env', 
    'bet', 
    'venv', 
    'test_env'
]

for source_folder, destination_folder  in [
    # ('Desktop/a79', 'Desktop/a79'),
    # ('Desktop/qute', 'Desktop/qute'),
    # ('Desktop/work', 'Desktop/work')
    ('Documents', 'Documents')
]:
    copy_files('/home/fs/' + source_folder, '/run/media/fs/0bda989c-4a6b-4c9a-a4a2-93cf1100eaa8/' + destination_folder, ignore_list)
