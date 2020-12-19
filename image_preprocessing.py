from PIL import ImageEnhance, Image
import os
import pandas as pd
from os.path import join, dirname
from pathlib import Path
os.chdir('/Path/to/work/dir')

resize_factor = 0.1

def processFile(dir, file_name, shelter_num):
    for image_name in file_name.index:
        print(image_name)
        image_path = os.path.join(dir, image_name)
        image = Image.open(image_path)
        width, height = image.size
        print(image.size)
        # resize
        height = int(height*resize_factor)
        width = int(width*resize_factor)
        image = image.resize((width, height))
        # rotate image
        if width > height:
            angle = 270
            print("rotate")
            image = image.rotate(angle, expand=True)
        width, height = image.size
        print(image.size)
        # enhancement
        image = ImageEnhance.Contrast(image).enhance(0.6)
        image = ImageEnhance.Brightness(image).enhance(1.7)
        # image.show()
        # pixel manipulation
        image_data = image.load()
        for loop1 in range(width):
            for loop2 in range(height):
                r,g,b = image_data[loop1,loop2]
                # print(r)
                if b>g or b>r:
                    image_data[loop1,loop2] = 0,0,0
                elif r-b>200:
                    image_data[loop1,loop2] = 0,0,0
        new_file_name = file_name.loc[image_name].genotype + '_' + image_name
        new_file_name = new_file_name.replace(' ','_')
        new_file_name = new_file_name.replace('JPG','jpg')
        new_file_name = shelter_num + new_file_name
        image.save(new_file_name)

dir = '/path/to/img/dir
file_name = pd.read_csv('/genotype/and/img/file/name/label.csv')
file_name = file_name.set_index('image_file_name')
processFile(dir, file_name, '1')
