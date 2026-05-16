import os
import shutil
import subprocess
import time
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, styled_input
from utils.translator import tr

def list_directory(path):
    draw_header(f"{path}")
    try:
        items = os.listdir(path)
        for item in items:
            full = os.path.join(path, item)
            if os.path.isdir(full):
                print(f"{Colors.CYAN}[DIR]  {item}")
            else:
                size = os.path.getsize(full)
                print(f"{Colors.WHITE}[FILE] {item} ({size} bytes)")
    except Exception as e:
        print(f"{Colors.RED}{tr.get('error')}: {e}")
    draw_footer()

def file_manager_menu():
    curr = os.getcwd()
    while True:
        list_directory(curr)
        print(f"{Colors.YELLOW}cd [path], del [name], force [name], prop [name], search [name], back")
        cmd_input = styled_input("FM> ").split(maxsplit=1)
        if not cmd_input: continue
        
        act = cmd_input[0].lower()
        if act == "back": break
        
        try:
            arg = cmd_input[1] if len(cmd_input) > 1 else ""
            full_path = os.path.abspath(os.path.join(curr, arg))
            
            if act == "cd":
                if os.path.isdir(full_path): curr = full_path
            elif act == "del":
                if styled_input(tr.get("confirm_yes")) == "YES":
                    if os.path.isdir(full_path): shutil.rmtree(full_path)
                    else: os.remove(full_path)
            elif act == "force":
                if styled_input(tr.get("confirm_destroy")) == "DESTROY":
                    subprocess.run(f'takeown /f "{full_path}" /r /d y', shell=True)
                    subprocess.run(f'icacls "{full_path}" /grant administrators:F /t', shell=True)
                    if os.path.isdir(full_path): shutil.rmtree(full_path)
                    else: os.remove(full_path)
            elif act == "prop":
                draw_header("PROPERTIES")
                st = os.stat(full_path)
                print(f"Path: {full_path}\nSize: {st.st_size}\nModified: {time.ctime(st.st_mtime)}")
                draw_footer(); input(tr.get("press_enter"))
            elif act == "search":
                term = styled_input("Term: ")
                for r, d, f in os.walk(curr):
                    for file in f:
                        if term.lower() in file.lower(): print(os.path.join(r, file))
                input(tr.get("press_enter"))
        except Exception as e: print(f"{Colors.RED}{e}")
