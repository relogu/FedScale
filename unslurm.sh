#!/bin/bash
#SBATCH --cpus-per-task 44
#SBATCH -w mauao
#SBATCH --gres=gpu:a40:4
#SBATCH --job-name=fedscale_gspeech

source /nfs-share/ls985/anaconda3/bin/activate fedscale-11
export FEDSCALE_HOME=/nfs-share/ls985/FedScale
cd $FEDSCALE_HOME

srun python $FEDSCALE_HOME/docker/driver.py start $FEDSCALE_HOME/benchmark/configs/speech/google_speech_mauao_16w4g.yml
