class Translator:
    LANGS = {
        "EN": {
            "welcome": "WA CORPORATION SYSTEM CONTROL PANEL",
            "warning": "!!! WARNING !!!",
            "disclaimer_1": "WA CORPORATION IS NOT RESPONSIBLE FOR YOUR ACTIONS.",
            "disclaimer_2": "SYSTEM MODIFICATIONS MAY CAUSE PERMANENT DATA LOSS.",
            "disclaimer_3": "ADMINISTRATIVE PRIVILEGES WILL BE REQUESTED.",
            "accept": "Accept and launch? [Y/N]",
            "admin_req": "Requesting UAC Elevation. This window will close...",
            "select_lang": "SELECT LANGUAGE / ОБЕРІТЬ МОВУ / ВЫБЕРИТЕ ЯЗЫК / SPRACHE WÄHLEN",
            "fm": "FILE MANAGER",
            "sys": "SYSTEM CONTROL",
            "proc": "PROCESS MANAGER",
            "cmd": "CMD EXECUTOR",
            "net": "NETWORK TOOLS",
            "reg": "REGISTRY EDITOR",
            "danger": "DANGER ZONE",
            "exit": "EXIT",
            "confirm_yes": "Type YES to confirm: ",
            "confirm_destroy": "Type DESTROY to confirm: ",
            "confirm_initiate": "Type INITIATE to execute: ",
            "back": "Back",
            "bsod_warn": "THIS WILL CRASH YOUR COMPUTER IMMEDIATELY.",
            "press_enter": "Press ENTER to continue...",
            "found": "FOUND",
            "error": "ERROR",
            "success": "SUCCESS"
        },
        "UA": {
            "welcome": "ПАНЕЛЬ КЕРУВАННЯ СИСТЕМОЮ WA CORPORATION",
            "warning": "!!! УВАГА !!!",
            "disclaimer_1": "WA CORPORATION НЕ НЕСЕ ВІДПОВІДАЛЬНОСТІ ЗА ВАШІ ДІЇ.",
            "disclaimer_2": "МОДИФІКАЦІЯ СИСТЕМИ МОЖЕ ПРИЗВЕСТИ ДО ВТРАТИ ДАНИХ.",
            "disclaimer_3": "БУДУТЬ ЗАПИТАНІ ПРАВА АДМІНІСТРАТОРА.",
            "accept": "Прийняти та запустити? [Y/N]",
            "admin_req": "Запит прав адміністратора. Це вікно буде закрито...",
            "select_lang": "ОБЕРІТЬ МОВУ",
            "fm": "ФАЙЛОВИЙ МЕНЕДЖЕР",
            "sys": "КЕРУВАННЯ СИСТЕМОЮ",
            "proc": "МЕНЕДЖЕР ПРОЦЕСІВ",
            "cmd": "КОМАНДНИЙ РЯДОК",
            "net": "МЕРЕЖЕВІ ІНСТРУМЕНТИ",
            "reg": "РЕДАКТОР РЕЄСТРУ",
            "danger": "ЗОНА НЕБЕЗПЕКИ",
            "exit": "ВИХІД",
            "confirm_yes": "Введіть YES для підтвердження: ",
            "confirm_destroy": "Введіть DESTROY для підтвердження: ",
            "confirm_initiate": "Введіть INITIATE для виконання: ",
            "back": "Назад",
            "bsod_warn": "ЦЕ НЕГАЙНО ВИКЛИЧЕ ЗБІЙ СИСТЕМИ (BSOD).",
            "press_enter": "Натисніть ENTER для продовження...",
            "found": "ЗНАЙДЕНО",
            "error": "ПОМИЛКА",
            "success": "УСПІШНО"
        },
        "RU": {
            "welcome": "ПАНЕЛЬ УПРАВЛЕНИЯ СИСТЕМОЙ WA CORPORATION",
            "warning": "!!! ВНИМАНИЕ !!!",
            "disclaimer_1": "WA CORPORATION НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ.",
            "disclaimer_2": "ИЗМЕНЕНИЯ СИСТЕМЫ МОГУТ ПРИВЕСТИ К ПОТЕРЕ ДАННЫХ.",
            "disclaimer_3": "БУДУТ ЗАПРОШЕНЫ ПРАВА АДМИНИСТРАТОРА.",
            "accept": "Принять и запустить? [Y/N]",
            "admin_req": "Запрос прав администратора. Это окно будет закрыто...",
            "select_lang": "ВЫБЕРИТЕ ЯЗЫК",
            "fm": "ФАЙЛОВЫЙ МЕНЕДЖЕР",
            "sys": "УПРАВЛЕНИЕ СИСТЕМОЙ",
            "proc": "МЕНЕДЖЕР ПРОЦЕССОВ",
            "cmd": "КОМАНДНЫЙ СТРОКА",
            "net": "СЕТЕВЫЕ ИНСТРУМЕНТЫ",
            "reg": "РЕДАКТОР РЕЕСТРА",
            "danger": "ЗОНА РИСКА",
            "exit": "ВЫХОД",
            "confirm_yes": "Введите YES для подтверждения: ",
            "confirm_destroy": "Введите DESTROY для подтверждения: ",
            "confirm_initiate": "Введите INITIATE для выполнения: ",
            "back": "Назад",
            "bsod_warn": "ЭТО НЕМЕДЛЕННО ВЫЗОВЕТ СБОЙ СИСТЕМЫ (BSOD).",
            "press_enter": "Нажмите ENTER для продолжения...",
            "found": "НАЙДЕНО",
            "error": "ОШИБКА",
            "success": "УСПЕШНО"
        },
        "DE": {
            "welcome": "WA CORPORATION SYSTEMSTEUERUNG",
            "warning": "!!! WARNUNG !!!",
            "disclaimer_1": "WA CORPORATION HAFTET NICHT FÜR IHRE HANDLUNGEN.",
            "disclaimer_2": "SYSTEMÄNDERUNGEN KÖNNEN ZU DATENVERLUST FÜHREN.",
            "disclaimer_3": "ADMINISTRATORRECHTE WERDEN ANGEFORDERT.",
            "accept": "Akzeptieren und starten? [Y/N]",
            "admin_req": "UAC-Erhöhung angefordert. Dieses Fenster wird geschlossen...",
            "select_lang": "SPRACHE WÄHLEN",
            "fm": "DATEI-MANAGER",
            "sys": "SYSTEMSTEUERUNG",
            "proc": "PROZESS-MANAGER",
            "cmd": "BEFEHLSAUSFÜHRUNG",
            "net": "NETZWERK-TOOLS",
            "reg": "REGISTRIERUNGS-EDITOR",
            "danger": "GEFAHRENZONE",
            "exit": "BEENDEN",
            "confirm_yes": "Geben Sie YES ein: ",
            "confirm_destroy": "Geben Sie DESTROY ein: ",
            "confirm_initiate": "Geben Sie INITIATE ein: ",
            "back": "Zurück",
            "bsod_warn": "DIES WIRD IHREN COMPUTER SOFORT ABSTÜRZEN LASSEN.",
            "press_enter": "Drücken Sie ENTER...",
            "found": "GEFUNDEN",
            "error": "FEHLER",
            "success": "ERFOLG"
        }
    }

    def __init__(self):
        self.lang = "EN"

    def set_lang(self, lang_code):
        if lang_code in self.LANGS:
            self.lang = lang_code

    def get(self, key):
        return self.LANGS[self.lang].get(key, key)

tr = Translator()
