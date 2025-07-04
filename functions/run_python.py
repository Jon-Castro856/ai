import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f"Error: {file_path} is not a python file."
    
    try:
        commands = ['python3', abs_file_path]
        if args:
            commands.extend(args)

        code = subprocess.run(commands ,capture_output=True, text=True, timeout=30, cwd=abs_working_dir)
    except Exception as e:
        return f"Error during execution: {e}"
    output = []
    if code.stdout:
        output.append(f"STDOUT: {code.stdout}")
    if code.stderr:
        output.append(f"STDERR: {code.stderr}")

    if code.returncode != 0:
        output.append(f"Process exited with code {code.returncode}")

    return "\n".join(output) if output else "No output produced"
