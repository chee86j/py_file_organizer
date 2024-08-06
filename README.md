# Python File Organizer

Welcome to the File Organizer — an efficient tool designed to automate the organization of your files. 
Utilizing Python this script sorts files into categorized folders based on their extensions, 
ensuring a neat and orderly directory structure.

Ideal for professionals, students, and anyone alike with a cluttered downloads folder, the File Organizer 
simplifies file management by automatically sorting documents, images, videos, and more into specific 
folders. No more manual sorting or losing track of important files!

## Key Features

1. **Automated File Sorting**: Automatically categorizes and moves files into relevant folders based on file type.
2. **Customizable Categories**: Easily modify the script to include additional file types and categories.
3. **Handles Miscellaneous Files**: Places unclassified files into an "Others" folder, ensuring no file is left unsorted.
4. **Effortless Setup**: Simple to set up and use, with minimal configuration required.

## Technologies & Libraries

1. `os` for interacting with the operating system.
2. `shutil` for high-level file operations like moving and copying files.
3. Python's `logging` module for error logging and debugging.

## Prerequisites

Before running the File Organizer, ensure you have the following installed:

1. **Python**: Ensure Python 3.x is installed on your system. [Download Python](https://www.python.org/downloads/).
2. Before running the script set the `base_path` variable to the directory you want to organize
   base_path = 'C:/Users/username/Downloads'  **Replace with your directory path**

## Running The Script

1. Navigate to your directory from your terminal or command line containing 'file_organizer.py' and execute the script:
   `python file_organizer.py` or `python3 file_organizer.py`
