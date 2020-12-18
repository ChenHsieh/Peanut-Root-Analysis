import os 
import cv2  
from PIL import Image 
import pandas as pd
import numpy as np
from os.path import join, dirname
from pathlib import Path

# took about 1 min
os.chdir('/Work/Dir')

root_path = '/dirt/output/path'
header_list = ['IMAGE_NAME','DS10','DS20','DS30','DS40','DS50','DS60','DS70','DS80','DS90']
output = {}
for header in header_list:
    output[header] = []

original_images_name = [ name for name in os.listdir(root_path) if
          os.path.isfile(os.path.join(root_path, name)) & name.endswith('.jpg')]
img_array = []
ww = 640
hh = 480
color = (0,0,0)
fail_list = []
for id in range(1001, 1962):
    print(id)
    # image_name = original_images_name[id-1001]
    
    image_result_path = os.path.join(root_path, str(id))
    csv_path = os.path.join(image_result_path, 'output.csv')
    try:
        individual_csv = pd.read_csv(csv_path)
        image_name = individual_csv.values[0][1]
        image_name_ = image_name.replace(' ','_')
        output['IMAGE_NAME'].append(image_name.replace(' ', '_'))
        # print(output)
        output['DS10'].append(individual_csv.values[0][28])
        output['DS20'].append(individual_csv.values[0][29])
        output['DS30'].append(individual_csv.values[0][30])
        output['DS40'].append(individual_csv.values[0][31])
        output['DS50'].append(individual_csv.values[0][32])
        output['DS60'].append(individual_csv.values[0][33])
        output['DS70'].append(individual_csv.values[0][34])
        output['DS80'].append(individual_csv.values[0][35])
        output['DS90'].append(individual_csv.values[0][36])
        

        ori_image0 = f'{root_path}/resize/{image_name_}'
        ori_image1 = f'{root_path}/enhance/{image_name_}'
        img_seq1 = f'{image_result_path}/Mask/{image_name}.png'
        img_seq2 = f'{image_result_path}/Crown/{image_name}.png'
        img_seq3 = f'{image_result_path}/Crown/Skeleton/{image_name}.png_skel.png'
        img_seq4 = f'{image_result_path}/Crown/Result/{image_name}.pngSeg2.png'
        img_seq = [ ori_image0, ori_image1, img_seq1, img_seq2, img_seq3, img_seq4 ]
        for img_path in img_seq:
            # print(img_path)
            img = cv2.imread(img_path)
            height, width, layers = img.shape
            x = int((ww-width)/2)
            y = int((hh-height)/2)
            result = np.full((hh,ww,layers), color, dtype=np.uint8)
            result[y:y+height, x:x+width] = img
            img_array.append(result)
    except:
        fail_list.append(id)
        print('fail')
    print(image_name)
# output a csv file for architecture clustering
pd.DataFrame(output).to_csv('output.csv')

# write a video composed of original and 5 output images
size = (ww,hh)
#fourcc mp4v or avc1 for mac
video = cv2.VideoWriter('dirt_image_sequence.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 6, size)
 
for i in range(len(img_array)):
    video.write(img_array[i])
video.release()
print(fail_list)