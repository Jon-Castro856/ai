import os

def get_files_info(working_directory, directory=None):
    abs_path = os.path.abspath(working_directory)
    path = os.path.join(abs_path, directory.strip('/'))

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    if '..' in path:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    dir_contents = os.listdir(path)
    try:
        string_list = ""
        for file in dir_contents:
            item = os.path.join(path, file)
            is_dir = False

            if os.path.isdir(item):
                is_dir = True

            file_size = os.path.getsize(item)
            string_list += f"{file}: file_size={file_size} bytes, is_dir={is_dir}\n"

    except Exception as e:
        return f"Error listing files: {e}"
    
    return string_list