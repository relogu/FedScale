#!/bin/bash
#SBATCH --job-name=SS1
#SBATCH --cpus-per-task 11
#SBATCH -w mauao
#SBATCH --gres=gpu:a40:1

export FEDSCALE_HOME=/nfs-share/ls985/FedScale
DRIVER_SCRIPT=/nfs-share/ls985/FedScale/docker/driver.py
YAML_CONFIG=/nfs-share/ls985/FedScale/benchmark/configs/shakespeare/shakespeare-mauao-1gpu.yml
cd /nfs-share/ls985/FedScale
poetry shell

srun poetry run python $DRIVER_SCRIPT start $YAML_CONFIG
