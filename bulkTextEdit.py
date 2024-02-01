import os
# read files from folder and store in variables
file_list = os.listdir('icons')
dir = 'icons/'


def changeName(list):
    for i in list:
        # replace png with blank
        cleanup_name = i.replace('png', '')

        # store new name with . replaced with _img.png
        new_name = cleanup_name.replace('.', '_img.png')

        # creates file path using directory and file name
        old_path = os.path.join(dir, i)
        new_path = os.path.join(dir, new_name)

        os.rename(old_path, new_path)


changeName(file_list)
