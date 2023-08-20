#!/bin/bash
#
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1

CONFIG = $1
WORK_DIR = $2

python -u /home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/tools/train.py $1  --work-dir=$2 --launcher="slurm"


