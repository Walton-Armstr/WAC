import subprocess
from utils.colors import Colors
from utils.animations import draw_header, draw_footer, styled_input

def process_menu():
    while True:
        draw_header("PROCESS MONITOR")
        try:
            res = subprocess.check_output("tasklist /NH /FO CSV", shell=True).decode()
            lines = res.strip().split('\n')
            print(f"{Colors.YELLOW}{'NAME':<25} {'PID':<8} {'MEMORY'}")
            print(Colors.RED + "═" * 50)
            for line in lines[:20]:
                p = line.replace('"', '').split(',')
                if len(p) >= 5:
                    print(f"{Colors.WHITE}{p[0]:<25} {p[1]:<8} {p[4]}")
            print(Colors.DIM + "... truncated ...")
        except:
            print(f"{Colors.RED}Unable to fetch process list.")
        draw_footer()
        
        print(f"{Colors.YELLOW}Commands: killpid [PID], killname [NAME], run [PATH], back")
        cmd_input = styled_input("PROC> ").split()
        if not cmd_input: continue
        
        act = cmd_input[0].lower()
        if act == "back": break
        
        try:
            if act == "killpid":
                subprocess.run(f"taskkill /F /PID {cmd_input[1]}", shell=True, check=True)
                print(f"{Colors.GREEN}PID {cmd_input[1]} terminated.")
            elif act == "killname":
                subprocess.run(f"taskkill /F /IM {cmd_input[1]} /T", shell=True, check=True)
                print(f"{Colors.GREEN}Image {cmd_input[1]} terminated.")
            elif act == "run":
                path = " ".join(cmd_input[1:])
                subprocess.Popen(path, shell=True)
                print(f"{Colors.GREEN}Process spawned: {path}")
        except Exception as e:
            print(f"{Colors.RED}Process Error: {e}")
