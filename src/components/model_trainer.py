from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import os
import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np
from src.utils import save_object,evaluate_model


from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation


class ModelTrainerConfig:
    model_trainer=os.path.join("artifacts","model.pkl")



class ModelTrainer:

    def __init__(self):
        self.modeltrainer=ModelTrainerConfig()


    def models_list(self,final_train,
                    final_test):


        try:
            x_train,y_train,x_test,y_test=(
                final_train[:,:-1],
                final_train[:,-1],
                final_test[:,:-1],
                final_test[:,-1]
            )

            models={
            "AdaBoostRegressor":AdaBoostRegressor(),
            "LinearRegression":LinearRegression(),
            "Ridge":Ridge(),
            "Lasso":Lasso(),
            "ElasticNet":ElasticNet(),
            "DecisionTreeRegressor":DecisionTreeRegressor(),
            "RandomForestRegressor":RandomForestRegressor(),
            "GradientBoostingRegressor":GradientBoostingRegressor(),
            "KNeighborsRegressor":KNeighborsRegressor()   

            }
            params = {

    "AdaBoostRegressor": {
        "n_estimators": [50, 100],
        "learning_rate": [0.01, 0.1]
    },

    "LinearRegression": {
        "fit_intercept": [True, False]
    },

    "Ridge": {
        "alpha": [0.1, 1, 10],
        "fit_intercept": [True, False]
    },

    "Lasso": {
        "alpha": [0.01, 0.1, 1],
        "fit_intercept": [True, False]
    },

    "ElasticNet": {
        "alpha": [0.01, 0.1, 1],
        "l1_ratio": [0.3, 0.5, 0.7]
    },

    "DecisionTreeRegressor": {
        "max_depth": [5, 10, 20],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2]
    },

    "RandomForestRegressor": {
        "n_estimators": [100, 200],
        "max_depth": [10, 20],
        "min_samples_split": [2, 5]
    },

    "GradientBoostingRegressor": {
        "n_estimators": [100, 200],
        "learning_rate": [0.05, 0.1],
        "max_depth": [3, 5]
    },

    "KNeighborsRegressor": {
        "n_neighbors": [3, 5, 7],
        "weights": ["uniform", "distance"]
    }
}

 
            logging.info("Models and Params are initiated")

            model_report=evaluate_model(x_train=x_train,
                                        y_train=y_train,
                                        x_test=x_test,
                                        y_test=y_test,
                                        models=models,
                                        params=params
                                        )
            logging.info("Model evaluation completed")
            best_model_score = max(
                                    model_report[name]["r2_score"]
                                    for name in model_report    
                                )

            best_model_name = max(
                model_report,
                key=lambda name: model_report[name]["r2_score"]
                )

            
            best_model = model_report[best_model_name]["model"]

            logging.info(
                f"Best Model: {best_model_name}, "
                f"Best R2 Score: {best_model_score}"
)

            save_object(
                file_path=self.modeltrainer.model_trainer,
                obj=best_model
            )

        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":

    data_ingestion = DataIngestion()

    train_data, test_data = data_ingestion.initiate_dataingestion()

    
    data_transformation = DataTransformation()

    final_train, final_test, preprocessor_path = (
        data_transformation.train_test_preprocessor(
            train_data,
            test_data
        )
    )

    model_trainer = ModelTrainer()

    model_trainer.models_list(
        final_train,
        final_test
    )