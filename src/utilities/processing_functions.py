"""
Functions to process pdf statements into text. Text will be analyzed and recorded
"""
### IMPORTS ###
import os
import pymupdf
from utilities.date_functions import extract_date_from_string

# Update this one later
def generate_text_files(statements_dir, text_statements_dir): # firast child functions that runs
    """
    Generates the text files to be read into the process functions
    """
    print("List of files in statements directory:")
    print(os.listdir(statements_dir))

    for filename in os.listdir(statements_dir):
        print(f"- - - - - Processing {filename} - - - - - ")
        new_file_name = generate_file_name(filename)
        if not new_file_name:
            continue

        doc = pymupdf.open(os.path.join(statements_dir, filename))

        with open(os.path.join(text_statements_dir,new_file_name), "wb") as output:
            for page in doc:
                text = page.get_text().encode("utf8")
                output.write(text)
                output.write(bytes((12,)))

def generate_file_name(filename):
    """
    Function to generate the file name for the text file

    Args:
        filename (str): The name of the file to be processed
    
    Returns:
        str: The new file name for the text file
        Will return None if the file name cannot be generated
    """
    file_indicator_dict = {
        "bank_of_america":
            {
                "file_indicator": "eStmt",
                "date_format": "YYYY-MM-DD"
            },
    }

    for key, value in file_indicator_dict.items():
        if value["file_indicator"] in filename:
            date_obj = extract_date_from_string(filename, date_format = value["date_format"])
            file_type = key
            new_file_name = f"{file_type}_{date_obj}.txt"
            return new_file_name

    print(f"WARNING: {filename} does not match any file indicators.")
    return None
    