# Binance Historical Hourly Quotes

**Binance Historical Hourly Quotes** is a Python script designed to retrieve and export historical hourly cryptocurrency quote data from Binance. This tool is ideal for traders, analysts, and developers who need reliable access to historical binance data for backtesting, analysis, or research purposes.


## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Tabasco5779/Binance-Historical-Hourly-Quotes.git
    cd binance-historical-hourly-quotes
    ```

2. **Install required packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your `.env` file with your Binance API credentials:**
    ```env
    API_KEY=your_api_key
    API_SECRET=your_api_secret
    ```

4. **Configure `config.json` with your desired symbols, start date, and end date.** (date format should be day/month/year)

## Usage

Run the script to start retrieving and export data to json file:
```sh
python main.py
```

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to the developers of the libraries used in this project.
