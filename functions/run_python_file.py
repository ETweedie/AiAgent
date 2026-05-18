import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
    # getting the absolute path for the working directory
        abs_working_dir = os.path.abspath(working_directory)
    # constructing the full path to the target directory
        target_directory = os.path.normpath(os.path.join(abs_working_dir, file_path))
    # checking to see if target directory falls within the absolute working directory
        valid_target_dir = os.path.commonpath([abs_working_dir, target_directory]) == abs_working_dir
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    # Verify that the file path exists and points to a regular file not a directory
        if not os.path.isfile(target_directory):
            return f'Error: "{file_path}" does not exist or is not a regular file'
    # Check that the file name ends with .py
        if not target_directory.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_directory]
        if args is not None:
            command.extend(args)

    # running the command with the subprocess run
        result = subprocess.run(command, capture_output=True, timeout=30.00, text=True, check=True)
        completed_string = 'Command output: '
        if result.returncode != 0:
            completed_string += f'Process exited with code {result.returncode}'
        elif result.stderr is None and result.stdout is None:
            completed_string += 'No output produced'
        completed_string += f'STDERR: {result.stderr} and STDOUT: {result.stdout}'
        return completed_string
    
    except Exception as e:
        return f'Error: {e}'
