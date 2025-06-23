import importlib
import pkgutil
from typing import List
from plugin_interface import TextAnalyzer

class PluginManager:
    def __init__(self, package: str):
        self.package = package
        self.plugins: List[TextAnalyzer] = []

    def load_plugins(self):
        self.plugins.clear()
        package = importlib.import_module(self.package)

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            try:
                module = importlib.import_module(f"{self.package}.{module_name}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and hasattr(obj, 'analyze'):
                        instance = obj()
                        self.plugins.append(instance)
            except Exception as e:
                print(f"[ERROR] Failed to load {module_name}: {e}")

    def get_plugins(self):
        return self.plugins


