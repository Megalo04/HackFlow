from rich.prompt import Prompt
from rich.console import Console

class InputHandler:
    def __init__(self):
        self.console = Console()

    def ask_option(self, prompt: str, choices: list[str], default: str = None) -> str:
        """
        Pide al usuario una opción válida de la lista `choices`.
        Reintenta hasta que el usuario introduzca una opción válida.
        """
        while True:
            try:
                choice = Prompt.ask(prompt, choices=choices, default=default)
                return choice
            except KeyboardInterrupt:
                self.console.print("\n[red]Entrada interrumpida por el usuario.[/red]")
                raise
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")