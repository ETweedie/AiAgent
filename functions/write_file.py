import os

def write_file(working_directory, file_path, content):
    try:
    # getting the absolute path for the working directory
        abs_working_dir = os.path.abspath(working_directory)
    # constructing the full path to the target directory
        target_directory = os.path.normpath(os.path.join(abs_working_dir, file_path))
    # checking to see if target directory falls within the absolute working directory
        valid_target_dir = os.path.commonpath([abs_working_dir, target_directory]) == abs_working_dir
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    # checking to see if the file path is an existing directory
        if os.path.isdir(target_directory):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    # Making sure all parent directories of file path exist
        os.makedirs(os.path.dirname(target_directory), exist_ok=True)
    # Opening the file path in write mode and overwrite its contents with content variable
        with open(target_directory, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: {e}'