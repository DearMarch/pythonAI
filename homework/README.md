# YOLO目标检测最小闭环

## 项目简介

本项目基于Ultralytics YOLOv8模型，实现了对图像的目标检测功能。通过预训练模型`yolov8n.pt`对输入图像进行检测，输出包含目标类别、位置和置信度的检测结果。

## 环境配置

### 软件要求

- Python 3.10+
- PyCharm（推荐IDE）

### Python依赖

```bash
pip install ultralytics
```

## 项目结构

```
homework/
├── README.md (3.7KB)
├── data/
│   └── test.jpg (134.2KB)
├── runs/
│   └── detect/
│       └── output/
│           └── result.jpg (357.3KB)
├── run_yolo.py (0.2KB)
└── yolov8n.pt (6396.3KB)

```

## 使用步骤

### 1. 安装依赖

```bash
pip install ultralytics
```

### 2. 准备测试图像

将待检测图像放入`data/`目录，命名为`test.jpg`。

### 3. 运行检测

```bash
python run_yolo.py
```

### 4. 查看结果

检测结果保存在`output/result.jpg`。

## 核心代码

```python
from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolov8n.pt")

# 执行目标检测并保存结果
results = model("data/result.jpg", save=True, project="output", name="result")
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `model` | 模型文件路径 | `yolov8n.pt` |
| `source` | 输入图像路径 | `data/test.jpg` |
| `save` | 是否保存结果 | `True` |
| `project` | 输出项目目录 | `output` |
| `name` | 输出结果名称 | `result` |

## 检测结果

### 输入图像

`data/test.jpg` - 包含人物、车辆、交通设施等目标的街道场景图像。

### 输出结果

`output/result.jpg` - 检测结果可视化图像，包含边界框和类别标签。

### 检测到的目标类别与数量

| 类别 | 数量 | 说明 |
|------|------|------|
| person（人物） | 5 | 检测到5个人体目标 |
| bus（公交车） | 1 | 检测到1辆公交车 |

## 误差分析与改进建议

### 1. 误检现象

**现象描述**：将路边指示牌误检为交通灯

**原因分析**：指示牌与交通灯在颜色和形状上有相似性，模型可能将圆形红色指示牌误判为交通灯。

**改进建议**：
- 提高置信度阈值（从0.25调整到0.5），减少低置信度误检
- 使用更多交通场景数据进行模型微调
- 考虑使用专门针对交通场景优化的高版本模型

### 2. 漏检现象

**现象描述**：远处的行人未被检测到

**原因分析**：远处行人目标尺度较小，在图像中像素占比较小，模型对小目标的检测能力有限。

**改进建议**：
- 使用更高分辨率的输入图像
- 采用多尺度检测策略
- 使用更大版本的YOLO模型（如yolov8m.pt）提升小目标检测能力
- 考虑在检测流程中加入图像金字塔处理

### 3. 其他改进方向

- **数据增强**：添加模糊、亮度变化等数据增强提升模型鲁棒性
- **模型选择**：根据精度/速度需求选择合适的模型版本（n/s/m/l/x）
- **后处理优化**：调整NMS阈值优化重叠目标的检测效果

## 模型信息

- **模型名称**：YOLOv8n（nano版本，轻量级）
- **预训练数据集**：COCO数据集（80个类别）
- **模型特点**：速度快、参数量小，适合实时应用和快速原型开发

## 许可证

本项目仅供学习研究使用。

## 参考资料

- [Ultralytics YOLOv8官方文档](https://docs.ultralytics.com/)
- [YOLOv8 GitHub仓库](https://github.com/ultralytics/ultralytics)