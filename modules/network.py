import subprocess
import os
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, styled_input

def network_menu():
    while True:
        draw_header("NETWORK OPERATIONS")
        print(f"{Colors.WHITE}[1] Show IP Configuration")
        print(f"{Colors.WHITE}[2] Ping Host")
        print(f"{Colors.WHITE}[3] Flush DNS Cache")
        print(f"{Colors.WHITE}[4] Show WiFi Passwords")
        print(f"{Colors.WHITE}[5] Active Connections (Netstat)")
        print(f"{Colors.WHITE}[B] Back")
        draw_footer()
        
        choice = styled_input("NET> ").upper()
        if choice == "B": break
        
        try:
            if choice == "1":
                print(subprocess.check_output("ipconfig", shell=True).decode())
            elif choice == "2":
                host = styled_input("Target: ")
                os.system(f"ping {host}")
            elif choice == "3":
                subprocess.run("ipconfig /flushdns", shell=True)
                print(f"{Colors.GREEN}DNS Flush sequence complete.")
            elif choice == "4":
                draw_header("WIFI VAULT")
                data = subprocess.check_output("netsh wlan show profiles", shell=True).decode(errors="ignore")
                profs = [i.split(":")[1][1:-1] for i in data.split('\n') if "All User Profile" in i]
                for p in profs:
                    res = subprocess.check_output(f'netsh wlan show profile "{p}" key=clear', shell=True).decode(errors="ignore")
                    key = [b.split(":")[1][1:-1] for b in res.split('\n') if "Key Content" in b]
                    print(f"{Colors.CYAN}{p:<20} {Colors.WHITE}: {Colors.GREEN}{key[0] if key else 'OPEN/HIDDEN'}")
            elif choice == "5":
                print(subprocess.check_output("netstat -an", shell=True).decode()[:1500])
            input("\nPress ENTER to return...")
        except Exception as e:
            print(f"{Colors.RED}Network Operation Failed: {e}")
