import ctypes
import sys
import os
from utils.translator import tr

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def run_as_admin(lang_code):
    """
    Closes the current non-admin console and spawns a new elevated one.
    Passes lang_code so the user doesn't have to select it again.
    """
    if not is_admin():
        print(f"\n{tr.get('admin_req')}")
        # Command line args for the new process
        # argv[0] is the script path, argv[1] is lang, argv[2] is flag
        script = os.path.abspath(sys.argv[0])
        params = f'"{script}" {lang_code} elevated'
        
        try:
            # ShellExecute with 'runas' verb triggers UAC
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        except Exception as e:
            print(f"Elevation Error: {e}")
        
        # Kill the current non-admin process immediately
        sys.exit(0)
