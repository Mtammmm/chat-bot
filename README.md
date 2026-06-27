# Train AI Model From Scratch - Python Interview Demo

Demo nay train mot model AI tu dau den cuoi bang Python tren du lieu that co san trong scikit-learn: Breast Cancer Wisconsin Diagnostic.

Script dung:

- `numpy` cho vectorized math
- `scikit-learn` cho load dataset, split data, feature scaling va metrics
- training loop va gradient descent tu viet, khong dung `LogisticRegression.fit()`

## Files

- `train_from_scratch.py`: train logistic regression bang NumPy gradient descent
- `predict_python.py`: inference bang model da train
- `requirements.txt`: dependencies
- `SLIDE_OUTLINE.md`: goi y noi dung tung slide

## Problem

Binary classification tren dataset Breast Cancer Wisconsin Diagnostic:

- Input: 30 numeric features tu anh chup te bao, vi du `mean radius`, `mean texture`, `worst area`
- Output: `malignant` hoac `benign`
- Positive class trong sklearn dataset la `benign`

Pipeline:

1. Load du lieu that bang `load_breast_cancer()`
2. Chia train/validation/test
3. Chuan hoa feature bang `StandardScaler`
4. Forward pass: `p = sigmoid(X @ w + b)`
5. Tinh binary cross-entropy loss
6. Tinh gradient bang NumPy
7. Cap nhat weights bang gradient descent
8. Danh gia bang accuracy, precision, recall, F1
9. Luu model artifact

## Demo

Tren may hien tai, `python` trong PATH van dang tro toi WindowsApps alias. Python that dang nam o:

```text
C:\Users\GF66 KATANA\AppData\Local\Programs\Python\Python311\python.exe
```

Chay bang PowerShell:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" train_from_scratch.py
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" predict_python.py
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" predict_python.py 10
```

Sau khi sua PATH hoac tat App Execution Alias cua Windows:

```bash
python train_from_scratch.py
python predict_python.py
python predict_python.py 10
```

`predict_python.py` co 3 cach dung:

- Khong truyen argument: predict sample 0 trong dataset that
- Truyen 1 so: predict sample theo index, vi du `10`
- Truyen du 30 gia tri: predict manual raw feature values

Ket qua duoc luu vao:

- `artifacts/model-python.json`
- `artifacts/training-history-python.json`

Ket qua hien tai tren test set:

- Loss: `0.0967`
- Accuracy: `0.9535`
- Precision: `0.9808`
- Recall: `0.9444`
- F1: `0.9623`



- Khong train tren test set.
- Fit scaler chi tren train set de tranh data leakage.
- Validation dung de quan sat overfitting va chon hyperparameter.
- Test chi dung mot lan cuoi de bao cao chat luong.
- Recall quan trong trong bai toan y te vi bo sot case positive/negative co chi phi cao, tuy can dinh nghia positive class ro rang.
