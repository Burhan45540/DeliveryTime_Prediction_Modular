from src.logger import logging
from src.utils import load_object
import sys
import pandas as pd
from src.exception import CustomException

class PredictPipeline:

    def __init__(self):
        pass

    def predict(self,features):

        try:
            preprocessor=load_object("artifacts/preprocessor.pkl")
            model = load_object(
                "artifacts/model.pkl"
            )

            scaled_data = preprocessor.transform(features)
            prediction=model.predict(scaled_data)

            return prediction

        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    sample_data = pd.DataFrame({
        "Distance_km": [10],
        "Weather": ["Clear"],
        "Traffic_Level": ["High"],
        "Time_of_Day": ["Evening"],
        "Vehicle_Type": ["Bike"],
        "Preparation_Time_min": [15],
        "Courier_Experience_yrs": [2]
    })

    predict_pipeline=PredictPipeline()

    prediction=predict_pipeline.predict(sample_data)

    print(f"Predicted delivery time",prediction[0])
    