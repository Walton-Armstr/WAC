import sys
import time
from utils.colors import Colors
from utils.animations import typewriter, glitch_text, clear_screen, loading_bar, styled_input, draw_header, draw_footer
from utils.translator import tr

WA_LOGO = r"""
              __          __
              \ \        /  /
               \ \  /\  /  /
                \ \/  \/  /
                 \  /\  /
                 / /  \ \
                / /____\ \
               /_/      \_\

           W A   C O R P O R A T I O N
"""

def show_disclaimer():
    clear_screen()
    # 1. Select Language First
    draw_header(tr.get("select_lang"))
    print(f"  [1] ENGLISH")
    print(f"  [2] УКРАЇНСЬКА")
    print(f"  [3] РУССКИЙ")
    print(f"  [4] DEUTSCH")
    draw_footer()
    
    lang_choice = styled_input(">> ")
    if lang_choice == "2": tr.set_lang("UA")
    elif lang_choice == "3": tr.set_lang("RU")
    elif lang_choice == "4": tr.set_lang("DE")
    else: tr.set_lang("EN")
    
    clear_screen()
    print(Colors.RED + WA_LOGO)
    glitch_text(tr.get("welcome"), iterations=10)
    time.sleep(0.3)
    
    print("\n" + Colors.BRIGHT_RED + "╔" + "═"*58 + "╗")
    print(Colors.BRIGHT_RED + "║" + Colors.YELLOW + tr.get("warning").center(58) + Colors.BRIGHT_RED + "║")
    print(Colors.BRIGHT_RED + "╚" + "═"*58 + "╝\n")
    
    typewriter(tr.get("disclaimer_1"), color=Colors.BRIGHT_RED)
    typewriter(tr.get("disclaimer_2"), color=Colors.YELLOW)
    typewriter(tr.get("disclaimer_3"), color=Colors.WHITE)
    print("\n")
    
    choice = styled_input(tr.get("accept") + ": ").upper()
    
    if choice == 'Y':
        loading_bar(duration=1.0, label="AUTHORIZING")
        return True
    else:
        sys.exit()
