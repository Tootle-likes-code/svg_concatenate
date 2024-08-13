import os
import shutil


test_directories = {
    "MergeSvgsTests": "wip\\test_output\\merge_svgs"
}


def delete_all_files_for_test(test_name):
    _delete_all_files_in_directory(test_directories[test_name])


def _delete_all_files_in_directory(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        try:
            # Check if it's a file and delete it
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
            # Check if it's a directory and delete it recursively
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted directory: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

