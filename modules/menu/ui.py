from rich.console import Console
from rich.panel import Panel
from modules.menu.input_handler import InputHandler

class Menu:
    def __init__(self, environment: str):
        self.console = Console()
        self.environment = environment
        self.input_handler = InputHandler()

    def show_main_menu(self):
        self.console.print(
            Panel.fit(
                f"[bold green]Bienvenido a HackFlow[/bold green]\nEntorno detectado: [cyan]{self.environment}[/cyan]",
                title="HackFlow"
            )
        )

        options = {
            "1": "Escaneo de puertos",
            "2": "Reverse Shell",
            "3": "Instalar dependencias",
            "4": "Salir"
        }

        while True:
            self.console.print("\n[bold yellow]Elige una opción:[/bold yellow]")
            for key, val in options.items():
                self.console.print(f"  [cyan]{key}[/cyan] - {val}")

            choice = self.input_handler.ask_option("Opción", choices=list(options.keys()), default="4")

            if choice == "1":
                self.console.print("[green]Ejecutar módulo de escaneo... (pendiente de implementar)[/green]")
            elif choice == "2":
                self.console.print("[green]Ejecutar módulo de reverse shell... (pendiente de implementar)[/green]")
            elif choice == "3":
                self.console.print("[green]Ejecutar módulo de instalación... (pendiente de implementar)[/green]")
            elif choice == "4":
                self.console.print("[bold red]Saliendo...[/bold red]")
                break