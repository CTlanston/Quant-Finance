### Random Forest Model for Predicting Returns

This project focused on predicting stock returns using a **Random Forest** model, selecting six features for the prediction task, three of which were not used in class. The selected features include key financial ratios that are known to be significant predictors of a company’s performance in quantitative finance:

#### Selected Features:
1. **Investment**: Measures a company's relative investment in capital assets, indicating potential growth.
2. **Accruals**: Reflects the quality of earnings, separating cash from non-cash earnings, crucial for true performance assessment.
3. **Book-to-Market Ratio**: A valuation metric that compares book value to market value, traditionally used to identify undervalued stocks.
4. **Debt-to-Equity Ratio**: A critical measure of leverage that indicates the financial risk associated with the company.
5. **Return on Assets (ROA)**: A profitability metric indicating how efficiently the company uses its assets to generate profit.
6. **Price-to-Earnings Ratio (P/E)**: A commonly used valuation ratio, assessing whether a stock is over or under-valued relative to its earnings.

#### Performance Evaluation:

- **Decile Portfolios**: Portfolios were formed by ranking stocks based on predicted returns into deciles. The portfolios in the top deciles (e.g., Decile 9 and Decile 8) showed higher returns, confirming the efficacy of the stock selection process.
- **Long-Short Portfolio**: A portfolio was constructed by going long on Decile 9 and short on Decile 0. This allowed us to evaluate the return spread and capture excess returns from effective stock ranking.

#### Key Performance Metrics:

1. **Information Ratio**: Highest in Deciles 9 and 8, indicating consistent alpha generation with low tracking error.
   - Purpose: Evaluates the risk-adjusted return relative to benchmark error.
2. **Sharpe Ratio**: A value of **0.884** indicates decent risk-adjusted returns, but with room for improvement.
   - Implication: Indicates the trade-off between risk and return.
3. **Root Mean Square Error (RMSE)**: **0.1895**, representing the average magnitude of the prediction errors, signaling high accuracy in the model’s predictions.

#### Key Domain Knowledge:

1. **Feature Outliers**: Outliers in the selected features can distort predictions in models like Random Forest. While Random Forest is somewhat robust to outliers, extreme values can still skew the results by disproportionately influencing the splits at the decision nodes.
2. **Addressing Overfitting**: The Random Forest algorithm reduces overfitting by averaging predictions across multiple decision trees (ensemble method), ensuring that the model generalizes better to unseen data rather than just memorizing the training data. Random sampling of features also helps reduce the risk of overfitting by introducing variation in the decision trees.

This project highlights the integration of financial domain knowledge in feature selection, leveraging well-established financial metrics to enhance the accuracy of return predictions and the evaluation of decile portfolios. The performance metrics like Information Ratio, Sharpe Ratio, and RMSE offer key insights into the quality of the model's predictions and its ability to handle real-world financial data.
