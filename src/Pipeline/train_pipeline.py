from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=="__main__":

    data_ingestion=DataIngestion()

    train_data,test_data=data_ingestion.initiate_dataingestion()

    data_transformation=DataTransformation()

    final_train,final_test=data_transformation.train_test_preprocessor(
        train_data,
        test_data
    )

    model_trainer=ModelTrainer()

    model_trainer.models_list(
        final_train,final_test
    )