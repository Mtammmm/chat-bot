# Slide Outline: Train Một Model AI Từ Đầu Đến Cuối

## Slide 1 - Title

**Train một model AI logic từ đầu đến cuối**

- Bài toán: dự đoán ứng viên phỏng vấn có nên approve hay không
- Model demo: logistic regression train from scratch bằng Python thuần
- Mục tiêu: hiểu pipeline training, không chỉ gọi thư viện

Speaker note:

> Em sẽ trình bày một pipeline nhỏ nhưng đầy đủ: từ dữ liệu, preprocessing, training loop, evaluation đến lưu model để inference.

## Slide 2 - Problem Framing

- Input: `technical_score`, `communication_score`
- Output: `approve = 1` hoặc `reject = 0`
- Loại bài toán: supervised binary classification
- Metric chính: accuracy, precision, recall, F1

Speaker note:

> Trước khi chọn model, cần định nghĩa rõ input, output, label và metric. Nếu bài toán approve ứng viên, precision và recall đều quan trọng vì false positive và false negative đều có chi phí.

## Slide 3 - Dataset

- Demo tự sinh 1,200 sample có seed cố định
- Mỗi sample gồm 2 feature và 1 label
- Label được tạo từ một hidden rule có noise
- Noise giúp bài toán giống thực tế hơn, không thể đạt 100%

Speaker note:

> Trong thực tế dữ liệu đến từ database/log/user behavior. Ở demo này em tự sinh dữ liệu để kiểm soát toàn bộ pipeline và có thể chạy lại ra cùng kết quả.

## Slide 4 - Data Split

- Train: 70%
- Validation: 15%
- Test: 15%
- Train để học parameter
- Validation để theo dõi chất lượng trong quá trình train
- Test để đánh giá cuối cùng

Speaker note:

> Nguyên tắc quan trọng là không để test set ảnh hưởng đến quá trình training hoặc tuning, tránh báo cáo kết quả ảo.

## Slide 5 - Feature Scaling

- Chuẩn hóa bằng z-score
- Công thức: `x_scaled = (x - mean) / std`
- Fit scaler chỉ trên train set
- Apply cùng scaler cho validation/test

Speaker note:

> Nếu fit scaler trên toàn bộ dataset thì validation/test đã rò rỉ thông tin vào training. Đây là lỗi data leakage rất hay gặp.

## Slide 6 - Model Choice

- Logistic regression
- Công thức: `p = sigmoid(w1*x1 + w2*x2 + b)`
- Output là xác suất từ 0 đến 1
- Threshold mặc định: `p >= 0.5` thì approve

Speaker note:

> Dù đơn giản, logistic regression thể hiện đầy đủ logic của nhiều model AI: parameter, forward pass, loss, gradient và update.

## Slide 7 - Forward Pass

- Nhận feature đã scale
- Tính linear score `z = w*x + b`
- Đưa qua sigmoid để ra probability
- So sánh probability với label thật

Speaker note:

> Forward pass là bước model đưa ra dự đoán hiện tại. Ban đầu weights gần random nên dự đoán kém, sau mỗi epoch model sẽ điều chỉnh weights.

## Slide 8 - Loss Function

- Dùng binary cross-entropy
- Phạt mạnh khi model tự tin nhưng sai
- Loss càng thấp nghĩa là xác suất dự đoán càng gần label

Formula:

```text
loss = -[y*log(p) + (1-y)*log(1-p)]
```

Speaker note:

> Loss là tín hiệu để model biết sai bao nhiêu. Với classification, cross-entropy phù hợp hơn MSE vì nó tối ưu xác suất phân lớp.

## Slide 9 - Backward Pass / Gradient

- Gradient cho biết cần đổi weight theo hướng nào
- Với logistic regression: `error = prediction - label`
- `dw = average(error * x)`
- `db = average(error)`

Speaker note:

> Backpropagation ở đây là tính đạo hàm của loss theo từng parameter. Với neural network, ý tưởng vẫn giống vậy nhưng áp dụng qua nhiều layer bằng chain rule.

## Slide 10 - Gradient Descent

- Update parameter sau mỗi epoch
- Công thức: `w = w - learning_rate * dw`
- Learning rate quá lớn: dễ dao động
- Learning rate quá nhỏ: train chậm

Speaker note:

> Đây là phần model thật sự học. Mỗi update làm weight dịch chuyển để giảm loss trên train set.

## Slide 11 - Training Loop

- Lặp qua nhiều epoch
- Mỗi epoch gồm:
- Predict
- Compute loss
- Compute gradient
- Update weights
- Log train/validation metrics

Speaker note:

> Training loop là trái tim của quá trình train model. Trong code demo, toàn bộ loop này được viết thủ công để thấy rõ từng bước.

## Slide 12 - Evaluation

- Accuracy: đúng bao nhiêu phần trăm
- Precision: approve rồi thì đúng bao nhiêu
- Recall: trong các hồ sơ nên approve, bắt được bao nhiêu
- F1: cân bằng precision và recall

Speaker note:

> Không nên chỉ nhìn accuracy. Nếu dataset lệch class, model đoán toàn một class vẫn có accuracy cao nhưng vô dụng.

## Slide 13 - Result

- Chạy `python train_from_scratch.py`
- Nếu PATH chưa đúng, chạy bằng PowerShell:
- `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" train_from_scratch.py`
- Training history được lưu ở `artifacts/training-history-python.json`
- Model cuối được lưu ở `artifacts/model-python.json`
- Kết quả demo hiện tại trên test set:
- Loss: `0.5042`
- Accuracy: `0.7833`
- Precision: `0.7934`
- Recall: `0.8727`
- F1: `0.8312`

Speaker note:

> Phần này em show bảng log loss/accuracy qua các epoch và final test metrics. Nếu validation loss tăng trong khi train loss giảm thì có dấu hiệu overfitting.

## Slide 14 - Inference Flow

- Nhận input mới
- Scale input bằng mean/std đã lưu
- Tính probability bằng weight/bias đã train
- Áp threshold để ra decision
- Có thể điều chỉnh threshold theo business cost
- Python command: `python predict_python.py 82 76`

Speaker note:

> Artifact cần lưu không chỉ weights mà cả preprocessing config. Nếu quên scaler, inference sẽ sai distribution so với training.

## Slide 15 - Common Interview Questions

- Vì sao phải split train/validation/test?
- Vì sao không fit scaler trên toàn bộ data?
- Learning rate ảnh hưởng gì?
- Làm sao biết model overfit?
- Khi nào dùng precision thay vì recall?
- Logistic regression khác neural network ở đâu?

Speaker note:

> Với mỗi câu, nên trả lời bằng trade-off và liên hệ trực tiếp đến pipeline vừa trình bày.

## Slide 16 - Next Step

- Thay logistic regression bằng neural network 1 hidden layer
- Dùng real dataset thay synthetic dataset
- Thêm confusion matrix và ROC-AUC
- Thêm model versioning và monitoring sau deploy

Speaker note:

> Sau khi nắm pipeline cơ bản, các model phức tạp hơn chủ yếu thay đổi kiến trúc và cách tối ưu, còn tư duy train/evaluate/deploy vẫn giống nhau.
