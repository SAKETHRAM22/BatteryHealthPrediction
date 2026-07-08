
# 🔋 Battery Health Prediction Platform

> **An end-to-end AI-powered Battery Health Prediction Platform built using Deep Learning (LSTM + GRU), Streamlit, TensorFlow, and Plotly for predicting battery capacity, State of Health (SOH), Remaining Useful Life (RUL), and future capacity degradation.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-orange?style=for-the-badge&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-3.15-red?style=for-the-badge&logo=keras)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 🌐 Live Demo

🔗 **Application:**  
https://batteryhealthprediction-xb2yby38reheopbiqoymdh.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/SAKETHRAM22/BatteryHealthPrediction

---

# 📌 Project Overview

Lithium-ion batteries degrade over time due to repeated charge-discharge cycles, causing a gradual reduction in usable capacity.

This project presents an intelligent Battery Health Prediction Platform capable of predicting:

- 🔋 Next Cycle Battery Capacity
- 📈 Multi-Step Capacity Forecasting
- 💚 State of Health (SOH)
- ⏳ Remaining Useful Life (RUL)
- ⚠ Battery Health Status

using a **hybrid LSTM + GRU Deep Learning architecture** trained on battery degradation datasets.

The application provides an interactive web dashboard for real-time prediction and visualization.

---

# 🚀 Features

### 📊 Interactive Dashboard

- Modern Streamlit Interface
- Real-time Battery Monitoring
- KPI Cards
- Interactive Charts

---

### 🔋 Battery Prediction

Predict battery capacity using the previous 10 charge/discharge cycles.

Outputs:

- Predicted Capacity
- Battery SOH
- Battery Status
- Remaining Useful Life

---

### 📈 Capacity Forecast

Recursive multi-step forecasting for

- 1 Cycle
- 5 Cycles
- 10 Cycles
- 20 Cycles
- 50 Cycles

Visualized using Plotly.

---

### 📊 Model Performance

Performance comparison of

- CNN
- LSTM
- GRU
- CNN + GRU
- LSTM + CNN
- LSTM + GRU
- LSTM + CNN + GRU
- Tuned LSTM + GRU

---

### 📁 Prediction History

Automatically stores prediction history including

- Capacity
- SOH
- RUL
- Forecast Horizon

---

# 🧠 Deep Learning Architecture

```
Battery Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Sliding Window
(10 Previous Cycles)
        │
        ▼
MinMax Scaling
        │
        ▼
Tuned LSTM + GRU Model
        │
        ▼
Predicted Capacity
        │
 ┌──────┴─────────┐
 ▼                ▼
SOH            Forecast
 │                │
 ▼                ▼
Battery Status   Remaining Useful Life
        │
        ▼
Streamlit Dashboard
```

---

# ⚙ Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Deep Learning | TensorFlow, Keras |
| Machine Learning | Scikit-learn |
| Visualization | Plotly |
| Web Application | Streamlit |
| Data Processing | Pandas, NumPy |
| Data Storage | Pickle |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
BatteryHealthPrediction
│
├── battery_health_platform/
│   ├── app.py
│   ├── backend.py
│   ├── dashboard.py
│   ├── prediction.py
│   ├── performance.py
│   ├── forecast.py
│   ├── history.py
│   ├── about.py
│   ├── styles.py
│   └── utils.py
│
├── models/
│   └── Best_LSTM_GRU.keras
│
├── scaler/
│   └── scaler.pkl
│
├── data/
│   └── capacityFade.xlsx
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# 📈 Model Performance

| Model | MAE | RMSE | MAPE | R² |
|------|------:|------:|------:|------:|
| CNN | 5.92 | 7.41 | 1.12 | 0.541 |
| LSTM | 4.84 | 6.33 | 0.91 | 0.646 |
| GRU | 4.51 | 5.98 | 0.86 | 0.691 |
| CNN + GRU | 3.88 | 5.12 | 0.74 | 0.742 |
| LSTM + CNN | 3.64 | 4.84 | 0.69 | 0.779 |
| LSTM + GRU | 3.12 | 4.21 | 0.59 | 0.811 |
| LSTM + CNN + GRU | 3.34 | 4.48 | 0.64 | 0.798 |
| **Tuned LSTM + GRU** | **4.29** | **6.14** | **0.67** | **0.9979** |

> **Note:** The Tuned LSTM + GRU model is the deployed production model

---

## Battery P

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/SAKETHRAM22/BatteryHealthPrediction.git
```

Move into the project directory

```bash
cd BatteryHealthPrediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run battery_health_platform/app.py
```

---

# 🎯 Future Improvements

- Transformer-based Battery Prediction
- Attention-based LSTM
- Uncertainty Estimation
- Battery Health Classification
- Cloud Database Integration
- REST API Deployment
- IoT Battery Monitoring
- Mobile Application

---

# 👨‍💻 Author

**Saketh Ram**

Final Year B.Tech Student  
Department of Electrical Engineering  
National Institute of Technology Silchar

GitHub

https://github.com/SAKETHRAM22



---

# ⭐ Support

If you found this project useful,

⭐ Star the repository

Fork it

Share it with others
<img width="960" height="540" alt="Screenshot 2026-07-08 184055" src="https://github.com/user-attachments/assets/254c3d25-e79d-4e6b-9da2-cb883d05a47c" />
<img width="960" height="540" alt="Screenshot 2026-07-08 184035" src="https://github.com/user-attachments/assets/2c75b3b2-1622-419c-8c84-365fbc699d17" />
<img width="960" height="540" alt="Screenshot 2026-07-08 184018" src="https://github.com/user-attachments/assets/f5f6160b-0269-49dd-85a4-152230e0c75d" />

