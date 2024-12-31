import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

with open('gradient_boosting_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

columns_to_filter = [
    "service_failure_count", "download_avg", "upload_avg",
    "download_over_limit", "subscription_age", "bill_avg"
]

data_stats = {
    "service_failure_count": {"Q1": 0.0, "Q3": 2.0},
    "download_avg": {"Q1": 50.0, "Q3": 300.0},
    "upload_avg": {"Q1": 10.0, "Q3": 100.0},
    "download_over_limit": {"Q1": 0, "Q3": 5},
    "subscription_age": {"Q1": 12, "Q3": 36},
    "bill_avg": {"Q1": 20.0, "Q3": 80.0},
}

columns_scaling = {
    "MinMaxScaler": ["service_failure_count", "download_over_limit", "is_tv_subscriber",
                     "is_movie_package_subscriber", "subscription_age", "bill_avg",
                     "download_avg", "upload_avg"]
}

scaler = MinMaxScaler()
scaler.fit([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 7, 1, 1, 100, 1000, 300, 100]
])

def filter_iqr(value, column_name):
    Q1 = data_stats[column_name]["Q1"]
    Q3 = data_stats[column_name]["Q3"]
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return max(min(value, upper_bound), lower_bound)

st.title("Прогноз відтоку клієнтів")

st.header("Введіть дані клієнта:")

is_tv_subscriber = st.selectbox("Клієнт підписаний на ТВ?", ["Yes", "No"])
is_movie_package_subscriber = st.selectbox("Клієнт підписаний на кіно-пакет?", ["Yes", "No"])
subscription_age = st.number_input("Вік підписки (у місяцях):", min_value=0, step=1)
bill_avg = st.number_input("Середній рахунок:", min_value=0.0, step=0.1)
service_failure_count = st.number_input("Кількість збоїв у послугах:", min_value=0, step=1)
download_avg = st.number_input("Середнє завантаження:", min_value=0.0, step=0.1)
upload_avg = st.number_input("Середня віддача:", min_value=0.0, step=0.1)
download_over_limit = st.selectbox("Перевантаження завантажень:", [0, 1, 2, 3, 4, 5, 6, 7])

is_tv_subscriber = 1 if is_tv_subscriber == "Yes" else 0
is_movie_package_subscriber = 1 if is_movie_package_subscriber == "Yes" else 0

service_failure_count = filter_iqr(service_failure_count, "service_failure_count")
download_avg = filter_iqr(download_avg, "download_avg")
upload_avg = filter_iqr(upload_avg, "upload_avg")
download_over_limit = filter_iqr(download_over_limit, "download_over_limit")
subscription_age = filter_iqr(subscription_age, "subscription_age")
bill_avg = filter_iqr(bill_avg, "bill_avg")

input_data = np.array([[
    service_failure_count, download_over_limit, is_tv_subscriber,
    is_movie_package_subscriber, subscription_age, bill_avg,
    download_avg, upload_avg
]])

scaled_data = scaler.transform(input_data)

if st.button("Перевірити"):
    try:
        prediction = loaded_model.predict_proba(scaled_data)[0][1]
        st.subheader(f"Імовірність відтоку: {prediction * 100:.2f}%")

        if prediction > 0.5:
            st.error("Клієнт має високу ймовірність відтоку!")
        else:
            st.success("Клієнт має низьку ймовірність відтоку!")
    except ValueError as e:
        st.error(f"Помилка: {str(e)}")
