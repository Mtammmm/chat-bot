# Train AI Model From Scratch - Interview Demo Python

Demo này train một model AI cơ bản từ đầu đến cuối bằng Python thuần, không dùng NumPy, scikit-learn hoặc thư viện ML.

- `train_from_scratch.py`
- `predict_python.py`

## Bài toán

Binary classification: dự đoán một hồ sơ ứng viên phỏng vấn nên được approve hay không dựa trên:

- `technical_score`: điểm kỹ thuật 0-100
- `communication_score`: điểm giao tiếp 0-100

Model dùng logistic regression vì dễ giải thích rõ pipeline:

1. Tạo dữ liệu
2. Chia train/validation/test
3. Chuẩn hóa feature
4. Forward pass
5. Tính binary cross-entropy loss
6. Backpropagation/gradient
7. Gradient descent update
8. Đánh giá model
9. Lưu model artifact

## Chạy demo

Trên máy hiện tại, `python` trong PATH vẫn đang trỏ tới WindowsApps alias. Python thật đang nằm ở:

```text
C:\Users\GF66 KATANA\AppData\Local\Programs\Python\Python311\python.exe
```

Chạy bằng PowerShell:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" train_from_scratch.py
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" predict_python.py 82 76
```

Sau khi sửa PATH hoặc tắt App Execution Alias của Windows, có thể chạy ngắn gọn:

```bash
python train_from_scratch.py
python predict_python.py 82 76
```

Kết quả được lưu vào:

- `artifacts/model-python.json`
- `artifacts/training-history-python.json`

## Cách nói trong phỏng vấn

Bạn có thể nói ngắn gọn:

> Em chọn logistic regression để minh họa cách train model từ đầu vì nó có đầy đủ các thành phần của training loop: dữ liệu, feature scaling, forward pass, loss function, gradient, update parameters, validation và test. Sau khi hiểu pipeline này, cùng tư duy đó có thể mở rộng sang neural network nhiều layer.

Điểm cần nhấn mạnh:

- Không train trên test set.
- Validation dùng để quan sát overfitting và chọn hyperparameter.
- Test chỉ dùng một lần cuối để báo cáo chất lượng.
- Feature scaling giúp gradient descent ổn định hơn.
- Loss giảm chưa đủ, cần xem accuracy/precision/recall/F1 theo mục tiêu business.
