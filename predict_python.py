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

    print_prediction_report(model, source, raw_features, probability, decision)


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


def print_prediction_report(model, source, raw_features, benign_probability, decision):
    malignant_probability = 1 - benign_probability
    confidence = max(benign_probability, malignant_probability)

    print_banner("AI MODEL INFERENCE DEMO")
    print("Task: Predict whether a tumor is malignant or benign\n")

    print_section("Input")
    print_key_values(
        [
            ("Source", source),
            ("Feature count", len(raw_features)),
            ("Model artifact", "artifacts/model-python.json"),
        ]
    )

    print_section("Feature Preview")
    preview_rows = [
        {
            "feature": feature_name,
            "value": round(raw_features[index], 4),
        }
        for index, feature_name in enumerate(model["features"][:8])
    ]
    print_table(preview_rows)
    print(f"... {len(raw_features) - len(preview_rows)} more features used by the model")

    print_section("Prediction")
    print_key_values(
        [
            ("Predicted class", decision.upper()),
            ("Confidence", format_percent(confidence)),
            ("Malignant probability", format_percent(malignant_probability)),
            ("Benign probability", format_percent(benign_probability)),
        ]
    )

    print_section("Interpretation")
    if decision == "benign":
        print("The model leans toward BENIGN for this input sample.")
    else:
        print("The model leans toward MALIGNANT for this input sample.")


def print_banner(title):
    line = "=" * 64
    print(line)
    print(title.center(64))
    print(line)


def print_section(title):
    print(f"\n{title}")
    print("-" * len(title))


def print_key_values(rows):
    width = max(len(str(key)) for key, _ in rows)
    for key, value in rows:
        print(f"{str(key).ljust(width)} : {value}")


def format_percent(value):
    return f"{value * 100:.2f}%"


def print_table(rows):
    if not rows:
        return

    columns = list(rows[0].keys())
    widths = {
        column: max(len(column), *(len(str(row[column])) for row in rows))
        for column in columns
    }
    header = " | ".join(column.ljust(widths[column]) for column in columns)
    divider = "-+-".join("-" * widths[column] for column in columns)

    print(header)
    print(divider)
    for row in rows:
        print(" | ".join(str(row[column]).ljust(widths[column]) for column in columns))


if __name__ == "__main__":
    main()
