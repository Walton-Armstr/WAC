import sys
import time
import random
import os
from utils.colors import Colors

def typewriter(text, speed=0.02, color=Colors.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Colors.RESET)

def glitch_text(text, iterations=8, speed=0.04):
    chars = "/\\X#%@&*"
    for _ in range(iterations):
        glitched = "".join(random.choice(chars) if random.random() < 0.2 else c for c in text)
        sys.stdout.write("\r" + Colors.BRIGHT_RED + glitched)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\r" + Colors.WHITE + text + "\n")

def loading_bar(duration=1.5, label="LOADING", width=30):
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        progress = min(elapsed / duration, 1.0)
        filled = int(width * progress)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(progress * 100)
        sys.stdout.write(f"\r{Colors.WHITE}{label}: [{Colors.RED}{bar}{Colors.WHITE}] {percent}%")
        sys.stdout.flush()
        if progress >= 1.0:
            print()
            break
        time.sleep(0.04)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_header(title):
    width = 80
    print(Colors.RED + "╔" + "═" * (width - 2) + "╗")
    print(Colors.RED + "║" + Colors.WHITE + title.center(width - 2) + Colors.RED + "║")
    print(Colors.RED + "╠" + "═" * (width - 2) + "╣")

def draw_footer():
    width = 80
    print(Colors.RED + "╚" + "═" * (width - 2) + "╝")

def styled_input(prompt):
    return input(f"{Colors.RED}[{Colors.WHITE}>{Colors.RED}]{Colors.WHITE} {prompt}").strip()
