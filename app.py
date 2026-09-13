import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import requests


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Smart Food Waste Intelligence",
    page_icon="🍽️",
    layout="wide"
)


# -----------------------------------
# Load Trained ML Model
# -----------------------------------

model = joblib.load("food_waste_model.pkl")


# -----------------------------------
# Weather API
# -----------------------------------

def get_weather():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 30.3165,
        "longitude": 78.0322,
        "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "timezone": "Asia/Kolkata"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()["current"]


# -----------------------------------
# Prediction Function
# -----------------------------------

def predict_food_waste(input_data):

    input_df = pd.DataFrame([input_data])

    input_df["Food per Guest"] = (
        input_df["Quantity of Food"] /
        input_df["Number of Guests"]
    )

    predicted_waste = model.predict(input_df)[0]

    return predicted_waste


# -----------------------------------
# Optimization Function
# -----------------------------------

def optimize_food_quantity(
    input_data,
    min_percentage=0.85,
    step=5
):

    current_quantity = input_data["Quantity of Food"]

    min_quantity = current_quantity * min_percentage

    candidate_quantities = np.arange(
        min_quantity,
        current_quantity + 1,
        step
    )

    results = []

    for quantity in candidate_quantities:

        test_input = input_data.copy()

        test_input["Quantity of Food"] = quantity

        predicted_waste = predict_food_waste(
            test_input
        )

        predicted_waste_rate = (
            predicted_waste / quantity
        ) * 100

        results.append({

            "Quantity": quantity,

            "Predicted Waste": predicted_waste,

            "Predicted Waste Rate": predicted_waste_rate
        })

    results_df = pd.DataFrame(results)

    best_option = results_df.loc[
        results_df["Predicted Waste"].idxmin()
    ]

    return results_df, best_option


# -----------------------------------
# Title
# -----------------------------------

st.title(
    "🍽️ Smart Food Waste Intelligence System"
)

st.write(
    "An ML-powered system to predict food waste "
    "and recommend an optimal food preparation quantity."
)


# -----------------------------------
# Live Weather Intelligence
# -----------------------------------

st.subheader(
    "🌦️ Live Weather Intelligence"
)

try:

    weather = get_weather()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f"{weather['temperature_2m']} °C"
    )

    col2.metric(
        "Humidity",
        f"{weather['relative_humidity_2m']}%"
    )

    col3.metric(
        "Precipitation",
        f"{weather['precipitation']} mm"
    )

    col4.metric(
        "Wind Speed",
        f"{weather['wind_speed_10m']} km/h"
    )

    temperature = weather["temperature_2m"]

    humidity = weather["relative_humidity_2m"]

    precipitation = weather["precipitation"]


    # Weather-based operational insight

    if humidity >= 80:

        weather_insight = (
            "High humidity detected — storage conditions "
            "should be monitored carefully."
        )

    elif temperature >= 30:

        weather_insight = (
            "High temperature detected — proper food "
            "storage should be prioritized."
        )

    elif precipitation > 0:

        weather_insight = (
            "Rain detected — consider possible changes "
            "in event attendance while planning food."
        )

    else:

        weather_insight = (
            "Current weather conditions are relatively normal."
        )


    st.info(
        f"💡 **Weather Insight:** {weather_insight}"
    )


except Exception:

    st.warning(
        "Weather data unavailable."
    )


# -----------------------------------
# Divider
# -----------------------------------

st.divider()


# -----------------------------------
# Sidebar Inputs
# -----------------------------------

st.sidebar.header(
    "📋 Event Details"
)


food_type = st.sidebar.selectbox(

    "Type of Food",

    [
        "Meat",
        "Baked Goods",
        "Dairy Products",
        "Fruits",
        "Vegetables"
    ]
)


guests = st.sidebar.number_input(

    "Number of Guests",

    min_value=1,

    value=100,

    step=1
)


event_type = st.sidebar.selectbox(

    "Event Type",

    [
        "Corporate",
        "Social Gathering",
        "Wedding",
        "Birthday"
    ]
)


quantity = st.sidebar.number_input(

    "Quantity of Food",

    min_value=1,

    value=300,

    step=5
)


storage = st.sidebar.selectbox(

    "Storage Conditions",

    [
        "Room Temperature",
        "Refrigerated"
    ]
)


purchase = st.sidebar.selectbox(

    "Purchase History",

    [
        "Regular",
        "Occasional"
    ]
)


season = st.sidebar.selectbox(

    "Seasonality",

    [
        "Winter",
        "All Seasons",
        "Summer"
    ]
)


preparation = st.sidebar.selectbox(

    "Preparation Method",

    [
        "Sit-down Dinner",
        "Finger Food",
        "Buffet"
    ]
)


