import sys
import os
import subprocess
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, styled_input, clear_screen, typewriter
from utils.translator import tr
import modules.system as system
import modules.file_manager as file_manager
import modules.processes as processes
import modules.network as network
import modules.registry as registry
import modules.danger_zone as danger_zone

def cmd_executor():
    while True:
        draw_header(tr.get("cmd"))
        cmd = styled_input("CMD> ")
        if cmd.lower() == "back": break
        if styled_input(tr.get("confirm_yes")).upper() == "YES":
            try:
                res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                print(f"{Colors.GREEN}OUT: {res.stdout}\n{Colors.RED}ERR: {res.stderr}")
            except Exception as e: print(f"{Colors.RED}{e}")
        input(tr.get("press_enter"))

def main_menu():
    while True:
        clear_screen()
        draw_header(tr.get("welcome"))
        print(f" [1] {tr.get('fm'):<20} [2] {tr.get('sys'):<20}")
        print(f" [3] {tr.get('proc'):<20} [4] {tr.get('cmd'):<20}")
        print(f" [5] {tr.get('net'):<20} [6] {tr.get('reg'):<20}")
        print(f" [7] {Colors.BRIGHT_RED}{tr.get('danger'):<20} {Colors.WHITE}[E] {tr.get('exit')}")
        draw_footer()
        
        c = styled_input("SELECT: ").upper()
        if c == "1": file_manager.file_manager_menu()
        elif c == "2":
            while True:
                draw_header(tr.get("sys"))
                print(" 1.Info 2.Shut 3.Rest 4.Hib 5.Can 6.Lock 7.Disp 8.Recy B.Back")
                s = styled_input("SYS> ").upper()
                if s == "B": break
                elif s == "1": system.get_sys_info(); input(tr.get("press_enter"))
                elif s == "2": system.power_control("shutdown")
                elif s == "3": system.power_control("restart")
                elif s == "4": system.power_control("hibernate")
                elif s == "5": system.power_control("cancel")
                elif s == "6": system.power_control("lock")
                elif s == "7": system.power_control("display_off")
                elif s == "8": system.power_control("recycle")
        elif c == "3": processes.process_menu()
        elif c == "4": cmd_executor()
        elif c == "5": network.network_menu()
        elif c == "6": registry.registry_menu()
        elif c == "7": danger_zone.danger_zone_menu()
        elif c == "E": sys.exit()
