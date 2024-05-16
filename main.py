import logging
import os

from dotenv import load_dotenv

from config import load_config
from data_processing import process_data
from data_retrieval import get_historical_data
from utils import save_to_json, format_date


def main() -> None:
    """Main function to execute the data retrieval and processing."""
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

    # Load environment variables from .env file
    load_dotenv()

    # Retrieve API credentials from environment variables
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')

    if not api_key or not api_secret:
        raise ValueError("API_KEY and API_SECRET must be set in the .env file")

    # Load configuration
    config = load_config('config.json')
    symbols = config['symbols']
    start_date = config['start_date']
    end_date = config['end_date']

    interval = '1h'  # Interval for data retrieval is set to 1 hour

    start_date_formatted = format_date(start_date, output_format='%d%m%y')
    end_date_formatted = format_date(end_date, output_format='%d%m%y')

    for symbol in symbols:
        try:
            # Retrieve historical data
            df = get_historical_data(api_key, api_secret, symbol, interval, start_date, end_date)

            # Process the data
            result = process_data(df)

            # Generate the filename dynamically
            filename = f"{symbol}_hourly_{start_date_formatted}_{end_date_formatted}.json"

            # Save the result to a JSON file
            save_to_json(result, filename, folder='EXPORT')

            logging.info(f"Data for {symbol} has been exported to {os.path.join('EXPORT', filename)}")
        except Exception as e:
            logging.error(f"Failed to process data for {symbol}: {e}")


if __name__ == "__main__":
    main()
