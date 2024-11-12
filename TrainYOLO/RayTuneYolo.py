from ultralytics import YOLO
from ray import tune
import ray

ray.init(address="ray://127.0.0.1:10001")

# Define a YOLO model
model = YOLO("yolo11n.pt")

# Run Ray Tune on the model
result_grid = model.tune(
    data=r"C:\Users\User\Desktop\Python\RayCluster\pythonProject1\datasets/car/data.yaml",
    space={"lr0": tune.uniform(1e-5, 1e-1)},
    epochs=30,
    use_ray=True,
)