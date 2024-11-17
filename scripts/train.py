from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo11x-cls.pt")

# Train the model
results = model.train(data="dataset", epochs=100, imgsz=200, batch=128, device=0)
