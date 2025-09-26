import importlib

def load_algorithm(name):
    try:
        module = importlib.import_module(f"helpers.algorithms.{name}")
        return module.find_path
    except ImportError:
        raise ValueError(f"Algorithm '{name}' not found")
