import winreg
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, styled_input

def registry_menu():
    while True:
        draw_header("REGISTRY ACCESS")
        print(f"{Colors.WHITE}[1] Read Value")
        print(f"{Colors.WHITE}[2] Write Value")
        print(f"{Colors.WHITE}[3] Delete Key")
        print(f"{Colors.WHITE}[B] Back")
        draw_footer()
        
        choice = styled_input("REG> ").upper()
        if choice == "B": break
        
        try:
            h_str = styled_input("HKEY (e.g., HKEY_CURRENT_USER): ")
            hkey = getattr(winreg, h_str)
            path = styled_input("Subkey Path: ")
            
            if choice == "1":
                name = styled_input("Value Name: ")
                with winreg.OpenKey(hkey, path) as k:
                    val, typ = winreg.QueryValueEx(k, name)
                    print(f"{Colors.GREEN}Data: {val} (Type: {typ})")
            elif choice == "2":
                name = styled_input("Value Name: ")
                val = styled_input("New Data: ")
                if styled_input("Confirm Registry Write? (type YES): ") == "YES":
                    with winreg.CreateKey(hkey, path) as k:
                        winreg.SetValueEx(k, name, 0, winreg.REG_SZ, val)
                        print(f"{Colors.GREEN}Registry entry updated.")
            elif choice == "3":
                if styled_input("PURGE REGISTRY KEY? (type DESTROY): ") == "DESTROY":
                    winreg.DeleteKey(hkey, path)
                    print(f"{Colors.GREEN}Key Deleted.")
            input("Press ENTER...")
        except Exception as e:
            print(f"{Colors.RED}Registry Access Error: {e}")
