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
        # Command line args for the new process:
        # script run: python.exe "main.py" EN elevated
        # frozen run: WAC_System_Control.exe EN elevated
        if getattr(sys, "frozen", False):
            executable = sys.executable
            params = f'{lang_code} elevated'
        else:
            executable = sys.executable
            script = os.path.abspath(sys.argv[0])
            params = f'"{script}" {lang_code} elevated'
        
        try:
            # ShellExecute with 'runas' verb triggers UAC
            ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, params, None, 1)
        except Exception as e:
            print(f"Elevation Error: {e}")
        
        # Kill the current non-admin process immediately
        sys.exit(0)
