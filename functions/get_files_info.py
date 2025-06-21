import os
def get_files_info(working_directory, directory=None):
    if directory not in working_directory:
        print(f"Error, Cannot list '{directory}' as it is outside the permitted working directory")

    if not os.path.isdir(directory):
        print(f'Error: "{directory}" is not a directory')

    dir_contents = os.listdir(directory)
    string_list = []

    if directory is not ".":
        