### Quant Finance Project Summary

In this project, I worked as an analyst at a bank tasked with improving their failure prediction model. The key steps and results of the project are outlined below:

1. **Feature Engineering**:
   - **New Features**: I introduced two new features:
     - **DER (Debt to Equity Ratio)**: This ratio is a measure of a company's financial leverage. Companies with higher DER are more likely to default due to increased financial risk. I expect a positive relationship between DER and the probability of default.
     - **ROA (Return on Assets)**: A measure of profitability, indicating how efficiently a company uses its assets to generate earnings. I expect a negative relationship between ROA and the probability of default.

2. **Univariate Comparisons**:
   - Conducted univariate comparisons of these two new features for the two classes of the dataset ("0" for non-bankruptcy and "1" for bankruptcy), showing that companies with higher DER and lower ROA are more prone to bankruptcy.

3. **Logit Model**:
   - I used the new features **DER** and **ROA** along with three existing features from the original model:
     - **TLTA (Total Liabilities to Total Assets)**: Measures the financial stability of a company.
     - **WCTA (Working Capital to Total Assets)**: Assesses liquidity and operational efficiency.
     - **FUTL (Funds From Operations to Total Liabilities)**: Captures cash flow adequacy relative to liabilities.
   - The **AUC** (Area Under the Curve) for this model was **0.9284**, indicating strong predictive performance.

4. **Classification Threshold**:
   - I compared the default threshold of **0.50** with an alternative threshold of **0.01** for classification.
   - Metrics for both thresholds were calculated:
     - **Accuracy**: Shows how many predictions were correct.
     - **Recall**: The ability to identify bankrupt companies (true positives).
     - **Precision**: The percentage of correct positive predictions.
   - Based on these metrics, I justified whether a threshold of **0.01** would be more appropriate than the default of **0.50**, balancing the trade-offs between precision and recall.
