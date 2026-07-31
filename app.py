from flask import Flask, request, render_template
import pandas as pd

from src.Pipeline.predict_pipeline import PredictPipeline


application = Flask(__name__)

app = application


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():

    if request.method == "GET":
        return render_template("index.html")

    else:

        Distance_km = float(request.form["Distance_km"])
        Weather = request.form["Weather"]
        Traffic_Level = request.form["Traffic_Level"]
        Time_of_Day = request.form["Time_of_Day"]
        Vehicle_Type = request.form["Vehicle_Type"]
        Preparation_Time_min = float(request.form["Preparation_Time_min"])
        Courier_Experience_yrs = float(request.form["Courier_Experience_yrs"])


        data = {
            "Distance_km": [Distance_km],
            "Weather": [Weather],
            "Traffic_Level": [Traffic_Level],
            "Time_of_Day": [Time_of_Day],
            "Vehicle_Type": [Vehicle_Type],
            "Preparation_Time_min": [Preparation_Time_min],
            "Courier_Experience_yrs": [Courier_Experience_yrs]
        }


        final_data = pd.DataFrame(data)


        predict_pipeline = PredictPipeline()

        prediction = predict_pipeline.predict(final_data)


        return render_template(
            "index.html",
            prediction_text=f"Predicted Delivery Time: {prediction[0]:.2f} minutes"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)