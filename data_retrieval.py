import pandas as pd
from binance.client import Client

COLUMNS = [
    'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
    'quote_asset_volume', 'number_of_trades',
    'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
]


def get_historical_data(
        api_key: str,
        api_secret: str,
        symbol: str,
        interval: str,
        start_date: str,
        end_date: str
) -> pd.DataFrame:
    """
    Fetch historical klines from Binance and return as a DataFrame.

    Args:
        api_key (str): Binance API key.
        api_secret (str): Binance API secret.
        symbol (str): Symbol for the trading pair.
        interval (str): Interval for the klines (e.g., '1h').
        start_date (str): Start date for fetching data.
        end_date (str): End date for fetching data.

    Returns:
        pd.DataFrame: DataFrame containing historical klines.
    """
    try:
        client = Client(api_key, api_secret)
        klines = client.get_historical_klines(symbol, interval, start_date, end_date)
        if not klines:
            raise ValueError(f"No data returned for symbol: {symbol}")
    except Exception as e:
        raise RuntimeError(f"Error fetching historical data: {e}")

    # Create DataFrame from fetched klines
    df = pd.DataFrame(klines, columns=COLUMNS)

    # Convert timestamp to datetime and extract date and hour
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms', utc=True)
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour

    return df
