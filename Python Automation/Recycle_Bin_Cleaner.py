import winshell
from win10toast import ToastNotifier

try:
    winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=False)
    # Create a ToastNotifier object
    toaster = ToastNotifier()

    # Display a sample notification
    toaster.show_toast("Recycle Bin Cleanup Message", "Python has cleaned out your recycle bin files.", duration=10)

except Exception as e:
    toaster = ToastNotifier()
    
    # Display a sample notification
    toaster.show_toast("Recycle Bin Cleanup Failed", "Python failed to clean out your recycle bin files", duration=10)


