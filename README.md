# Algorithmic Trading using Momentum Strategy and Python

This is a Python application that uses the Streamlit library to perform algorithmic trading analysis based on stock momentum. It retrieves stock data from Yahoo Finance using the `yfinance` library and visualizes the momentum and buying/selling signals using Plotly.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/shaadclt/Algorithmic-Trading-Python.git
    ```
    
2. Install the required Python packages:
    ```shell
   pip install -r requirements.txt
    ```
    
## Usage
1.Run the application:

    ```shell
    streamlit run app.py
    ```
    
2. Enter a stock ticker (e.g., AAPL) in the input field.

3. Select a period from the dropdown menu (1mo, 3mo, 6mo, 1y).

4. The application will display a plot showing the stock's close price and momentum. It will also indicate the buy and sell signals based on the momentum.

## Contributing
Contributions are welcome! If you find any issues or want to enhance the functionality of the application, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
