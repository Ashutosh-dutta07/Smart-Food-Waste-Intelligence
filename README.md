# 🍽️ Smart Food Waste Intelligence System

An end-to-end Machine Learning application that predicts restaurant food waste, identifies the factors influencing waste predictions, and recommends an optimized food preparation quantity to help reduce unnecessary food waste.

🔗 **Live Demo:** https://smart-food-waste-intelligence-ljsejeeudpxpfyqkc6utwt.streamlit.app/

🔗 **GitHub Repository:** https://github.com/Ashutosh-dutta07/Smart-Food-Waste-Intelligence

---

## 📌 Project Overview

Food waste is a major operational and sustainability challenge for restaurants and food-service businesses.

Preparing too much food can increase waste and operational costs, while preparing too little can affect customer satisfaction.

This project develops a **Smart Food Waste Intelligence System** that combines:

- Data Analysis
- Machine Learning
- Explainable AI
- Optimization
- Weather Intelligence
- Interactive Visualization
- Streamlit Deployment

The system takes food and event-related information as input, predicts the expected amount of food waste, evaluates the waste risk, and recommends a lower food preparation quantity based on ML-driven waste minimization.

---

## 🎯 Project Objective

The main objectives of this project are:

1. Analyze restaurant food-waste patterns.
2. Identify important factors associated with food waste.
3. Build a Machine Learning model to predict food waste.
4. Use Explainable AI (SHAP) to understand model predictions.
5. Develop an optimization-based recommendation system.
6. Integrate live weather information.
7. Build an interactive Streamlit application.
8. Deploy the application so it can be accessed through a web browser.

---

## 🚀 Key Features

### 1. 📊 Exploratory Data Analysis

The dataset was analyzed to understand:

- Food-type distribution
- Event-type distribution
- Storage conditions
- Purchase history
- Seasonality
- Preparation methods
- Geographical locations
- Pricing categories
- Food quantity
- Number of guests
- Food wastage patterns

Additional derived metrics were created for analysis:

- Wastage Rate
- Food per Guest
- Waste per Guest

---

### 2. 🤖 Food Waste Prediction

A **Random Forest Regressor** is used to predict:

> **Wastage Food Amount**

The model uses both categorical and numerical features.

Categorical variables are converted using **One-Hot Encoding**, while numerical features are passed through directly using a Scikit-learn preprocessing pipeline.

---

### 3. 🔍 Explainable AI with SHAP

**SHAP (SHapley Additive exPlanations)** is used to understand which features have the strongest influence on the model's predictions.

The analysis helps answer questions such as:

- Which features strongly influence predicted waste?
- Which feature values tend to increase predictions?
- Which feature values tend to decrease predictions?
- Which variables are most important to the model?

SHAP provides model-level interpretability rather than claiming that a feature directly causes food waste.

---

### 4. 💡 Smart Recommendation Engine

After predicting food waste, the system evaluates different food quantities and identifies an option with lower predicted waste.

The recommendation system provides:

- Current food quantity
- Recommended food quantity
- Quantity reduction
- Current predicted waste
- Recommended predicted waste
- Potential waste reduction
- Current waste rate
- Recommended waste rate
- Waste risk level

---

### 5. 📈 Food Quantity Optimization

The application evaluates candidate food quantities between **85% of the current quantity and the current quantity**.

Candidate quantities are evaluated at a step size of 5 units.

The quantity with the minimum predicted food waste is selected as the recommended quantity.

> **Note:** This is an ML-based waste-minimization approach. The current dataset does not contain a direct measure of food shortage, unmet demand, or customer dissatisfaction. Therefore, the recommendation should be interpreted as a waste-minimization heuristic rather than a complete inventory optimization solution.

---

### 6. 🌦️ Live Weather Intelligence

The application integrates the **Open-Meteo API** to retrieve live weather information.

The dashboard displays:

- Temperature
- Humidity
- Precipitation
- Wind Speed

The system also provides a simple weather-based operational insight.

Weather information is used as contextual information and is not currently a direct ML model feature.

---

### 7. 🖥️ Interactive Streamlit Dashboard

The complete system is available through an interactive Streamlit application.

Users can enter:

