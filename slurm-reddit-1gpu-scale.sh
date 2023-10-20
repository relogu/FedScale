#!/bin/bash
#SBATCH --job-name=SR1-scale
#SBATCH --cpus-per-task 11
#SBATCH -w mauao
#SBATCH --output=%x-%j.out
#SBATCH --gres=gpu:a40:1

export FEDSCALE_HOME=/nfs-share/ls985/FedScale
DRIVER_SCRIPT=/nfs-share/ls985/FedScale/docker/driver.py
YAML_CONFIG_1000=/nfs-share/ls985/FedScale/benchmark/configs/reddit/reddit-mauao-1gpu-scale1000.yml
YAML_CONFIG_10000=/nfs-share/ls985/FedScale/benchmark/configs/reddit/reddit-mauao-1gpu-scale10000.yml
cd /nfs-share/ls985/FedScale
poetry shell

srun poetry run python $DRIVER_SCRIPT start $YAML_CONFIG_1000

sleep 30

srun poetry run python $DRIVER_SCRIPT start $YAML_CONFIG_10000
