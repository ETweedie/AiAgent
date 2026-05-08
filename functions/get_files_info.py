import os

def get_files_info(working_directory, directory="."):
    try:
    # getting the absolute path for the working directory
        abs_working_dir = os.path.abspath(working_directory)
    # constructing the full path to the target directory
        target_directory = os.path.normpath(os.path.join(abs_working_dir, directory))
    # checking to see if target directory falls within the absolute working directory
        valid_target_dir = os.path.commonpath([abs_working_dir, target_directory]) == abs_working_dir
        if not valid_target_dir:
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    # checking to see if the directory is valid
        if not os.path.isdir(target_directory):
            return f"Error: '{directory}' is not a directory"

    # iterating over the contents of the target directory
        target_items = os.listdir(target_directory)
        lines = []
        for item in target_items:
            target_check = os.path.join(target_directory, item)
            if os.path.isdir(target_check):
                dir_size = os.path.getsize(target_check)
                lines.append(f"- {item}: file_size={dir_size} bytes, is_dir=True")
            elif os.path.isfile(target_check):
                file_size = os.path.getsize(target_check)
                lines.append(f"- {item}: file_size={file_size} bytes, is_dir=False")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"
        