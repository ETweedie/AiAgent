def get_files_info(working_directory, directory="."):
    # getting the absolute path for the working directory
    abs_working_dir = os.path.abspath(working_directory)
    # constructing the full path to the target directory
    target_directory = os.path.normpath(os.path.join(abs_working_dir, directory))
    # checking to see if target directory falls within the absolute working directory
    valid_target_dir = os.path.commonpath([abs_working_dir, target_directory]) == abs_working_dir
    if not valid_target_dir:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    # checking to see if the directory is valid
    if not os.path.isdir(directory):
        return f"Error: '{directory}' is not a directory"
