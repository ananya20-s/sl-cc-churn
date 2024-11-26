#features to drop, not considered for model
cols_to_drop = ['Customer_Age','Months_on_book','Avg_Open_To_Buy']

#numerical features
num_cols = ['Dependent_count', 'Total_Relationship_Count', 'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 
            'Credit_Limit', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt','Total_Revolving_Bal',
            'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']
#categorical features
cat_cols = ['Gender', 'Education_Level', 'Marital_Status',
       'Income_Category', 'Card_Category']


from sklearn.base import BaseEstimator, TransformerMixin


#Custom Transformers to drop columns
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, cols_to_drop=None):
        self.cols_to_drop = cols_to_drop
        
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        
        X.drop(cols_to_drop,axis=1,inplace=True)
              
        return X


