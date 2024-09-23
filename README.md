### Summary of Quantitative Finance Projects

This document summarizes various quantitative finance projects that I have completed, which focus on predictive modeling, portfolio construction, and automated trading systems. Each project emphasizes core techniques and methodologies from the field of quantitative finance, including feature engineering, machine learning, and algorithmic trading.

---

#### 1. **Failure Prediction Model for a Bank**
- **Objective**: Improve a bank's default prediction model by adding two new features.
- **Key Techniques**:
  - Introduced **Debt to Equity Ratio (DER)** and **Return on Assets (ROA)** as additional predictors.
  - Fit a **logit model** using these features and evaluated performance through the **AUC score** (0.9284).
  - Compared classification thresholds of 0.50 and 0.01 to assess **accuracy, recall, and precision**.
- **Quant Finance Relevance**:
  - Similar to risk modeling in finance, feature engineering was critical for improving prediction accuracy.
  - Evaluating classification thresholds is akin to adjusting decision boundaries for portfolio risk management.

---

#### 2. **House Price Prediction (Atlanta County)**
- **Objective**: Predict house prices using a **stacked model** combining Random Forest and Gradient Boosting.
- **Key Techniques**:
  - Feature selection focused on key real estate metrics, including **Total Livable Area (Unit SF)**, **Lot Size (Lot SF)**, and **Distance to Downtown (Miles)**.
  - Model performance was evaluated through **Mean Absolute Error (MAE)** of $24,768 and **R²** score of 0.73.
- **Quant Finance Relevance**:
  - The process of feature normalization and model stacking parallels financial asset pricing models, which often combine linear and non-linear predictors.
  - The use of R² and MAE provides a clear understanding of model effectiveness, much like performance metrics in financial forecasts.

---

#### 3. **Random Forest for Predicting Stock Returns**
- **Objective**: Predict stock returns using a Random Forest model with six financial features.
- **Key Techniques**:
  - Chose six features, including **Investment**, **Accruals**, **Book-to-Market Ratio**, and **Return on Assets (ROA)**.
  - Evaluated decile portfolios and constructed a **long-short** portfolio by going long on Decile 9 and short on Decile 0.
  - Performance metrics such as the **Information Ratio**, **Sharpe Ratio**, and **RMSE** were calculated to assess model effectiveness.
- **Quant Finance Relevance**:
  - The project reflects the real-world application of **portfolio construction** based on stock rankings.
  - Evaluating risk-adjusted returns (Sharpe Ratio) and consistency of alpha (Information Ratio) are fundamental in portfolio management.

---

#### 4. **Interactive Broker Automatic Trading**
- **Objective**: Develop an automatic trading system using **Interactive Brokers API** to trade based on **JPMorgan’s Q Model**.
- **Key Techniques**:
  - Integrated market data from **Yahoo Finance** and **Alpha Vantage** to compute financial ratios like **Book-to-Market Ratio** and **P/E Ratio**.
  - Automated the process of stock selection and trade execution by placing orders for top-ranked stocks based on **Q Score**.
  - Utilized multi-threading for real-time data processing and trade execution.
- **Quant Finance Relevance**:
  - Algorithmic trading systems like this are key in **quantitative hedge funds**, where trades are executed automatically based on predefined models.
  - The project mirrors **quant trading strategies** used by institutions, such as **long-short equity** and **momentum trading**.

---

### Conclusion

Across these projects, I have applied a range of quantitative finance techniques, including **logit regression**, **stacked models**, **random forests**, and **automated trading systems**. Each project emphasizes key principles in quant finance, such as feature selection, model evaluation, risk management, and algorithmic execution. These experiences have enhanced my understanding of how data-driven models can inform investment decisions and trading strategies in real-world financial markets.
