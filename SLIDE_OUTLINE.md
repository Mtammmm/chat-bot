# Slide Outline: Train Mot Model AI Tu Dau Den Cuoi

## Slide 1 - Title

**Train mot model AI logic tu dau den cuoi**

- Dataset that: Breast Cancer Wisconsin Diagnostic
- Model demo: logistic regression train bang Python, NumPy va scikit-learn
- Muc tieu: hieu pipeline training, khong chi goi ham `.fit()`

Speaker note:

> Em se trinh bay mot pipeline nho nhung day du: load du lieu that, preprocessing, training loop, evaluation va luu model de inference.

## Slide 2 - Problem Framing

- Input: 30 numeric cell features
- Output: `malignant` hoac `benign`
- Loai bai toan: supervised binary classification
- Metric: accuracy, precision, recall, F1

Speaker note:

> Truoc khi chon model, can dinh nghia ro input, output, label va metric. Voi bai toan y te, precision va recall can duoc giai thich theo chi phi sai lam.

## Slide 3 - Real Dataset

- Dung `sklearn.datasets.load_breast_cancer`
- 569 samples
- 30 features
- 2 classes: malignant va benign
- Khong sinh du lieu gia

Speaker note:

> Dataset nay la dataset that duoc dong goi san trong scikit-learn, nen demo co the chay offline ma khong can download.

## Slide 4 - Data Split

- Train: 70%
- Validation: 15%
- Test: 15%
- Dung stratified split de giu ty le class
- Test set khong duoc dung trong training/tuning

Speaker note:

> Nguyen tac quan trong la khong de test set anh huong den training hoac hyperparameter tuning, tranh bao cao ket qua ao.

## Slide 5 - Feature Scaling

- Chuan hoa bang `StandardScaler`
- Cong thuc: `x_scaled = (x - mean) / std`
- Fit scaler chi tren train set
- Apply cung scaler cho validation/test

Speaker note:

> Neu fit scaler tren toan bo dataset thi validation/test da ro ri thong tin vao training. Day la loi data leakage hay gap.

## Slide 6 - Model Choice

- Logistic regression
- Cong thuc: `p = sigmoid(X @ w + b)`
- Output la xac suat class `benign`
- Threshold mac dinh: `p >= 0.5`

Speaker note:

> Logistic regression don gian nhung co day du cac thanh phan cua training: parameters, forward pass, loss, gradient va update.

## Slide 7 - Forward Pass

- Nhan feature da scale
- Tinh linear score `z = X @ w + b`
- Dua qua sigmoid de ra probability
- So sanh probability voi label that

Speaker note:

> Forward pass la buoc model dua ra du doan hien tai. Ban dau weights gan random nen du doan kem, sau moi epoch model dieu chinh weights.

## Slide 8 - Loss Function

- Dung binary cross-entropy
- Phat manh khi model tu tin nhung sai
- Loss cang thap nghia la xac suat du doan cang gan label
- Code dung NumPy de tinh loss tren batch

Formula:

```text
loss = -mean(y*log(p) + (1-y)*log(1-p))
```

Speaker note:

> Voi classification, cross-entropy phu hop vi no toi uu xac suat phan lop.

## Slide 9 - Backward Pass / Gradient

- Gradient cho biet can doi weight theo huong nao
- `error = prediction - label`
- `dw = X.T @ error / n`
- `db = mean(error)`

Speaker note:

> Backpropagation o day la tinh dao ham loss theo tung parameter. Voi neural network, y tuong van giong vay nhung ap dung qua nhieu layer bang chain rule.

## Slide 10 - Gradient Descent

- Update parameter sau moi epoch
- Cong thuc: `w = w - learning_rate * dw`
- Learning rate qua lon: de dao dong
- Learning rate qua nho: train cham

Speaker note:

> Day la phan model that su hoc. Moi update lam weight dich chuyen de giam loss tren train set.

## Slide 11 - Training Loop

- Lap qua nhieu epoch
- Predict
- Compute loss
- Compute gradient
- Update weights
- Log train/validation metrics

Speaker note:

> Training loop la trai tim cua qua trinh train model. Trong code demo, loop nay duoc viet thu cong bang NumPy.

## Slide 12 - Evaluation

- Accuracy: dung bao nhieu phan tram
- Precision: du doan benign thi dung bao nhieu
- Recall: trong cac benign that, bat duoc bao nhieu
- F1: can bang precision va recall

Speaker note:

> Khong nen chi nhin accuracy. Can giai thich metric theo positive class va chi phi cua false positive/false negative.

## Slide 13 - Result

- Chay `python train_from_scratch.py`
- Neu PATH chua dung:
- `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" train_from_scratch.py`
- Training history: `artifacts/training-history-python.json`
- Model artifact: `artifacts/model-python.json`
- Test loss: `0.0967`
- Test accuracy: `0.9535`
- Test precision: `0.9808`
- Test recall: `0.9444`
- Test F1: `0.9623`

Speaker note:

> Phan nay show bang log loss/accuracy qua cac epoch va final test metrics. Neu validation loss tang trong khi train loss giam thi co dau hieu overfitting.

## Slide 14 - Inference Flow

- Load `model-python.json`
- Lay raw feature tu sample that hoac input moi
- Scale input bang mean/std da luu
- Tinh probability bang weights/bias
- Ap threshold de ra class
- Command: `python predict_python.py 10`

Speaker note:

> Artifact can luu khong chi weights ma ca preprocessing config. Neu quen scaler, inference se sai distribution so voi training.

## Slide 15 - Common Interview Questions

- Vi sao phai split train/validation/test?
- Vi sao khong fit scaler tren toan bo data?
- Learning rate anh huong gi?
- Lam sao biet model overfit?
- Khi nao uu tien precision thay vi recall?
- Logistic regression khac neural network o dau?

Speaker note:

> Voi moi cau, nen tra loi bang trade-off va lien he truc tiep den pipeline vua trinh bay.

## Slide 16 - Next Step

- Doi logistic regression sang neural network 1 hidden layer
- Them confusion matrix va ROC-AUC
- Them cross-validation
- Them model versioning va monitoring sau deploy

Speaker note:

> Sau khi nam pipeline co ban, cac model phuc tap hon chu yeu thay doi kien truc va cach toi uu, con tu duy train/evaluate/deploy van giong nhau.
