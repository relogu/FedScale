#!/bin/bash
#SBATCH --job-name=SO1-scale
#SBATCH --cpus-per-task 11
#SBATCH -w mauao
#SBATCH --gres=gpu:a40:1
#SBATCH --output=%x-%j.out
#!SBATCH --dependency=afterany:77817

export FEDSCALE_HOME=/nfs-share/ls985/FedScale
DRIVER_SCRIPT=/nfs-share/ls985/FedScale/docker/driver.py
YAML_CONFIG_1000=/nfs-share/ls985/FedScale/benchmark/configs/openimage/openimage-mauao-1gpu-scale1000.yml
YAML_CONFIG_10000=/nfs-share/ls985/FedScale/benchmark/configs/openimage/openimage-mauao-1gpu-scale10000.yml
cd /nfs-share/ls985/FedScale
poetry shell

srun poetry run python $DRIVER_SCRIPT start $YAML_CONFIG_1000

sleep 30

srun poetry run python $DRIVER_SCRIPT start $YAML_CONFIG_10000
