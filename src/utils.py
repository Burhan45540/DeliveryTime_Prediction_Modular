import sys
import os
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import numpy as np
from sklearn.model_selection import GridSearchCV



def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)



def evaluate_model(x_train,y_train,x_test,y_test,models,params):
    report={}

    for name, model in models.items():

        grid_model=GridSearchCV(
            estimator=model,
            param_grid=params[name],
            cv=3
        )

        grid_model.fit(x_train,y_train)

        best_model=grid_model.best_estimator_
        best_params=grid_model.best_params_

       
        y_test_pred = best_model.predict(x_test)
        
        
        test_r2 = r2_score(y_test, y_test_pred)
        
        
        print(f"--- {name} ---")
        
        print("Test R2 Score:", test_r2)

        report[name]={

            "model":best_model,
            "r2_score":test_r2,
            "best_params":best_params
        }

    return report
        



def load_object(file_path):

    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e,sys)

        
        



    