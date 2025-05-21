import platform
import subprocess

class EnvDetector:
    def __init__(self):
        self.env = self.detect_environment()

    def detect_environment(self) -> str:
        """
        Detecta el entorno actual y devuelve una cadena identificativa:
        'termux', 'ubuntu', 'parrot', 'unknown'
        """
        if self.is_termux():
            return "termux"
        elif self.is_kali():
            return "kali"
        elif self.is_ubuntu():
            return "ubuntu"
        else:
            return "unknown"

    def is_termux(self) -> bool:
        try:
            # En Termux la variable $PREFIX suele contener /data/data/com.termux/files/usr
            prefix = subprocess.check_output("echo $PREFIX", shell=True, text=True).strip()
            return "com.termux" in prefix
        except Exception:
            return False

    def is_ubuntu(self) -> bool:
        try:
            dist = platform.linux_distribution()[0].lower()
            return "ubuntu" in dist
        except AttributeError:
            # platform.linux_distribution fue removido en Python 3.8+
            # Intentamos leer /etc/os-release
            try:
                with open("/etc/os-release") as f:
                    content = f.read().lower()
                    return "ubuntu" in content
            except FileNotFoundError:
                return False

    def is_kali(self) -> bool:
        try:
            with open("/etc/os-release") as f:
                content = f.read().lower()
                return "kali" in content
        except FileNotFoundError:
            return False

if __name__ == "__main__":
    detector = EnvDetector()
    print(f"Entorno detectado: {detector.env}")
