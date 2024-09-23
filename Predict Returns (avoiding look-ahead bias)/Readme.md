### Quant Finance Project Techniques

In this project, I focused on identifying two new features that could potentially predict returns, calculating these features while avoiding look-ahead bias, and analyzing portfolio performance based on combined scores. The key techniques and domain knowledge are outlined below:

1. **Feature Selection**:
   - **New Features**:
     - Chose two features not used in class but relevant for predicting stock returns, based on financial theory and empirical evidence.
     - The rationale for these features was explained intuitively, discussing their expected relationships with returns.
   
2. **Avoiding Look-Ahead Bias**:
   - **Look-Ahead Bias Avoidance**:
     - When computing the new features, I ensured that no future information was used by basing feature values only on data available at the time of prediction.
     - This prevents the model from using information that wouldn't have been known at the time, ensuring a more realistic evaluation of model performance.

3. **Portfolio Formation**:
   - **Decile Portfolios**:
     - Formed decile portfolios based on combined feature scores, with Decile 9 representing the top-ranked portfolio and Decile 0 representing the bottom-ranked portfolio.
     - A "diff" portfolio was created by going long in Decile 9 and short in Decile 0, allowing for the analysis of the spread between these extreme portfolios.

4. **Performance Analysis**:
   - **Average Returns and T-Statistics**:
     - Calculated average returns and their associated t-statistics for the "diff" portfolio, assessing the statistical significance of the portfolio's performance.
   - **Market Model Estimation (α and β)**:
     - Estimated the market model parameters (α and β) using Ordinary Least Squares (OLS) regression for each decile portfolio.
     - **α (Alpha)**: Measures the portfolio's performance relative to the market, i.e., the excess return that cannot be explained by market movements.
     - **β (Beta)**: Represents the sensitivity of the portfolio's returns to market movements.
     - These estimates provide insights into how much of the portfolio's returns are driven by market exposure versus idiosyncratic factors.
