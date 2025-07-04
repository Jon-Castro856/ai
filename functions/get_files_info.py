import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    dir_contents = os.listdir(target_dir)
    try:
        string_list = ""
        for file in dir_contents:
            item = os.path.join(target_dir, file)
            is_dir = False

            if os.path.isdir(item):
                is_dir = True

            file_size = os.path.getsize(item)
            string_list += f"{file}: file_size={file_size} bytes, is_dir={is_dir}\n"

    except Exception as e:
        return f"Error listing files: {e}"
    
    return string_list