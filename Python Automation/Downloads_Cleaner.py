import os
from win10toast import ToastNotifier



try:
    # Get the Downloads folder
    downloads_folder = r"C:\Users\willh\Downloads"

    downloads = os.listdir(downloads_folder)

    # Loop through the items in the Downloads folder and delete them
    for file in downloads:
        file_path = os.path.join(downloads_folder, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete: {file_path}, Error: {e}")


    # Create a ToastNotifier object
    toaster = ToastNotifier()

    # Display a sample notification
    toaster.show_toast("Download Folder Cleanup Message", "Python has cleaned out your downloads.", duration=10)

except Exception as e:
    toaster = ToastNotifier()
    
    # Display a sample notification
    toaster.show_toast("Download Folder Cleanup Failed", "Python failed to clean out your download files", duration=10)