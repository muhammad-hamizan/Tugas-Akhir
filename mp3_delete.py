import os
import sys

def delete_mp3_files_in_range(start_num, end_num, root_dir='.'):
    """
    Deletes MP3 files within a specific numerical range from all subdirectories.

    This function walks through all directories starting from the root_dir.
    It identifies files with a '.mp3' extension and a purely numeric name
    (e.g., '001002.mp3'). If the number falls within the specified range
    [start_num, end_num], the file is deleted.

    Args:
        start_num (int): The starting number of the range of files to delete.
        end_num (int): The ending number of the range of files to delete.
        root_dir (str): The directory to start the search from. Defaults to the
                        current directory.
    """
    print(f"Starting search in directory: {os.path.abspath(root_dir)}")
    print(f"Will delete .mp3 files from {start_num:06d}.mp3 to {end_num:06d}.mp3")
    print("-" * 30)

    # Walk through all directories and subdirectories
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check if the file is an MP3 file
            if filename.lower().endswith('.mp3'):
                # The name of the file without the .mp3 extension
                file_base_name = filename[:-4]

                # Check if the filename is purely numeric
                if file_base_name.isdigit():
                    try:
                        file_num = int(file_base_name)

                        # Check if the file number is within the specified range
                        if start_num <= file_num <= end_num:
                            file_path = os.path.join(dirpath, filename)
                            try:
                                # Attempt to delete the file
                                os.remove(file_path)
                                print(f"DELETED: {file_path}")
                            except OSError as e:
                                # Handle errors during file deletion (e.g., permissions)
                                print(f"ERROR: Could not delete {file_path}. Reason: {e}", file=sys.stderr)
                    except ValueError:
                        # This handles cases where the filename isn't a simple integer
                        # (e.g., 'my_song_01.mp3'), so we just ignore it.
                        pass # Not a numeric filename we are interested in.

    print("-" * 30)
    print("Script finished.")

if __name__ == '__main__':
    # --- Configuration ---
    # Set the range of file numbers to be deleted.
    # The script will target files like '001002.mp3', '001003.mp3', etc.
    START_NUMBER = 1002
    END_NUMBER = 77050

    # The directory to search. '.' means the current directory where the script is run.
    TARGET_DIRECTORY = '.'

    # --- Execution ---
    # This check ensures the script runs only when executed directly.
    delete_mp3_files_in_range(START_NUMBER, END_NUMBER, TARGET_DIRECTORY)

