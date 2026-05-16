import sys
import os
from admin_check import is_admin, run_as_admin
from disclaimer import show_disclaimer
from menu import main_menu
from utils.translator import tr
from utils.colors import Colors

def main():
    # 1. Setup Console Title
    if os.name == 'nt':
        os.system("title WA Corporation System Control Panel")

    # 2. Check Arguments for Elevated Session
    # sys.argv: [main.py, lang_code, "elevated"]
    if len(sys.argv) >= 3 and sys.argv[2] == "elevated":
        tr.set_lang(sys.argv[1])
    else:
        # Initial run in user mode: Disclaimer + Lang Choice
        if not show_disclaimer():
            sys.exit()
        
        # If not admin, elevate and restart
        if not is_admin():
            run_as_admin(tr.lang)

    # 3. If here, we are Admin. Enter main loop.
    try:
        main_menu()
    except Exception as e:
        print(f"\n{Colors.BRIGHT_RED}FATAL EXCEPTION: {e}")
        input(tr.get("press_enter"))

if __name__ == "__main__":
    main()
