from rich.console import Console
from rich.text import Text

class Logger:
    def __init__(self):
        self.console = Console()

    def info(self, message: str):
        self.console.print(f"[bold cyan][INFO][/bold cyan] {message}")

    def warning(self, message: str):
        self.console.print(f"[bold yellow][WARNING][/bold yellow] {message}")

    def error(self, message: str):
        self.console.print(f"[bold red][ERROR][/bold red] {message}")

# Instancia global para usar en toda la app
logger = Logger()
