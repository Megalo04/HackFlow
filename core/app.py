from core.logger import logger
from core.env_detector import EnvDetector
from core.config import APP_NAME, VERSION, ETHICS_MESSAGE
from modules.menu.ui import Menu

class App:
    def __init__(self):
        self.name = APP_NAME
        self.version = VERSION
        self.env_detector = EnvDetector()
        self.environment = self.env_detector.env
        self.menu = None

    def start(self):
        logger.info(f"Arrancando {self.name} v{self.version}")
        logger.info(f"Entorno detectado: {self.environment}")
        logger.info(ETHICS_MESSAGE.strip())

        # Crear menú con entorno detectado
        self.menu = Menu(self.environment)
        self.menu.show_main_menu()

if __name__ == "__main__":
    app = App()
    app.start()
