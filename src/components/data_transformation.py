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
from src.utils import save_object


class DataTransformationConfig:
    preprocessor_path=os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:

    def __init__(self):
        self.data_transform=DataTransformationConfig()


    def data_preprocessor(self):

        try:
            logging.info("Start making Numerical and categorical features")
            num_features=[
    "Distance_km","Preparation_Time_min","Courier_Experience_yrs"
]
            cat_features=[
    "Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"

]
            logging.info("Pipeline has been started")

            num_pipeline=Pipeline(
                steps=[
                    ("simple imputer",SimpleImputer(strategy="mean")),
                    ("standard scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("simple imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot encoder",OneHotEncoder()),
                    ("standard scaler",StandardScaler(with_mean=False))

                ]
            )

            logging.info("Preprossor started")


            preprocessor=ColumnTransformer(
                transformers=[
                    ("num_pipeline",num_pipeline,num_features),
                    ("cat_pipeline",cat_pipeline,cat_features)
                ]
            )

            logging.info("Preprossor complete")

            return preprocessor

        
        
        except Exception as e:
            raise CustomException(e,sys)


    def train_test_preprocessor(self,train_data,test_data):

        try:
            preprocessortransform=self.data_preprocessor()

            train_df=pd.read_csv(train_data)
            test_df=pd.read_csv(test_data)

            target_column="Delivery_Time_min"

            independent_train=train_df.drop(columns=["Delivery_Time_min","Order_ID"],axis=1)
            dependent_train=train_df[target_column]


            independent_test=test_df.drop(columns=["Delivery_Time_min","Order_ID"],axis=1)
            dependent_test=test_df[target_column]

            train_transformed=preprocessortransform.fit_transform(independent_train)
            test_transformed=preprocessortransform.transform(independent_test)

            final_train=np.c_[
                train_transformed,
                np.array(dependent_train)
            ]

            final_test=np.c_[
                test_transformed,
                np.array(dependent_test)
            ]


            save_object(
                file_path=self.data_transform.preprocessor_path,
                obj=preprocessortransform
            )

            return (
                final_train,
                final_test,
    
            )



            
        except Exception as e:
            raise CustomException(e,sys)




if __name__=="__main__":

    obj=DataTransformation()

    train_data="artifacts/train.csv"
    test_data="artifacts/test.csv"

    obj.train_test_preprocessor(
        train_data,test_data
    )




























