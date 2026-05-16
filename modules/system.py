import os
import subprocess
import platform
import ctypes
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, typewriter, styled_input

def get_sys_info():
    draw_header("SYSTEM DIAGNOSTICS")
    try:
        print(f"{Colors.YELLOW}OS ARCH: {Colors.WHITE}{platform.system()} {platform.release()} {platform.machine()}")
        print(f"{Colors.YELLOW}CPU PROC: {Colors.WHITE}{platform.processor()}")
        
        # Memory Info
        try:
            mem = subprocess.check_output("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value", shell=True).decode()
            for line in mem.split('\n'):
                if "=" in line:
                    key, val = line.split('=')
                    if "TotalVisibleMemorySize" in key:
                        print(f"{Colors.YELLOW}TOTAL RAM: {Colors.WHITE}{int(val.strip())//1024} MB")
                    if "FreePhysicalMemory" in key:
                        print(f"{Colors.YELLOW}FREE RAM: {Colors.WHITE}{int(val.strip())//1024} MB")
        except: pass
        
        # Uptime
        try:
            uptime = subprocess.check_output("net statistics workstation", shell=True).decode()
            for line in uptime.split('\n'):
                if "since" in line:
                    print(f"{Colors.YELLOW}UPTIME SINCE: {Colors.WHITE}{line.split('since')[1].strip()}")
        except: pass

    except Exception as e:
        print(f"{Colors.RED}Diagnostic Error: {e}")
    draw_footer()

def power_control(action):
    try:
        if action == "shutdown":
            if styled_input("Shutdown System? (type YES): ") == "YES":
                typewriter("Initiating shutdown...", color=Colors.RED)
                os.system("shutdown /s /t 10")
        elif action == "restart":
            if styled_input("Restart System? (type YES): ") == "YES":
                typewriter("Initiating restart...", color=Colors.RED)
                os.system("shutdown /r /t 10")
        elif action == "hibernate":
            os.system("shutdown /h")
        elif action == "cancel":
            os.system("shutdown /a")
            print(f"{Colors.GREEN}Abort command successful.")
        elif action == "lock":
            ctypes.windll.user32.LockWorkStation()
        elif action == "recycle":
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 7)
            print(f"{Colors.GREEN}Recycle bin cleared.")
        elif action == "display_off":
            ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
    except Exception as e:
        print(f"{Colors.RED}Power Sequence Error: {e}")
