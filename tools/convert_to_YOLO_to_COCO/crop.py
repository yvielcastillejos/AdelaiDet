import os
import yaml
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
d = ['testing', 'training', 'validation']

path=''
dataset = d[2]
folder = sorted(os.listdir(f'{path}{dataset}'))
i=0
# Get the txt file to write the yolo path files
for file1 in folder:
    folder2 = sorted(os.listdir(f"{path}{dataset}/{file1}"))
    #output = open(f'{path}{dataset}1/{file1}','r')
    for img in folder2:
            if img.endswith(".png"):
                output_list = [0]
                input1 = open(f'{path}{dataset}2/{file1}/{img[:-4]}.txt','r')
                f_list = yaml.load(input1, Loader=yaml.FullLoader)
                new_list = f_list['position_vehicle']
                new_list = [new_list.replace(' ', ',')]
                new_list = [x for xs in new_list for x in xs.split(',')]
                print(f'{path}{dataset}2/{file1}/{img}')
                for num in range(0, len(new_list)):
                    #print("more")
                    #print(lp[num])
                    output_list.append(int(new_list[num]))
                img3 = plt.imread(f'{path}{dataset}2/{file1}/{img}')
                #print(f'{output_list[1]}:{output_list[1]+output_list[3]}')
                img3 = img3[ output_list[2]:output_list[2]+output_list[4], output_list[1]:output_list[1]+output_list[3], :]
                #print(type(img3))

                #pts = np.array([[output_list[1],output_list[2]],[output_list[1]+output_list[3], output_list[2]+output_list[4]]])
                #plt.imshow(img3)
                #plt.scatter(pts[:, 0], pts[:, 1], marker="x", color="red", s=200)
                #plt.show()
                #im = Image.fromarray(img3)
                matplotlib.image.imsave(f'/home/yviel/datasets/UPFR-ALPR dataset (cropped)/{dataset}/{img}', img3)
