# 🚀 Delivery Time Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Machine Learning application that predicts **food delivery time** based on delivery distance, weather conditions, traffic level, time of day, vehicle type, food preparation time, and courier experience.

The project follows a **production-style modular architecture** with separate components for data ingestion, preprocessing, model training, prediction, logging, exception handling, and a Flask web interface.

---

# 📌 Project Overview

Fast and accurate delivery time estimation is an important problem in the food delivery industry.

This project uses Machine Learning to estimate the expected delivery time using multiple real-world delivery factors.

Users can enter delivery details through an interactive web application and instantly receive the predicted delivery time.

---

# ✨ Features

* ✅ End-to-End Machine Learning Pipeline
* ✅ Modular Project Structure
* ✅ Feature Engineering Pipeline
* ✅ Data Preprocessing
* ✅ Missing Value Handling
* ✅ One-Hot Encoding
* ✅ Feature Scaling
* ✅ Multiple Regression Algorithms
* ✅ Automatic Best Model Selection
* ✅ Model Serialization using Dill
* ✅ Flask Web Application
* ✅ Custom Exception Handling
* ✅ Logging System
* ✅ Interactive User Interface

---

# 🛠 Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Flask
* Dill

### Machine Learning

* Linear Regression
* Ridge Regression
* Lasso Regression
* ElasticNet
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* AdaBoost Regressor
* K-Nearest Neighbors Regressor

---

# 📂 Project Structure

```text
DeliveryTime_Prediction_Modular/
│
├── artifacts/
│
├── logs/
│
├── notebook/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# ⚙ Machine Learning Pipeline

```
Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Prediction Pipeline
      │
      ▼
Flask Web Application
```

---

# 📊 Input Features

| Feature                | Description                              |
| ---------------------- | ---------------------------------------- |
| Distance_km            | Distance between restaurant and customer |
| Weather                | Weather condition                        |
| Traffic_Level          | Traffic intensity                        |
| Time_of_Day            | Morning, Afternoon, Evening, Night       |
| Vehicle_Type           | Bike, Scooter, Car                       |
| Preparation_Time_min   | Food preparation time                    |
| Courier_Experience_yrs | Delivery partner experience              |

---

# 🎯 Prediction Output

```
Predicted Delivery Time:
34.76 Minutes
```

---

# 🖥 Application Preview

### Home Page

> *(Add screenshot here)*

```
images/home.png
```

---

### Prediction Result

> *(Add screenshot here)*

```
images/result.png
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Burhan45540/DeliveryTime_Prediction_Modular.git
```

Move into the project directory

```bash
cd DeliveryTime_Prediction_Modular
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📈 Model Evaluation

Multiple regression models were trained and evaluated.

The final model was selected based on performance metrics including:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

# 📌 Future Improvements

* Deploy on Render
* Docker Support
* CI/CD Pipeline
* Model Monitoring
* Explainable AI (SHAP)
* REST API Documentation
* User Authentication
* Prediction History Dashboard

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project, feel free to fork the repository and submit a pull request.

---

# 👨‍💻 Author

**Burhan Jalal**

B.Tech Computer Science Student

Aspiring Data Scientist | Machine Learning Engineer

GitHub

https://github.com/Burhan45540

LinkedIn

https://www.linkedin.com/in/burhan-jalal-b23ab031b/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to build more Machine Learning projects.
