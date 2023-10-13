#!/bin/bash
#SBATCH --job-name=SO13
#SBATCH --nodelist=ngongotaha,mauao
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:3
#SBATCH --cpus-per-task=24

export FEDSCALE_HOME=/nfs-share/ls985/FedScale
DRIVER_SCRIPT=/nfs-share/ls985/FedScale/docker/driver_slurm_multinode.py
YAML_CONFIG=/nfs-share/ls985/FedScale/benchmark/configs/openimage/openimage-multi-1+3.yml
cd /nfs-share/ls985/FedScale
poetry shell

#! NOTE: Forcing the head node to be the current node
#! that will be used for executing the simulation script
this_hostname=$(hostname)
echo "STARTING HEAD at $this_hostname"
srun --nodes=1 --ntasks=1 -w "$this_hostname" \
    poetry run python $DRIVER_SCRIPT start $YAML_CONFIG 0 &

sleep 10

# Getting the node names
nodes=$(scontrol show hostnames "$SLURM_JOB_NODELIST")
nodes_array=($nodes)
# Number of total nodes minus 1
num_nodes=$((SLURM_JOB_NUM_NODES - 1))
# Launching one worker per node that is different from the head node
cnt=1
for ((i = 0; i <= num_nodes; i++)); do
    node_i=${nodes_array[$i]}
    if [ "$node_i" != "$this_hostname" ]; then
        echo "Starting WORKER $i at $node_i"
        srun --nodes=1 --ntasks=1 -w "$node_i" \
            poetry run python $DRIVER_SCRIPT start $YAML_CONFIG $cnt
        cnt+=1
    fi
done
