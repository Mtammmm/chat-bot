import json
import math
import sys
from pathlib import Path

from sklearn.datasets import load_breast_cancer


def main():
    model_path = Path("artifacts/model-python.json")
    if not model_path.exists():
        raise SystemExit("Run `python train_from_scratch.py` before prediction.")

    model = json.loads(model_path.read_text(encoding="utf-8"))
    raw_features, source = read_input_features(model)
    scaled_features = [
        (value - model["scaler"]["mean"][index]) / model["scaler"]["std"][index]
        for index, value in enumerate(raw_features)
    ]

    z = sum(
        weight * scaled_features[index]
        for index, weight in enumerate(model["weights"])
    ) + model["bias"]
    probability = 1 / (1 + math.exp(-z))
    prediction = 1 if probability >= model["threshold"] else 0
    decision = model["dataset"]["target_names"][prediction]

    print(
        {
            "input_source": source,
            "benign_probability": round(probability, 4),
            "prediction": decision,
        }
    )


def read_input_features(model):
    dataset = load_breast_cancer()
    expected_feature_count = len(model["features"])
    args = sys.argv[1:]

    if not args:
        sample_index = 0
        return dataset.data[sample_index].astype(float).tolist(), f"dataset sample {sample_index}"

    if len(args) == 1:
        sample_index = int(args[0])
        if sample_index < 0 or sample_index >= len(dataset.data):
            raise SystemExit(f"Sample index must be from 0 to {len(dataset.data) - 1}.")
        return dataset.data[sample_index].astype(float).tolist(), f"dataset sample {sample_index}"

    if len(args) != expected_feature_count:
        raise SystemExit(
            f"Expected either 0 args, 1 sample index, or {expected_feature_count} raw feature values."
        )

    return [float(value) for value in args], "manual raw feature values"


if __name__ == "__main__":
    main()
