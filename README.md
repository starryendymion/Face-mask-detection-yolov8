# Face mask detection using YOLOv8

Requirements : Python 3  + Ultralytics  + webcam

Dataset used : https://www.kaggle.com/datasets/aditya276/face-mask-dataset-yolo-format

Intructions : To start capturing, run the file 'runmodel.py'. 
              To stop, press Q .
              Please maintain a distance of at least 1 m from the webcam for proper prediction.
              
Source code :  Dataset is NOT included in the code. Train and Val folders are empty. Note that the file paths in data_locations.yaml are absolute paths and modification
is needed in order for them to suit the user's computer.

              
              
Other Info : 

This is a CNN Model trained by using the weights of the colo128 model. [ transfer learning ]
epochs= 25 ; time taken : 45 minutes ; GPU : Nvidia RTX  3050 notebook  4 GB  [2048 CUDA cores] 