- Type of Food
- Number of Guests
- Event Type
- Quantity of Food
- Storage Conditions
- Purchase History
- Seasonality
- Preparation Method
- Geographical Location
- Pricing

The application then generates prediction and recommendation results.

---

## 🧠 Machine Learning Workflow

```text
Restaurant Food-Waste Dataset
            ↓
        Data Cleaning
            ↓
    Exploratory Data Analysis
            ↓
       Feature Engineering
            ↓
        Train-Test Split
            ↓
        One-Hot Encoding
            ↓
      Random Forest Regression
            ↓
        Model Evaluation
            ↓
          SHAP Analysis
            ↓
    Food Quantity Optimization
            ↓
    Smart Recommendation Engine
            ↓
       Streamlit Dashboard
            ↓
        Live Deployment
```

---

## 📂 Dataset

The project uses the **Food Wastage Data in Restaurant** dataset.

### Dataset Summary

- Original records: **1,782**
- Original features: **11**
- Duplicate records identified: **164**
- Records after duplicate removal: **1,618**

### Dataset Columns

| Column | Description |
|---|---|
| Type of Food | Category of food |
| Number of Guests | Number of guests attending the event |
| Event Type | Type of event |
| Quantity of Food | Quantity of food prepared |
| Storage Conditions | Food storage condition |
| Purchase History | Regular or occasional purchase |
| Seasonality | Seasonal category |
| Preparation Method | Food preparation/service method |
| Geographical Location | Location category |
| Pricing | Pricing category |
| Wastage Food Amount | Target variable representing food waste |

---

## ⚙️ Feature Engineering

Additional features were created during the analysis.

### Wastage Rate

```text
Wastage Rate = (Wastage Food Amount / Quantity of Food) × 100
```

### Food per Guest

```text
Food per Guest = Quantity of Food / Number of Guests
```

### Waste per Guest

```text
Waste per Guest = Wastage Food Amount / Number of Guests
```

### Target Leakage Prevention

`Wastage Rate` and `Waste per Guest` were not used as Machine Learning input features because they are calculated using the target variable `Wastage Food Amount`.

Using target-derived features as model inputs can cause **target leakage** and lead to misleading model performance.

---

## 🧪 Machine Learning Model

### Algorithm

The project uses a **Random Forest Regressor** to predict food wastage.

Random Forest was selected because it can capture nonlinear relationships between different food, event, quantity, and operational characteristics.

### Input Features

The model uses the following features:

- Type of Food
- Number of Guests
- Event Type
- Quantity of Food
- Storage Conditions
- Purchase History
- Seasonality
- Preparation Method
- Geographical Location
- Pricing
- Food per Guest

### Target Variable

`Wastage Food Amount`

### Preprocessing

Categorical variables are transformed using **One-Hot Encoding**, while numerical features are passed through the preprocessing pipeline.

A Scikit-learn `ColumnTransformer` and `Pipeline` are used to combine preprocessing and model training into a single workflow.

---

## 📏 Model Evaluation

The model is evaluated using standard regression metrics.

### MAE — Mean Absolute Error

Measures the average absolute difference between the actual and predicted food-waste values.

### RMSE — Root Mean Squared Error

Measures prediction error while giving greater importance to larger errors.

### R² Score

Measures how much of the variation in the target variable is explained by the model.

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

The testing data is kept separate and used to evaluate model performance on unseen observations.

---

## 🔍 Explainable AI — SHAP

The project uses **SHAP (SHapley Additive exPlanations)** to interpret the Machine Learning model.

SHAP helps identify which features have the strongest influence on the model's predictions.

The analysis helps answer:

- Which features strongly influence predicted food waste?
- Which feature values tend to increase predictions?
- Which feature values tend to decrease predictions?
- Which variables are most important to the model?

### Important Interpretation Note

SHAP explains **model behavior and associations**. It does not prove that a particular feature directly causes food waste.

A feature having high SHAP importance means that the model relies strongly on that feature when making a prediction.

---

## 💡 Smart Recommendation Engine

The system goes beyond prediction by providing a recommendation for food preparation quantity.

For a given event, the recommendation engine:

