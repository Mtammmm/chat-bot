# Breast Cancer Classification From Scratch

A small, readable machine learning project that trains a binary classifier on the
Breast Cancer Wisconsin Diagnostic dataset.

The goal of this project is educational: it shows how a simple AI model can be
trained from scratch using NumPy, while using scikit-learn only for practical
support tasks such as loading the dataset, splitting data, scaling features, and
calculating evaluation metrics.

> This project is not a medical product and must not be used for real diagnosis.
> It is a learning and demonstration project.

## What This Project Does

The model predicts whether a tumor sample is:

- `malignant`
- `benign`

Each sample contains 30 numeric measurements extracted from cell images, such as
radius, texture, perimeter, area, smoothness, compactness, and related features.

The project includes:

- A training script that builds a logistic regression model from scratch.
- A prediction script that loads the saved model and runs inference.
- A clean terminal output format designed for demos and presentations.
- Saved model artifacts in JSON format.

## Project Structure

```text
.
|-- train_from_scratch.py          # Trains the model
|-- predict_python.py              # Runs prediction using the saved model
|-- requirements.txt               # Python dependencies
|-- artifacts/
|   |-- model-python.json          # Saved model, scaler, config, and metrics
|   `-- training-history-python.json
`-- README.md
```

## How It Works

The training pipeline follows these steps:

1. Load the real Breast Cancer Wisconsin Diagnostic dataset.
2. Split the data into training, validation, and test sets.
3. Standardize the 30 input features using `StandardScaler`.
4. Initialize model weights and bias.
5. Run a logistic regression forward pass:

```text
z = X @ weights + bias
probability = sigmoid(z)
```

6. Calculate binary cross-entropy loss.
7. Compute gradients manually with NumPy.
8. Update weights and bias using gradient descent.
9. Evaluate the model with accuracy, precision, recall, F1 score, and loss.
10. Save the trained model and training history as JSON files.

The model optimization is implemented manually. The project does not call
`LogisticRegression.fit()`.

## Requirements

- Python 3.14+
- NumPy
- scikit-learn

Install dependencies with:

```powershell
python -m pip install -r requirements.txt
```

If you prefer a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run Training

```powershell
python train_from_scratch.py
```

If you are using the local virtual environment:

```powershell
.\.venv\Scripts\python.exe train_from_scratch.py
```

The training output is formatted for readability:

```text
================================================================
                     AI MODEL TRAINING DEMO
================================================================
Task: Predict whether a tumor is malignant or benign
Model: Logistic regression trained from scratch with NumPy
Data: Real Breast Cancer Wisconsin Diagnostic dataset
```

After training, the project saves:

```text
artifacts/model-python.json
artifacts/training-history-python.json
```

## Run Prediction

Predict the first sample in the dataset:

```powershell
python predict_python.py
```

Predict a specific sample by index:

```powershell
python predict_python.py 10
```

Or with the virtual environment:

```powershell
.\.venv\Scripts\python.exe predict_python.py 10
```

Example output:

```text
Prediction
----------
Predicted class       : MALIGNANT
Confidence            : 91.60%
Malignant probability : 91.60%
Benign probability    : 8.40%
```

## Prediction Input Options

`predict_python.py` supports three input modes:

| Command style | Meaning |
| --- | --- |
| `python predict_python.py` | Uses dataset sample `0` |
| `python predict_python.py 10` | Uses dataset sample `10` |
| `python predict_python.py <30 values>` | Uses 30 manual raw feature values |

Manual prediction requires all 30 numeric feature values in the same order as the
Breast Cancer Wisconsin dataset.

## Current Model Performance

Current test-set result:

| Metric | Value |
| --- | ---: |
| Loss | 0.0967 |
| Accuracy | 95.35% |
| Precision | 98.08% |
| Recall | 94.44% |
| F1 Score | 96.23% |

These numbers may change slightly if the training configuration, dependency
versions, or random seed are changed.

## Key Concepts Demonstrated

- Binary classification
- Logistic regression
- Sigmoid activation
- Binary cross-entropy loss
- Manual gradient calculation
- Gradient descent
- Feature scaling
- Train/validation/test split
- Model evaluation metrics
- JSON model export
- Reusable inference from saved artifacts

## Why This Project Is Useful

This repository is useful for learning and showcasing the fundamentals of model
training without hiding the core logic behind a high-level training API.

It keeps the model small enough to understand, while still using a real dataset
and a realistic machine learning workflow.

## Limitations

- This is not a clinical tool.
- The dataset is small compared with real-world medical AI systems.
- The model is a simple logistic regression classifier.
- The prediction output is only for educational demonstration.
- Real diagnosis requires professional medical review and validated systems.

## Troubleshooting

If imports fail in VS Code, make sure the selected Python interpreter matches the
environment where dependencies were installed.

For the local virtual environment, select:

```text
.\.venv\Scripts\python.exe
```

If installation fails, upgrade pip and install again:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## License

No license has been specified for this repository yet.
