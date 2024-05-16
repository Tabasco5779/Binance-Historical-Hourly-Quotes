import json
from typing import Any, Dict


def load_config(config_file: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.

    Args:
        config_file (str): Path to the configuration JSON file.

    Returns:
        Dict[str, Any]: Configuration dictionary.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        raise RuntimeError(f"Configuration file {config_file} not found.")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Error decoding JSON from {config_file}: {e}")
