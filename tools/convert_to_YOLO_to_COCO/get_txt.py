import os
import yaml

d = ['testing', 'training', 'validation']

path=''
dataset = d[0]
folder = sorted(os.listdir(f'{path}{dataset}'))
i=0
# Get the txt file to write the yolo path files
for file1 in folder:
    folder2 = sorted(os.listdir(f"{path}{dataset}/{file1}"))
    #output = open(f'{path}{dataset}1/{file1}','r')
    for img in folder2:
            if img.endswith(".txt"):
                output_list = [0]
                input1 = open(f'{path}{dataset}2/{file1}/{img}','r')
                output = open(f'{path}{dataset}/{file1}/{img}','w')
                f_list = yaml.load(input1, Loader=yaml.FullLoader)
                lp = f_list['position_plate']
                new_list = f_list['position_vehicle']
                #print(new_list)
                lp = [lp.replace(' ', ',')]
                new_list = [new_list.replace(' ', ',')]
                #print(new_list)
                lp = [x for xs in lp for x in xs.split(',')]
                new_list = [x for xs in new_list for x in xs.split(',')]
                print(f'{path}{dataset}2/{file1}/{img}')
                for num in range(0, len(new_list)):
                    #print("more")
                    #print(lp[num])
                    output_list.append(int(lp[num]))
                output.write(f"{output_list[0]} {output_list[1]} {output_list[2]} {output_list[3]} {output_list[4]}\n")
