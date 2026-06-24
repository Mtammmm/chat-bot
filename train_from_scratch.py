import json
import math
import random
from pathlib import Path


CONFIG = {
    "samples": 1200,
    "train_ratio": 0.7,
    "validation_ratio": 0.15,
    "learning_rate": 0.08,
    "epochs": 900,
    "log_every": 100,
    "seed": 42,
}


def main():
    rng = random.Random(CONFIG["seed"])
    data = make_dataset(CONFIG["samples"], rng)
    rng.shuffle(data)

    splits = split_dataset(data, CONFIG["train_ratio"], CONFIG["validation_ratio"])
    scaler = fit_standard_scaler([row["x"] for row in splits["train"]])

    for split in splits.values():
        for row in split:
            row["x"] = transform(scaler, row["x"])

    model = {
        "weights": [random_normal(rng) * 0.01 for _ in range(2)],
        "bias": 0.0,
    }

    history = []

    for epoch in range(1, CONFIG["epochs"] + 1):
        gradients = compute_gradients(model, splits["train"])

        model["weights"] = [
            weight - CONFIG["learning_rate"] * gradients["weights"][index]
            for index, weight in enumerate(model["weights"])
        ]
        model["bias"] -= CONFIG["learning_rate"] * gradients["bias"]

        if epoch == 1 or epoch % CONFIG["log_every"] == 0 or epoch == CONFIG["epochs"]:
            train_metrics = evaluate(model, splits["train"])
            val_metrics = evaluate(model, splits["validation"])
            history.append(
                {
                    "epoch": epoch,
                    "train_loss": round(train_metrics["loss"], 4),
                    "train_accuracy": round(train_metrics["accuracy"], 4),
                    "validation_loss": round(val_metrics["loss"], 4),
                    "validation_accuracy": round(val_metrics["accuracy"], 4),
                }
            )

    final_metrics = {
        "train": compact_metrics(evaluate(model, splits["train"])),
        "validation": compact_metrics(evaluate(model, splits["validation"])),
        "test": compact_metrics(evaluate(model, splits["test"])),
    }

    exported_model = {
        "task": "Binary classification: should approve an interview candidate profile?",
        "algorithm": "Logistic regression trained from scratch with gradient descent",
        "features": ["technical_score_standardized", "communication_score_standardized"],
        "original_feature_meaning": {
            "technical_score": "0-100 synthetic technical interview score",
            "communication_score": "0-100 synthetic communication score",
        },
        "scaler": scaler,
        "weights": model["weights"],
        "bias": model["bias"],
        "threshold": 0.5,
        "metrics": final_metrics,
        "training_config": CONFIG,
    }

    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)
    (artifacts_dir / "model-python.json").write_text(
        json.dumps(exported_model, indent=2) + "\n",
        encoding="utf-8",
    )
    (artifacts_dir / "training-history-python.json").write_text(
        json.dumps(history, indent=2) + "\n",
        encoding="utf-8",
    )

    print("Training checkpoints")
    print_table(history)
    print("\nFinal test metrics")
    print_table([final_metrics["test"]])
    print("\nSaved artifacts/model-python.json and artifacts/training-history-python.json")


def make_dataset(size, rng):
    rows = []

    for _ in range(size):
        technical = clamp(55 + random_normal(rng) * 18, 0, 100)
        communication = clamp(52 + random_normal(rng) * 20, 0, 100)

        hidden_score = (
            -7.2
            + 0.085 * technical
            + 0.06 * communication
            + 0.75 * math.sin((technical - communication) / 25)
        )

        probability = sigmoid(hidden_score)
        label = 1 if rng.random() < probability else 0
        rows.append({"x": [technical, communication], "y": label})

    return rows


def compute_gradients(model, data):
    gradient_weights = [0.0 for _ in model["weights"]]
    gradient_bias = 0.0

    for row in data:
        prediction = predict_probability(model, row["x"])
        error = prediction - row["y"]

        for index in range(len(gradient_weights)):
            gradient_weights[index] += error * row["x"][index]
        gradient_bias += error

    return {
        "weights": [value / len(data) for value in gradient_weights],
        "bias": gradient_bias / len(data),
    }


def evaluate(model, data):
    total_loss = 0.0
    correct = 0
    true_positive = 0
    false_positive = 0
    false_negative = 0

    for row in data:
        probability = predict_probability(model, row["x"])
        prediction = 1 if probability >= 0.5 else 0

        total_loss += binary_cross_entropy(row["y"], probability)
        correct += 1 if prediction == row["y"] else 0
        true_positive += 1 if prediction == 1 and row["y"] == 1 else 0
        false_positive += 1 if prediction == 1 and row["y"] == 0 else 0
        false_negative += 1 if prediction == 0 and row["y"] == 1 else 0

    precision = true_positive / max(true_positive + false_positive, 1)
    recall = true_positive / max(true_positive + false_negative, 1)
    f1 = (2 * precision * recall) / max(precision + recall, 1e-15)

    return {
        "loss": total_loss / len(data),
        "accuracy": correct / len(data),
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def predict_probability(model, features):
    z = dot(model["weights"], features) + model["bias"]
    return sigmoid(z)


def binary_cross_entropy(label, probability):
    clipped = min(max(probability, 1e-15), 1 - 1e-15)
    return -(label * math.log(clipped) + (1 - label) * math.log(1 - clipped))


def fit_standard_scaler(rows):
    feature_count = len(rows[0])
    mean = [sum(row[index] for row in rows) / len(rows) for index in range(feature_count)]
    std = []

    for index in range(feature_count):
        variance = sum((row[index] - mean[index]) ** 2 for row in rows) / len(rows)
        std.append(math.sqrt(variance) or 1)

    return {"mean": mean, "std": std}


def transform(scaler, row):
    return [
        (value - scaler["mean"][index]) / scaler["std"][index]
        for index, value in enumerate(row)
    ]


def split_dataset(rows, train_ratio, validation_ratio):
    train_end = int(len(rows) * train_ratio)
    validation_end = train_end + int(len(rows) * validation_ratio)

    return {
        "train": rows[:train_end],
        "validation": rows[train_end:validation_end],
        "test": rows[validation_end:],
    }


def compact_metrics(metrics):
    return {key: round(value, 4) for key, value in metrics.items()}


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


def dot(left, right):
    return sum(value * right[index] for index, value in enumerate(left))


def sigmoid(value):
    return 1 / (1 + math.exp(-value))


def clamp(value, minimum, maximum):
    return min(max(value, minimum), maximum)


def random_normal(rng):
    u1 = max(rng.random(), 1e-15)
    u2 = max(rng.random(), 1e-15)
    return math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)


if __name__ == "__main__":
    main()