1. Takes event and food-related information as input.
2. Predicts the expected food waste.
3. Evaluates multiple candidate food quantities.
4. Predicts the expected waste for each candidate quantity.
5. Compares the predicted waste values.
6. Selects the quantity associated with the lowest predicted waste within the evaluated range.
7. Displays the recommended quantity and potential waste reduction.

### Recommendation Output

The application provides:

- Current Quantity
- Recommended Quantity
- Quantity Reduction
- Current Predicted Waste
- Recommended Predicted Waste
- Potential Waste Reduction
- Current Waste Rate
- Recommended Waste Rate
- Waste Risk Level

---

## 📈 Food Quantity Optimization

The optimization module evaluates different food quantities between **85% of the current quantity and the current quantity**.

Candidate quantities are evaluated at a step size of 5 units.

The quantity with the minimum predicted food waste is selected as the recommended quantity.

### Optimization Workflow

```text
Current Food Quantity
        ↓
Generate Candidate Quantities
        ↓
Predict Waste for Each Quantity
        ↓
Calculate Predicted Waste Rate
        ↓
Compare Predictions
        ↓
Select Minimum Predicted Waste
        ↓
Recommended Food Quantity
```

---

## 📊 Weather Intelligence

The system integrates live weather information to provide additional environmental context for food-waste prediction.

### Weather Parameters

- 🌡️ Temperature
- 💧 Humidity
- 🌧️ Precipitation
- 💨 Wind Speed

Weather data is retrieved using the Open-Meteo API.

The weather information helps provide additional context around the conditions under which food preparation and wastage decisions are made.

---

## 🖥️ Streamlit Dashboard

The complete Machine Learning workflow is integrated into an interactive Streamlit web application.

### Dashboard Capabilities

- Enter event and food-related information
- View live weather conditions
- Predict expected food waste
- Calculate predicted wastage rate
- Identify waste risk level
- Get recommended food preparation quantity
- Estimate potential food-waste reduction
- Visualize food quantity optimization

### User Workflow

```text
User Input
    ↓
Weather Information
    ↓
Feature Engineering
    ↓
Machine Learning Model
    ↓
Food Waste Prediction
    ↓
Risk Assessment
    ↓
Quantity Optimization
    ↓
Smart Recommendation
```

---

## 🏗️ Application Architecture

```text
                    ┌──────────────────────┐
                    │      User Input      │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Feature Engineering  │
                    │    Food per Guest    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Random Forest      │
                    │     Regression       │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Food Waste         │
                    │     Prediction       │
                    └──────────┬───────────┘
                               ↓
              ┌────────────────┴────────────────┐
              ↓                                 ↓
     ┌──────────────────┐             ┌──────────────────┐
     │  Risk Assessment │             │  SHAP Analysis   │
     └────────┬─────────┘             └──────────────────┘
              ↓
     ┌──────────────────┐
     │ Quantity         │
     │ Optimization     │
     └────────┬─────────┘
              ↓
     ┌──────────────────┐
     │ Smart Food       │
     │ Recommendation   │
     └──────────────────┘
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and Machine Learning |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Scikit-learn | Machine Learning |
| Random Forest | Food waste prediction |
| SHAP | Model explainability |
| Matplotlib | Data visualization |
| Streamlit | Interactive web application |
| Requests | Weather API integration |
| Joblib | Model serialization |
| Open-Meteo API | Weather intelligence |
| Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
Smart-Food-Waste-Intelligence/
│
├── app.py
├── food_wastage_data.csv
├── food_waste_model.pkl
├── MINOR PROJECT (2).ipynb
├── import_data.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Ashutosh-dutta07/Smart-Food-Waste-Intelligence.git
```

### 2. Navigate to the Project Folder

