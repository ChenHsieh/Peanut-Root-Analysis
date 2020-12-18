## Some useful scripts

image processing using PIL, resize, enhance, rotate, pixel manipulation

DIRT cmd generator

video generator from image sequences using cv2

DIRT output processor for Momo's program

## conda_env

The conda environments required for running DIRT and Momo's clustering program

```bash
# create conda environment with yaml file 
conda env create -f file_name.yml
# activate the env, env_name is specified in the yaml file
conda activate env_name
# after some mod, use this to create your own env.yaml
conda env export > environment.yml
```

