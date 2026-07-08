import pickle
from functools import lru_cache
from pathlib import Path

import numpy as np
import keras
import sys
import keras
import tensorflow as tf

print("=" * 60)
print("Python:", sys.executable)
print("TensorFlow:", tf.__version__)
print("Keras:", keras.__version__)
print("Keras location:", keras.__file__)
print("=" * 60)

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR.parent / "models" / "Best_LSTM_GRU.keras"
SCALER_PATH = BASE_DIR.parent / "scaler" / "scaler.pkl"

WINDOW_SIZE = 10
print("MODEL PATH :", MODEL_PATH)
print("MODEL EXISTS:", MODEL_PATH.exists())

print("SCALER PATH :", SCALER_PATH)
print("SCALER EXISTS:", SCALER_PATH.exists())


@lru_cache(maxsize=1)
def load_prediction_model():
    import sys
    import tensorflow as tf
    import keras

    print("=" * 60)
    print("Python:", sys.executable)
    print("TensorFlow:", tf.__version__)
    print("Keras:", keras.__version__)
    print("Keras path:", keras.__file__)
    print("tf.keras:", tf.keras.__file__)
    print("=" * 60)

    model = keras.models.load_model(MODEL_PATH, compile=False)

    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler


def validate_input(capacities):
    if not isinstance(capacities, (list, tuple, np.ndarray)):
        raise TypeError("Input must be a list of capacities.")

    if len(capacities) != WINDOW_SIZE:
        raise ValueError(f"Exactly {WINDOW_SIZE} capacity values are required.")

    capacities = np.array(capacities, dtype=np.float32)

    if np.any(np.isnan(capacities)):
        raise ValueError("Input contains NaN values.")

    if np.any(capacities <= 0):
        raise ValueError("Capacity values must be positive.")

    return capacities


def preprocess_input(capacities):
    _, scaler = load_prediction_model()
    capacities = capacities.reshape(-1, 1)
    scaled = scaler.transform(capacities)
    return scaled.reshape(1, WINDOW_SIZE, 1)


def predict_capacity(capacities):
    capacities = validate_input(capacities)
    model, scaler = load_prediction_model()  # cached
    x = preprocess_input(capacities)
    prediction = model.predict(x, verbose=0)
    prediction = scaler.inverse_transform(prediction)
    return float(prediction[0][0])


def forecast_capacity(capacities, steps=10):
    capacities = validate_input(capacities)
    history = list(capacities)
    predictions = []

    for _ in range(steps):
        pred = predict_capacity(history[-WINDOW_SIZE:])
        predictions.append(pred)
        history.append(pred)

    return predictions


def generate_curve(capacities, steps=20):
    future = forecast_capacity(capacities, steps)
    return list(capacities) + future


def estimate_remaining_cycles(capacities, rated_capacity, threshold=80, max_cycles=500):
    history = list(capacities)
    current_cycle = 0

    while current_cycle < max_cycles:
        pred = predict_capacity(history[-WINDOW_SIZE:])
        history.append(pred)
        soh = (pred / rated_capacity) * 100

        if soh <= threshold:
            return current_cycle + 1

        current_cycle += 1

    return f">{max_cycles}"


def model_information():
    return {
        "Model": "Tuned LSTM+GRU",
        "Window Size": WINDOW_SIZE,
        "Framework": "TensorFlow",
        "Input Shape": "(10,1)",
    }


if __name__ == "__main__":
    sample = [527, 526, 526, 525, 525, 524, 524, 523, 523, 522]
    prediction = predict_capacity(sample)
    print(f"Next Capacity: {prediction:.3f}")
    print("Forecast:", np.round(forecast_capacity(sample, steps=10), 3))
    print("Estimated Remaining Cycles:", estimate_remaining_cycles(sample, rated_capacity=530))
