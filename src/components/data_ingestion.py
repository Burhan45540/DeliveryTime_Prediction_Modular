import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split


class DataIngestionConfig:

    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","data.csv")


class DataIngestion:

    def __init__(self):
        self.ingestionconfig=DataIngestionConfig()


    def initiate_dataingestion(self):

        logging.info("Data Ingestion started")

        try:

            df=pd.read_csv("Notebook/Food_Delivery_Times.csv")

            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)

            df.to_csv(self.ingestionconfig.raw_data_path,header=True,index=False)

            logging.info("Train-Test Split has started")

            train_data,test_data=train_test_split(df,test_size=0.25,random_state=42)

            train_data.to_csv(self.ingestionconfig.train_data_path,header=True,index=False)

            test_data.to_csv(self.ingestionconfig.test_data_path,header=True,index=False)

            logging.info("Train-Test Split Finished")


            return(
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )
        



            
        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    obj=DataIngestion()

    train_data,test_data=obj.initiate_dataingestion()