```bash
cd Smart-Food-Waste-Intelligence
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🌐 Live Demo

The project is deployed using **Streamlit Community Cloud**.

🔗 **Live Application:**

https://smart-food-waste-intelligence-ljsejeeudpxpfyqkc6utwt.streamlit.app/

The deployed application allows users to interact with the food-waste prediction and recommendation system directly through a web browser.

---

## 🔐 Security

The project follows basic security practices for handling sensitive configuration information.

- Database credentials are not hard-coded in the application.
- Local secrets are stored using Streamlit secrets.
- `.streamlit/secrets.toml` is excluded from Git.
- Passwords and API credentials are not committed to the repository.
- Sensitive configuration is separated from application code.

---

## ⚠️ Limitations

Although the system provides an end-to-end intelligent food-waste workflow, there are some limitations.

### 1. Dataset Size

The dataset contains 1,782 original records, which is relatively small for developing a highly generalized production-level ML system.

### 2. Historical Dataset

The model learns patterns from historical restaurant food-waste data. Real-world restaurant behavior may vary depending on location, customer behavior, menu, season, and operational practices.

### 3. Recommendation Optimization

The quantity recommendation is based on ML-predicted waste and candidate quantity comparison.

It should therefore be considered an optimization heuristic rather than a guaranteed demand-forecasting solution.

### 4. Demand Availability

The current dataset does not contain an explicit variable representing actual customer demand or food shortage.

Therefore, the optimization focuses primarily on reducing predicted waste rather than jointly optimizing:

```text
Food Waste
+
Customer Demand Satisfaction
```

### 5. Weather Influence

Weather information is currently provided as additional environmental context. The current trained model is based on the available dataset features and does not claim that weather directly causes food waste.

---

## 🔮 Future Scope

The system can be further improved with additional real-world data and advanced Machine Learning techniques.

### Possible Future Enhancements

- 📈 Real-time restaurant demand forecasting
- 🤖 XGBoost / LightGBM model comparison
- 🧠 Deep Learning based prediction
- 📦 Inventory optimization
- 🍽️ Dish-level demand forecasting
- 🌦️ Weather-aware demand prediction
- 📅 Festival and holiday effects
- 🏪 Restaurant-specific models
- 📊 Real-time PostgreSQL integration
- 🔄 Automated model retraining
- 📱 Mobile-friendly application
- ☁️ Cloud database integration
- 💰 Cost-based food optimization
- ♻️ Carbon-footprint estimation
- 🎯 Joint optimization of waste and customer demand

A future version can optimize preparation quantity using a multi-objective approach:

```text
Minimize:
    Food Waste
    +
Food Cost
    +
Inventory Loss

Subject to:
    Customer Demand Satisfaction
    +
Minimum Food Availability
```

---

## 📌 Key Project Highlights

### End-to-End Machine Learning

The project covers the complete ML workflow:

```text
Data
 ↓
Data Cleaning
 ↓
Exploratory Data Analysis
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Model Evaluation
 ↓
SHAP Explainability
 ↓
Prediction
 ↓
Optimization
 ↓
Recommendation
 ↓
Streamlit Deployment
```

### Explainable AI

SHAP is used to understand which features have the strongest influence on the model's predictions.

This improves model interpretability and helps users understand why the model produces a particular prediction.

### Decision Support

The project goes beyond simple prediction.

Instead of only answering:

> "How much food waste is expected?"

the system also provides:

> "What food quantity can be recommended based on the model's predicted waste?"

This makes the project more useful as a practical decision-support system.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Feature engineering
- Categorical feature encoding
- Regression Machine Learning
- Random Forest
- Model evaluation
- Feature importance analysis
- SHAP explainability
- Optimization logic
- API integration
- Streamlit application development
- Model deployment
- Git and GitHub
- Project documentation

---

## 🎯 Conclusion

The **Smart Food Waste Intelligence System** demonstrates how Machine Learning can be used to transform historical restaurant food-waste data into actionable decision support.

The system combines:

```text
Machine Learning
+
Explainable AI
+
Optimization
+
Weather Intelligence
+
Interactive Dashboard
```

to create an end-to-end solution for predicting food waste and recommending more efficient food preparation quantities.

The project demonstrates practical application of Data Science concepts to a real-world sustainability problem and provides a foundation for future improvements using real-time restaurant demand, inventory, cost, and operational data.

---

## 🔗 Project Links

### GitHub Repository

https://github.com/Ashutosh-dutta07/Smart-Food-Waste-Intelligence

### Live Streamlit Application

https://smart-food-waste-intelligence-lsjeeeudpxfyqkc6utwt.streamlit.app/

---

## 👨‍💻 Author

**Ashutosh Kumar**

Aspiring Data Analyst | Data Science Enthusiast | Machine Learning | Python | SQL | Power BI

---

⭐ If you find this project useful, consider giving the repository a star!
