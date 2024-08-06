import os
import shutil
# These libraries are used to work w/files and directories where
# os is used to work w/file and directory operations like renaming, deleting, etc.
# shutil is used for high-level file operations like moving, copying, etc.

# Dictionary to categorize files based on their extensions
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif, .tiff'],
    'Videos': ['.mp4', '.mkv', '.webm', '.flv', '.avi'],
    'Music': ['.mp3', '.wav', '.flac', '.ogg'],
    'Applications': ['.exe', '.dmg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.sh', '.bat', '.ps1']
}

# Function to create directories if they don't exist. 
def create_directories(base_path, categories):
    for category in categories.keys():
        path = os.path.join(base_path, category)
        if not os.path.exists(path):
            os.mkdirs(path)
# 'base_path' is the path where the files are located. 
# 'categories' is the dictionary of the file categories.
# The () loops through each cat & checks if the directory exists using 'os.path.exists()'.
# & if the directory doesn't exist, it creates it using 'os.mkdirs()'.
            
# Function to organize files - scans the directory, matches the file to categories, & moves them
def organize_files(base_path,):
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    shutil.move(item_path, os.path.join(base_path, category, item))
                    moved = True
                    break
            if not moved:
                other_path = os.path.join(base_path, 'Others')
                if not os.path.exists(other_path):
                    os.mkdir(other_path)
                shutil.move(item_path, os.path.join(other_path, item))

# Main function to run the file organizer
def main():
    base_path = 'C:/Users/username/Downloads' # Replace with your download directory
    create_directories(base_path, FILE_CATEGORIES)
    organize_files(base_path)
    
if __name__ == '__main__':
    main()