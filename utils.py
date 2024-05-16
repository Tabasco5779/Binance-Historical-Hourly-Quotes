import json
import os
from datetime import datetime
from typing import Any, Dict

DATE_FORMAT = "%d/%m/%y"


def save_to_json(data: Dict[str, Any], filename: str, folder: str = 'EXPORT') -> None:
    """
    Save the processed data to a JSON file.

    Args:
        data (Dict[str, Any]): Processed data to be saved.
        filename (str): Name of the output JSON file.
        folder (str): Folder to save the JSON file in.
    """
    os.makedirs(folder, exist_ok=True)  # Ensure the directory exists
    file_path = os.path.join(folder, filename)
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise RuntimeError(f"Error saving data to {file_path}: {e}")


def format_date(date_str: str, input_format: str = DATE_FORMAT, output_format: str = "%d%m%y") -> str:
    """
    Convert date string to a specified format.

    Args:
        date_str (str): Date string to be formatted.
        input_format (str, optional): Format of the input date string. Defaults to DATE_FORMAT.
        output_format (str, optional): Desired format of the output date string. Defaults to "%d%m%y".

    Returns:
        str: Formatted date string.
    """
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except ValueError as e:
        raise RuntimeError(f"Error formatting date {date_str}: {e}")
