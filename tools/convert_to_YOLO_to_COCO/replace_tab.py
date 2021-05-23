import os 

"""Replaces the txt file from tab to space"""
d = ['testing', 'training', 'validation']

# Get OS LIstdir
path=''
dataset = d[0]
folder = sorted(os.listdir(f'{path}{dataset}'))
i=0
# Get the txt file to write the yolo path files
for file1 in folder:
    folder2 = sorted(os.listdir(f"{path}{dataset}/{file1}"))
    #print(folder2)
    for img in folder2:
            if img.endswith(".txt"):
                 file_path = f"{path}{dataset}1/{file1}/{img}"
                 file_path2 = f"{path}{dataset}/{file1}/{img}"
                 inputFile = open(file_path, "r") 
                 exportFile = open(file_path2, "w+")
                 for line in inputFile:
                 #    print(line)
                     new_line = line.replace('\t', '')
                     print(line)
                     exportFile.write(new_line) 
             #    print(img)
                 inputFile.close()
                 exportFile.close()

