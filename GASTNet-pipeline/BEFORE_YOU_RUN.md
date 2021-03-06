# Before you run

This is a small and simple guide to prepare the project before running the code in this package. 

First, you need to download the models given below and place them in their respective folders. 

[YOLOv3 weights](https://drive.google.com/file/d/1AsxruW20w8zChvrnGb1wrfU1ZieKehQm/view?usp=sharing)
Location of the file after download: ./checkpoint/yolov3/yolov3.weights

[HRNet weights](https://drive.google.com/file/d/1B9SfUoNq_zHy9tp4V7_qdLru4NIiTJQP/view?usp=sharing)
Location of the file after download: ./checkpoint/hrnet/pose_coco/pose_hrnet_w48_384x288.pth

## Python plug-in for the package

Use the following Python code to run a subprocess call on the package that will create the output video file at its specified path: 

```
import sys
import subprocess

video_path = '/path/to/file.mp4'
subprocess.call([sys.executable, 'gen_skes.py', '-a', '-v', video_path])
```