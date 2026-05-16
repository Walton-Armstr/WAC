import os
import subprocess
import ctypes
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, styled_input, clear_screen
from utils.translator import tr
from utils.native import native

def danger_zone_menu():
    clear_screen()
    draw_header(tr.get("danger"))
    print(f"{Colors.BRIGHT_RED}!!! {tr.get('warning')} !!!")
    if styled_input(tr.get("confirm_yes")) != "YES": return
    
    while True:
        draw_header(tr.get("danger"))
        print(f" [1] {Colors.BRIGHT_RED}INITIATE SYSTEM CRASH (NATIVE BSOD)")
        print(f" [2] DISABLE WINDOWS DEFENDER (HYBRID METHOD)")
        print(f" [3] FLUSH ALL EVENT LOGS")
        print(f" [B] {tr.get('back')}")
        draw_footer()
        
        c = styled_input("DANGER> ").upper()
        if c == "B": break
        
        if c == "1":
            print(f"\n{Colors.BRIGHT_RED}--- {tr.get('bsod_warn')} ---")
            # Step 1: Confirmation
            if styled_input(tr.get("confirm_yes")) == "YES":
                # Step 2: Immediate Execution
                if styled_input(tr.get("confirm_initiate")) == "INITIATE":
                    native.trigger_kernel_panic()
        
        elif c == "2":
            if styled_input(tr.get("confirm_yes")) == "YES":
                # Hybrid Method: PowerShell + Registry
                subprocess.run("powershell Set-MpPreference -DisableRealtimeMonitoring $true", shell=True)
                os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f >nul 2>&1')
                print(f"{Colors.GREEN}{tr.get('success')}")
        
        elif c == "3":
            if styled_input(tr.get("confirm_yes")) == "YES":
                os.system('for /F "tokens=*" %1 in (\'wevtutil.exe el\') DO wevtutil.exe cl "%1"')
                print(f"{Colors.GREEN}{tr.get('success')}")
        input(tr.get("press_enter"))
