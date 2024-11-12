from torch.nn.functional import dropout
from ultralytics import YOLO
from ray import tune

# ray.init(address="ray://127.0.0.1:10001")

# Load a YOLOv8n model
model = YOLO("yolo11n.pt")
model.to("cpu")
# Start tuning hyperparameters for YOLOv8n training on the COCO8 dataset
result_model = model.train(data=r"C:\Users\User\Desktop\Python\RayCluster\pythonProject1\datasets/car/data.yaml",
                           epochs = 30, batch = -1, optimizer = 'auto', dropout=0, lr0= 0.001)