# **Trading Strategy Robustness Analysis** 📈💹

This project evaluates the **robustness of five trading strategies** across various market conditions using backtesting and cross-validation techniques. By analyzing performance metrics, we aim to identify the most reliable strategies for trading the EUR/USD currency pair and other forex pairs.

---

## **Project Highlights**

- **Strategies Tested**:
  - 📊 Bollinger Bands
  - 📈 Relative Strength Index (RSI)
  - 🔄 Moving Average Convergence Divergence (MACD)
  - 📉 Simple Moving Average (SMA) Crossover
  - 🎯 Stochastic Oscillator
- **Backtesting and Cross-Validation**:
  - Evaluate strategies on historical data with cash of $10,000 and a commission of 0.24%.
  - Optimize hyperparameters for improved performance.
- **Currency Pairs Tested**:
  - Primary focus: EUR/USD
  - Additional tests on 19 other forex pairs (e.g., USDJPY, GBPUSD, AUDUSD).

---

## **Key Features**

### **Backtesting**
- Analyze strategy performance on historical data using the `backtesting.py` library.
- Metrics evaluated:
  - Final Equity
  - Profit/Loss (PnL)
  - Sharpe Ratio
  - Win Rate (%)

### **Hyperparameter Optimization**
- Optimize strategy parameters using ranges for indicators like RSI thresholds, SMA windows, and Bollinger Band deviations.

### **Cross-Validation**
- Validate optimized strategies on out-of-sample data to ensure robustness.
- Compare backtesting results with cross-validation metrics.

### **Multi-Currency Testing**
- Test strategies on 20 forex pairs to assess robustness across different markets.

---

## **Results Summary**

### 🏆 Best Strategy: **Relative Strength Index (RSI)**
- RSI showed the most robust performance with:
  - Positive returns for multiple currency pairs.
  - High Sharpe and Sortino ratios during cross-validation.

### 📉 Worst Strategy: **Simple Moving Average Crossover**
- SMA Crossover consistently underperformed with no profitable trades across all currency pairs.

### Performance Rankings:
1. RSI
2. Bollinger Bands
3. Stochastic Oscillator
4. MACD
5. SMA Crossover

---

## **Example Metrics (EUR/USD)**

| Strategy          | Final Equity | Return % | Sharpe Ratio | Win Rate (%) |
|-------------------|--------------|----------|--------------|--------------|
| Bollinger Bands   | $10,439.82   | +4.40%   | 0.41         | 41.86%       |
| RSI               | $11,326.98   | +13.27%  | 1.16         | 37.04%       |
| MACD              | $6,090.76    | -39.09%  | 0.00         | 26.32%       |
| SMA Crossover     | $9,895.86    | -1.04%   | 0.00         | 27.71%       |
| Stochastic Oscillator | $9,954.40    | -0.46%   | 0.00         | 47.50%       |

---

## **How to Run**

### Prerequisites
1. Install Python and required libraries:
   ```bash
   pip install pandas numpy matplotlib pandas-ta yfinance backtesting seaborn
   ```

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/trading-strategy-analysis.git
   cd trading-strategy-analysis
   ```
2. Run the Jupyter Notebook or Python script:
   ```bash
   jupyter notebook Trading-Strategy-Robustness-Analysis.ipynb
   ```

3. To backtest multiple currency pairs:
   ```bash
   python bulk_backtest.py
   ```

---

## **Folder Structure**

```
project/
│
├── Trading-Strategy-Robustness-Analysis.ipynb # Main analysis notebook
├── bulk_backtest.py                           # Script for multi-currency backtesting
├── data/                                      # Contains insample and outsample datasets
├── results/                                   # Backtesting and validation metrics (.csv)
└── README.md                                  # Project documentation
```

---

## **Future Improvements**
1. Improve hyperparameter optimization with Bayesian methods.
2. Develop a dashboard for real-time strategy evaluation.

---