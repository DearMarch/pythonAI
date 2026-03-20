from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolov8n.pt")

# 执行目标检测并保存结果（置信度阈值设置为 0.5）
results = model("data/result.jpg", save=True, project="output", name="result", conf=0.5)