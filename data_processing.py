from typing import Any, Dict
import pandas as pd
from utils import format_date


def process_data(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Process the DataFrame and return a dictionary of daily and hourly data.

    Args:
        df (pd.DataFrame): DataFrame containing historical data.

    Returns:
        Dict[str, Any]: Dictionary with processed daily and hourly data.
    """
    result = {}
    grouped = df.groupby('date')

    for date, group in grouped:
        day_data = {
            'Day low': float(group['low'].min()),
            'Day high': float(group['high'].max()),
            'Hours opens': {}
        }

        for hour, hour_group in group.groupby('hour'):
            day_data['Hours opens'][hour] = float(hour_group['open'].values[0])

        # Format the date using format_date before adding to result
        formatted_date = format_date(str(date), input_format='%Y-%m-%d', output_format='%d/%m/%y')
        result[formatted_date] = day_data

    return result
