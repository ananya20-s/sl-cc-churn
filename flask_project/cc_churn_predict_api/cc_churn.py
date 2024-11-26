# Libraries to help with reading and manipulating data
import joblib
import pandas as pd
import json

from custom_transformer import DropColumns

#STATIC VARIABELES

TEST_SIZE = 0.2
FOLDS = 10
SEED = 42

#manual encoding for target
cust_attrite_map = {'Existing Customer':0,'Attrited Customer':1}




def predict(config):
    ##loading the model from the saved file
    model_filename = "cc_models/churn_pred_model.sav"
    with open(model_filename, 'rb') as f_in:
        model = joblib.load(f_in)

    if type(config) == dict:
        df = pd.DataFrame(config,index=['1'])
       # preprocess(df)
    else:
        df = config
    
    y_pred = model.predict(df)
    return y_pred
    
