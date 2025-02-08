import os

### FUNCTION DEFINITIONS ###
def return_directory_paths():
    """
    Function to return the directory paths for the folders where the files will live
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    statements_dir = os.path.join(parent_dir, "statements")
    text_statements_dir = os.path.join(parent_dir, "text_statements")

    return statements_dir, text_statements_dir

