import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
     name="get_file_content",
     description="Gets the content of a given file path from a specified working directory, listing part of the file depending on its size",
     parameters=types.Schema(
          type=types.Type.OBJECT,
          required=["file_path"],
          properties={
               "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="File path used to find the given file, relative to the working directory (default is the working directory itself)"
               )
          }
     )
)
def get_file_content(working_directory, file_path):
        try:
        # getting the absolute path for the working directory
            abs_working_dir = os.path.abspath(working_directory)
        # constructing the full path to the target directory
            target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        # checking to see if target directory falls within the absolute working directory
            valid_target_path = os.path.commonpath([abs_working_dir, target_path]) == abs_working_dir
            if not valid_target_path:
                return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
        # checking to see if the file path is valid
            if not os.path.isfile(target_path):
                return f"Error: File not found or is not a regular file:'{file_path}'"

        # reading the file up to max_chars characters and return the contents as a string
            with open(target_path, "r", encoding="utf-8") as f:
                file_content_string = f.read(10000)
                truncated = f.read(1) != ""

            if truncated:
                file_content_string += f"[...File '{target_path}' truncated at 10000 characters]"

            return file_content_string

        except Exception as e:
             return f"Error: {e}" 