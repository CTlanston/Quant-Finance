### House Price Prediction Project Summary

This project aimed to predict house prices in a specific county in Atlanta using a stacking model that combines non-linear data analysis from **Random Forest** and **Gradient Boosting** with a linear synthesis. The final model’s functional form is:

\[
\text{Price} = -10564 + 0.48 \times \text{Random Forest} + 0.54 \times \text{Gradient Boosting} + \epsilon
\]

Key features used in the model include:

1. **Unit SF (Total Livable Area)**: The most impactful feature in determining housing prices. Its importance was confirmed through **PCA** and **Random Forest** analysis. Standard scaling was applied to normalize its influence across the model.
   
2. **Lot SF (Lot Square Footage)**: Another significant factor in housing prices, the size of the lot contributes to market value. It was standardized to ensure it did not dominate the model due to its size and ensure low correlation with other features (corr <= 0.8).

3. **Miles (Distance to Downtown)**: Captures the geographic advantage, a key determinant of property desirability and pricing. Standard scaling was applied to maintain uniform influence on the predictive outcome.

4. **HOA Dues/Mo (Homeowners Association Dues per Month)**: Reflects the affordability aspect of a property. Standard scaling was applied to assess its relationship with other cost-dependent features.

### Results:

- **Mean Absolute Error (MAE)**: $24,768.28. This indicates that, on average, the predicted house prices deviate from actual prices by $24,768, offering stakeholders a clear understanding of the model's accuracy.
- **R² Score**: 0.73. This signifies that the model explains 73% of the variance in house prices, demonstrating strong explanatory power in capturing the key drivers of pricing in real-world data.

### Quantitative Finance Domain Knowledge

The techniques employed in this project draw parallels to **Quantitative Finance** in the following ways:
- **Feature Importance and Selection**: Similar to financial risk modeling, the use of techniques like **PCA** and **Random Forest** to identify critical features and reduce dimensionality is vital. Understanding the drivers of house prices mirrors the way key factors, such as interest rates or economic indicators, are isolated in financial models.
- **Stacking Model**: The combination of **Random Forest** and **Gradient Boosting** models provides a robust mechanism to predict non-linear relationships, much like in **asset pricing** or **default risk** prediction models in finance, where combining models helps capture both linear and non-linear patterns.
- **Bias Mitigation**: Standard scaling ensures that no one feature overwhelms the model’s performance, a common technique in financial models to prevent factors like outliers or data scale from distorting predictions.
