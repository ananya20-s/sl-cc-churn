# Credit Card Customer Churn Prediction

(/images/cc.avif)

## Objective

The aim of this project is to develop and deploy a machine learning model that can predict whether or not a customer will renounce their credit cards.

This problem statement was part of the solution developed as part of the PGP/AIML program. 
The dataset contains different details like customer age, gender, education, income, card related attributes like type of card, credit limit, number of transactions, bank relationship details like months acitve, total transaction amount, etc

## Approach

- Data Preprocessing
- Perform Exploratory Data Analysis
- Model Building and Evaluation (RandomForest,AdaBoost,GradientBoost,BaggingClassifier and XGBClassifier)
- Pick 3 models for Hyperparameter Tuning using GridSearch
- Finalise the model (XGBClassifier) 

## Results
- Provide Business Insights and Recommendation to prevent customer churn
- Build a pipeline and save model
- Build RestFul API using Flask
- Test the API

## Findings
The credit card customers with below attributes are higher risk of leaving the bank:

- Have less relations with the bank
- less number of transactions in last 12 months
- Transactions of lower amounts in last 12 months
- Inactive for more than 2 months
- Customers with Average Utlization Ratio = 0 (customers who do not use credit cards)
- Income category less than 40K
- Blue Card category

## Key Learnings
- Data analysis to derive Business insights
- Model Building and Evaluation
- Cross Validation and Hyperparameter Tuning
- Deploy the model using API on Flask

## Next Steps
Deploy the API on a Cloud based platform for better availability and scalibility.
