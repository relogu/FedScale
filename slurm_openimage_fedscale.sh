#!/bin/bash
#SBATCH --cpus-per-task 11
#SBATCH -w mauao
#SBATCH --gres=gpu:a40:1
#SBATCH --job-name=fedscale_speech

export FEDSCALE_HOME=/nfs-share/ls985/FedScale
DRIVER_SCRIPT=/nfs-share/ls985/FedScale/docker/driver.py
YAML_CONFIG=/nfs-share/ls985/FedScale/benchmark/configs/openimage/openimage_mauao_1gpu.yml
cd /nfs-share/ls985/FedScale
poetry shell

srun poetry run python $DRIVER_SCRIPT start $YAML_CONFIG

# srun -w mauao -c 11 --gres=gpu:1 --partition=interactive poetry run python /nfs-share/ls985/FedScale/docker/driver.py start /nfs-share/ls985/FedScale/benchmark/configs/openimage/openimage_mauao_1gpu.yml
