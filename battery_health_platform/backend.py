from __future__ import annotations

from importlib import import_module
from typing import Any


class BackendUnavailable(RuntimeError):
    pass


from importlib import import_module
import traceback


def _load_symbol(module_name: str, symbol: str):
    try:
        module = import_module(module_name)
        print("Imported:", module.__file__)
    except Exception as exc:
        print("=" * 80)
        traceback.print_exc()
        print("=" * 80)
        raise

    return getattr(module, symbol)


def predict_capacity(capacities: list[float]) -> float:
    return _load_symbol("predict", "predict_capacity")(capacities)


def forecast_capacity(capacities: list[float], steps: int = 10) -> list[float]:
    return _load_symbol("predict", "forecast_capacity")(capacities, steps=steps)


def estimate_remaining_cycles(
    capacities: list[float],
    rated_capacity: float,
    threshold: float = 80,
    max_cycles: int = 500,
) -> int | None:
    return _load_symbol("predict", "estimate_remaining_cycles")(
        capacities,
        rated_capacity=rated_capacity,
        threshold=threshold,
        max_cycles=max_cycles,
    )


def model_information() -> dict[str, Any]:
    return _load_symbol("predict", "model_information")()


def calculate_soh(capacity: float) -> float:
    return _load_symbol("utils", "calculate_soh")(capacity)


def battery_status(soh: float) -> str:
    return _load_symbol("utils", "battery_status")(soh)


def rul_status(cycles: int | None) -> str:
    return _load_symbol("utils", "rul_status")(cycles)


def battery_gauge(soh: float) -> Any:
    return _load_symbol("utils", "battery_gauge")(soh)


def forecast_plot(history: list[float], forecast: list[float]) -> Any:
    return _load_symbol("utils", "forecast_plot")(history, forecast)


def save_prediction(predicted_capacity: float, soh: float, rul: int | None, horizon: int) -> None:
    return _load_symbol("utils", "save_prediction")(predicted_capacity, soh, rul, horizon)


def load_prediction_history() -> Any:
    return _load_symbol("utils", "load_prediction_history")()


def clear_history() -> None:
    return _load_symbol("utils", "clear_history")()


def export_history() -> bytes:
    return _load_symbol("utils", "export_history")()


def model_metrics() -> dict[str, Any]:
    return _load_symbol("utils", "model_metrics")()


def project_information() -> dict[str, Any]:
    return _load_symbol("utils", "project_information")()
