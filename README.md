Customer Churn Prediction for a Telecom Company

Project Overview
This project aims to develop a predictive model for identifying the probability of customer churn in a telecom company. Using historical customer data, the project leverages exploratory data analysis (EDA), data preprocessing, and machine learning techniques to build an accurate churn prediction model.

Features
-Exploratory Data Analysis (EDA):
--Dataset Overview:The project analyzes a dataset of over 70,000 unique customers from an internet service provider.
---Includes customer-specific attributes such as subscription age, average bill amount, service failures, and download/upload speeds.
--Data Visualization:
---Histograms for numeric variables (e.g., subscription_age, bill_avg) to understand their distribution.
---Correlation heatmaps to identify relationships between features, such as service_failure_count and churn.
---Bar plots for binary features like is_tv_subscriber and is_movie_package_subscriber to observe their impact on churn.
--Insights Derived:
---Customers with higher service_failure_count show a strong likelihood of churning.
---A longer remaining_contract correlates with reduced churn likelihood.
---Excessive download_over_limit is a potential churn driver.
--Feature Importance:
---The analysis highlights key predictors of churn, including service_failure_count, remaining_contract, and bill_avg.
-Data Preprocessing:
--Handling missing values.
--Normalization and encoding categorical variables.
-Model Development:
--Implementation of machine learning algorithms for churn prediction.
--Evaluation using metrics like Accuracy, Recall, Precision, and F1 Score.
-Deployment:
--Dockerized model for ease of deployment and reproducibility.

Technologies Used
Languages: Python
Libraries:
Pandas, NumPy for data manipulation.
Matplotlib, Seaborn for data visualization.
Scikit-learn for machine learning.
Tools:
Jupyter Notebook for development and analysis.
Git & GitHub for version control and collaboration.
Docker for containerization.

Installation
...

Usage
...

Repository Structure