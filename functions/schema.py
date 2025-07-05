from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read a file from the specified directory, constrained to the working directory. File will be truncated to a max of 10,000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to read files from, relative to the working directory. If not provided, read files in the working directory itself.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the code contained in a .py file, constrainted to the working directory. Optional arguments can be accepted ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to execute files from, relative to the working directory. If not provided, execute files in the working directory itself.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write text into a file, constrained to the working directory. Text will be overwritten if the file already exists",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to write files from, relative to the working directory. If not provided, write files in the working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents that will be written to the file."
            )
        },
    ),
)