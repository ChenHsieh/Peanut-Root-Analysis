# This py script will output dirt execution script to terminal
# python dirt_cmd_generator.py > run.sh

import os
from os.path import join, dirname
from pathlib import Path

dir = 'Path/to/your/image'

images = [os.path.join(dir, name) for name in os.listdir(dir) if
          os.path.isfile(os.path.join(dir, name)) & name.endswith('.jpg')]
#print(len(images))

id = 1001
for image_file_path in images:
    print(f'python /dirt/main.py "{image_file_path}" {id} 6.0 0 1 1 0 1 0 1 /Path/to/work/space /dirt/rep/traits.csv')
    id += 1 