location = st.sidebar.selectbox(

    "Geographical Location",

    [
        "Suburban",
        "Urban",
        "Rural"
    ]
)


pricing = st.sidebar.selectbox(

    "Pricing",

    [
        "High",
        "Moderate",
        "Low"
    ]
)


# -----------------------------------
# Input Dictionary
# -----------------------------------

input_data = {

    "Type of Food": food_type,

    "Number of Guests": guests,

    "Event Type": event_type,

    "Quantity of Food": quantity,

    "Storage Conditions": storage,

    "Purchase History": purchase,

    "Seasonality": season,

    "Preparation Method": preparation,

    "Geographical Location": location,

    "Pricing": pricing
}


# -----------------------------------
# Prediction Button
# -----------------------------------

if st.button(
    "🔮 Predict Food Waste",
    use_container_width=True
):


    # -----------------------------------
    # Current Prediction
    # -----------------------------------

    current_waste = predict_food_waste(
        input_data
    )


    current_waste_rate = (
        current_waste / quantity
    ) * 100


    # -----------------------------------
    # Risk Level
    # -----------------------------------

    if current_waste_rate < 10:

        risk = "Low 🟢"

    elif current_waste_rate < 20:

        risk = "Medium 🟡"

    else:

        risk = "High 🔴"


    # -----------------------------------
    # Optimization
    # -----------------------------------

    optimization_results, best_option = (
        optimize_food_quantity(input_data)
    )


    recommended_quantity = (
        best_option["Quantity"]
    )


    recommended_waste = (
        best_option["Predicted Waste"]
    )


    quantity_reduction = (
        quantity -
        recommended_quantity
    )


    waste_reduction = (
        current_waste -
        recommended_waste
    )


    recommended_waste_rate = (

        recommended_waste /
        recommended_quantity

    ) * 100


    # -----------------------------------
    # Prediction Results
    # -----------------------------------

    st.subheader(
        "📊 Prediction Results"
    )


    col1, col2, col3, col4 = (
        st.columns(4)
    )


    col1.metric(

        "Predicted Food Waste",

        f"{current_waste:.2f}"
    )


    col2.metric(

        "Current Waste Rate",

        f"{current_waste_rate:.2f}%"
    )


    col3.metric(

        "Recommended Quantity",

        f"{recommended_quantity:.0f}"
    )


    col4.metric(

        "Waste Risk",

        risk
    )


    # -----------------------------------
    # Smart Recommendation
    # -----------------------------------

    st.divider()


    st.subheader(
        "💡 Smart Recommendation"
    )


    st.success(

        f"Recommended food preparation quantity: "
        f"**{recommended_quantity:.0f} units**"
    )


    col1, col2, col3 = (
        st.columns(3)
    )


    col1.metric(

        "Current Quantity",

        f"{quantity:.0f}"
    )


    col2.metric(

        "Quantity Reduction",

        f"{quantity_reduction:.0f}"
    )


    col3.metric(

        "Potential Waste Reduction",

        f"{waste_reduction:.2f}"
    )


    # -----------------------------------
    # Optimization Graph
    # -----------------------------------

    st.divider()


    st.subheader(
        "📈 Food Quantity Optimization"
    )


    fig, ax = plt.subplots(
        figsize=(10, 5)
    )


    ax.plot(

        optimization_results["Quantity"],

        optimization_results["Predicted Waste"],

        marker="o"
    )


    ax.axvline(

        recommended_quantity,

        linestyle="--",

        label="Recommended Quantity"
    )


    ax.set_xlabel(
        "Food Quantity"
    )


    ax.set_ylabel(
        "Predicted Food Waste"
    )


    ax.set_title(
        "Food Quantity vs Predicted Food Waste"
    )


    ax.legend()


    ax.grid(True)


    st.pyplot(fig)


    # -----------------------------------
    # Detailed Analysis
    # -----------------------------------

    st.divider()


    st.subheader(
        "🔎 Detailed Analysis"
    )


    st.write(

        f"**Current Predicted Waste:** "
        f"{current_waste:.2f}"
    )


    st.write(

        f"**Recommended Predicted Waste:** "
        f"{recommended_waste:.2f}"
    )


    st.write(

        f"**Current Waste Rate:** "
        f"{current_waste_rate:.2f}%"
    )


    st.write(

        f"**Recommended Waste Rate:** "
        f"{recommended_waste_rate:.2f}%"
    )


    st.write(

        f"**Risk Level:** {risk}"
    )


    st.caption(

        "Note: Recommended quantity is based on "
        "ML-based waste minimization within the "
        "evaluated quantity range."
    )