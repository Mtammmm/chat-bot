import json
from pathlib import Path

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


CONFIG = {
    "test_ratio": 0.15,
    "validation_ratio": 0.15,
    "learning_rate": 0.08,
    "epochs": 900,
    "log_every": 100,
    "seed": 42,
}


def main():
    dataset = load_real_dataset()
    features = dataset["features"]
    labels = dataset["labels"]

    x_train_val, x_test, y_train_val, y_test = train_test_split(
        features,
        labels,
        test_size=CONFIG["test_ratio"],
        random_state=CONFIG["seed"],
        stratify=labels,
    )

    validation_size = CONFIG["validation_ratio"] / (1 - CONFIG["test_ratio"])
    x_train, x_validation, y_train, y_validation = train_test_split(
        x_train_val,
        y_train_val,
        test_size=validation_size,
        random_state=CONFIG["seed"],
        stratify=y_train_val,
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_validation = scaler.transform(x_validation)
    x_test = scaler.transform(x_test)

    rng = np.random.default_rng(CONFIG["seed"])
    model = {
        "weights": rng.normal(loc=0.0, scale=0.01, size=x_train.shape[1]),
        "bias": 0.0,
    }

    history = []

    for epoch in range(1, CONFIG["epochs"] + 1):
        probabilities = predict_probability(model, x_train)
        error = probabilities - y_train

        gradient_weights = x_train.T @ error / len(x_train)
        gradient_bias = float(np.mean(error))

        model["weights"] -= CONFIG["learning_rate"] * gradient_weights
        model["bias"] -= CONFIG["learning_rate"] * gradient_bias

        if epoch == 1 or epoch % CONFIG["log_every"] == 0 or epoch == CONFIG["epochs"]:
            train_metrics = evaluate(model, x_train, y_train)
            validation_metrics = evaluate(model, x_validation, y_validation)
            history.append(
                {
                    "epoch": epoch,
                    "train_loss": round(train_metrics["loss"], 4),
                    "train_accuracy": round(train_metrics["accuracy"], 4),
                    "validation_loss": round(validation_metrics["loss"], 4),
                    "validation_accuracy": round(validation_metrics["accuracy"], 4),
                }
            )

    final_metrics = {
        "train": compact_metrics(evaluate(model, x_train, y_train)),
        "validation": compact_metrics(evaluate(model, x_validation, y_validation)),
        "test": compact_metrics(evaluate(model, x_test, y_test)),
    }

    exported_model = {
        "task": "Binary classification on the real Breast Cancer Wisconsin dataset",
        "dataset": {
            "name": dataset["name"],
            "source": "sklearn.datasets.load_breast_cancer",
            "sample_count": int(features.shape[0]),
            "feature_count": int(features.shape[1]),
            "target_names": dataset["target_names"],
            "positive_class": "benign",
        },
        "algorithm": "Logistic regression trained with NumPy gradient descent",
        "features": dataset["feature_names"],
        "scaler": {
            "mean": scaler.mean_.tolist(),
            "std": scaler.scale_.tolist(),
        },
        "weights": model["weights"].tolist(),
        "bias": model["bias"],
        "threshold": 0.5,
        "metrics": final_metrics,
        "training_config": CONFIG,
        "libraries": {
            "numpy": np.__version__,
            "scikit_learn": "used for dataset loading, split, scaling, and metrics; model optimization is manual",
        },
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

    print("Dataset")
    print_table(
        [
            {
                "name": dataset["name"],
                "samples": features.shape[0],
                "features": features.shape[1],
                "target_0": dataset["target_names"][0],
                "target_1": dataset["target_names"][1],
            }
        ]
    )
    print("\nTraining checkpoints")
    print_table(history)
    print("\nFinal test metrics")
    print_table([final_metrics["test"]])
    print("\nSaved artifacts/model-python.json and artifacts/training-history-python.json")


def load_real_dataset():
    data = load_breast_cancer()
    return {
        "name": "Breast Cancer Wisconsin Diagnostic",
        "features": data.data.astype(float),
        "labels": data.target.astype(int),
        "feature_names": data.feature_names.tolist(),
        "target_names": data.target_names.tolist(),
    }


def predict_probability(model, features):
    z = features @ model["weights"] + model["bias"]
    return sigmoid(z)


def evaluate(model, features, labels):
    probabilities = predict_probability(model, features)
    predictions = (probabilities >= 0.5).astype(int)

    return {
        "loss": binary_cross_entropy(labels, probabilities),
        "accuracy": accuracy_score(labels, predictions),
        "precision": precision_score(labels, predictions, zero_division=0),
        "recall": recall_score(labels, predictions, zero_division=0),
        "f1": f1_score(labels, predictions, zero_division=0),
    }


def binary_cross_entropy(labels, probabilities):
    clipped = np.clip(probabilities, 1e-15, 1 - 1e-15)
    return float(-np.mean(labels * np.log(clipped) + (1 - labels) * np.log(1 - clipped)))


def sigmoid(values):
    return 1 / (1 + np.exp(-values))


def compact_metrics(metrics):
    return {key: round(float(value), 4) for key, value in metrics.items()}


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
