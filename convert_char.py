import os
import shutil

def convert_filenames_to_lowercase(directory_path="./data"):
    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist!")
        return
    
    # Get all files in the directory
    files = os.listdir(directory_path)
    
    for filename in files:
        # Get full path of the file
        old_path = os.path.join(directory_path, filename)
        
        # Skip directories
        if os.path.isdir(old_path):
            continue
        
        # Convert filename to lowercase
        new_filename = filename.lower()
        
        # If the filename changed
        if new_filename != filename:
            new_path = os.path.join(directory_path, new_filename)
            
            # Rename the file
            try:
                shutil.move(old_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")
        else:
            print(f"Skipped: '{filename}' (already lowercase)")

if __name__ == "__main__":
    convert_filenames_to_lowercase()
    print("File conversion complete!")