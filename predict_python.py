import json
import math
import sys
from pathlib import Path


def main():
    technical_score = float(sys.argv[1]) if len(sys.argv) > 1 else 82
    communication_score = float(sys.argv[2]) if len(sys.argv) > 2 else 76

    model_path = Path("artifacts/model-python.json")
    if not model_path.exists():
        raise SystemExit("Run `python train_from_scratch.py` before prediction.")

    model = json.loads(model_path.read_text(encoding="utf-8"))
    raw_features = [technical_score, communication_score]
    scaled_features = [
        (value - model["scaler"]["mean"][index]) / model["scaler"]["std"][index]
        for index, value in enumerate(raw_features)
    ]

    z = sum(
        weight * scaled_features[index]
        for index, weight in enumerate(model["weights"])
    ) + model["bias"]
    probability = 1 / (1 + math.exp(-z))
    decision = "APPROVE" if probability >= model["threshold"] else "REJECT"

    print(
        {
            "technical_score": technical_score,
            "communication_score": communication_score,
            "approve_probability": round(probability, 4),
            "decision": decision,
        }
    )


if __name__ == "__main__":
    main()
