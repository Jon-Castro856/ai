import os

def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(abs_path, file_path.strip('/'))
    print(full_path)
    if file_path not in full_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    
    if not os.path.exists(full_path):
        f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(full_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
        
    except Exception as e:
        return f"Error listing file contents: {e}"
    
    if len(file_content_string) >= MAX_CHARS:
        return f"{file_content_string}\n[...File '{file_path}' truncated at 10000 characters]"

    else:
        return f"{file_content_string}"
