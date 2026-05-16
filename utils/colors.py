import sys
import os

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False

class Colors:
    if HAS_COLORAMA:
        RED = Fore.RED
        BRIGHT_RED = Fore.LIGHTRED_EX
        WHITE = Fore.WHITE
        YELLOW = Fore.YELLOW
        GREEN = Fore.GREEN
        CYAN = Fore.CYAN
        MAGENTA = Fore.MAGENTA
        RESET = Style.RESET_ALL
        DIM = Style.DIM
    else:
        RED = "\033[31m"
        BRIGHT_RED = "\033[91m"
        WHITE = "\033[37m"
        YELLOW = "\033[33m"
        GREEN = "\033[32m"
        CYAN = "\033[36m"
        MAGENTA = "\033[35m"
        RESET = "\033[0m"
        DIM = "\033[2m"

class Boxes:
    TL, TR, BL, BR = "╔", "╗", "╚", "╝"
    H, V = "═", "║"
    ML, MR = "╠", "╣"
    MT, MB = "╦", "╩"
    C = "╬"
