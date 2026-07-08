# Battery Health Prediction Platform

Premium Streamlit UI for the existing battery prediction backend.

## Expected backend files

These backend files are included beside `app.py`:

- `predict.py`
- `utils.py`

Add your trained model assets here:

- `models/Best_LSTM_GRU.keras`
- `scaler/scaler.pkl`

Prediction history is written to:

- `results/Prediction_History.csv`

The UI calls the public backend functions directly:

- `predict_capacity()`
- `forecast_capacity()`
- `estimate_remaining_cycles()`
- `calculate_soh()`
- `battery_status()`
- `battery_gauge()`
- `forecast_plot()`
- `save_prediction()`
- `load_prediction_history()`

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```


## Project Structure

```
app.py
predict.py
utils.py
models/
scaler/
results/
```

Ensure the trained model and scaler exist before launching the application.
