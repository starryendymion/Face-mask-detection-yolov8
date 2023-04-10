from ultralytics import YOLO
import os

absolute_path = os.path.dirname(__file__)
relative_path = "trained_mask_model.pt"
full_path = os.path.join(absolute_path, relative_path)

model=YOLO(full_path)

model.predict(source=0,show=True)