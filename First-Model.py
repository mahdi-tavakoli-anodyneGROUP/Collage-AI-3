#Create Directory
import os
HOME = os.getcwd()
print(HOME)


#Install YOLOv8
# Pip install method (recommended)

!pip install ultralytics==8.2.103 -q

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()


from ultralytics import YOLO

from IPython.display import display, Image

#Create datasets file
!mkdir -p {HOME}/datasets
%cd {HOME}/datasets


#Install roboflow and download datasets
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="BhJ63IemG3ACRXXxUyzC")
project = rf.workspace("dental-decay").project("check-hfbzl-zemwx")
version = project.version(13)
dataset = version.download("yolov8")


import yaml

with open(f"{dataset.location}/data.yaml", 'r') as f:
    dataset_yaml = yaml.safe_load(f)
dataset_yaml["train"] = "../train/images"
dataset_yaml["val"] = "../valid/images"
dataset_yaml["test"] = "../test/images"
with open(f"{dataset.location}/data.yaml", 'w') as f:
    yaml.dump(dataset_yaml, f)


#Training Model

    %cd {HOME}

    !yolo task = segment mode = train model = yolov8s-seg.pt data = {dataset.location}/data.yaml epochs = 10 imgsz = 640

#Visualize Confusion Matrix
%cd {HOME}
Image(filename=f'{HOME}/runs/segment/train/confusion_matrix.png', width=600)

#Visualize Plots
%cd {HOME}
Image(filename=f'{HOME}/runs/segment/train/results.png', width=600)

#Visualize Validation
%cd {HOME}
Image(filename=f'{HOME}/runs/segment/train/val_batch0_pred.jpg', width=600)

#Validate custom model
%cd {HOME}

!yolo task=segment mode=val model={HOME}/runs/segment/train/weights/best.pt data={dataset.location}/data.yaml

#Inference custom model
%cd {HOME}
!yolo task=segment mode=predict model={HOME}/runs/segment/train/weights/best.pt conf=0.25 source={dataset.location}/test/images save=true


#Show prediction images
import glob
from IPython.display import Image, display

for image_path in glob.glob(f'{HOME}/runs/segment/predict2/*.jpg')[:3]:
      display(Image(filename=image_path, height=600))
      print("\n")
