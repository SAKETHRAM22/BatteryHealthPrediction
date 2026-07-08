import keras
from pathlib import Path

MODEL = Path("models") / "Best_LSTM_GRU.keras"

print("Keras:", keras.__version__)
print("Model:", MODEL.resolve())

model = keras.models.load_model(MODEL, compile=False)

print("SUCCESS!")