from colorama import Fore, Style, init

init(autoreset=True)

class ColorOutput:
    def __init__(self):
        self.colors = {
            'header': Fore.CYAN + Style.BRIGHT,
            'success': Fore.GREEN + Style.BRIGHT,
            'warning': Fore.YELLOW + Style.BRIGHT,
            'error': Fore.RED + Style.BRIGHT,
            'info': Fore.BLUE + Style.BRIGHT,
            'reset': Style.RESET_ALL
        }
    
    def print_header(self, text):
        print(f"\n{self.colors['header']}{text}{self.colors['reset']}")
    
    def print_success(self, text):
        print(f"{self.colors['success']}✓ {text}{self.colors['reset']}")
    
    def print_warning(self, text):
        print(f"{self.colors['warning']}⚠ {text}{self.colors['reset']}")
    
    def print_error(self, text):
        print(f"{self.colors['error']}✗ {text}{self.colors['reset']}")
    
    def print_info(self, text):
        print(f"{self.colors['info']}ℹ {text}{self.colors['reset']}")