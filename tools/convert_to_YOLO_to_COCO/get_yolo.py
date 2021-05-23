import os

d = ['testing', 'training', 'validation']

# Get OS LIstdir
path=''
dataset = d[2]
folder = sorted(os.listdir(f'{path}{dataset}'))
i=0
# Get the txt file to write the yolo path files
for file1 in folder:
    folder2 = sorted(os.listdir(f"{path}{dataset}/{file1}"))
    with open('/home/yviel/yolo_v/yolo.txt','a') as f:
        for img in folder2:
            if img.endswith(".png"):
                f.write(f"{path}{dataset}/{file1}/{img}\n")
