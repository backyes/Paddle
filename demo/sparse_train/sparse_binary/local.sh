#!/bin/sh 

set -x

PYTHONPATH=./:../../../python ../../../build/paddle/trainer/paddle_trainer \
    --use_gpu=0 \
    --config=./sparse_trainer_config.py \
    --saving_period=1 \
    --test_period=0 \
    --num_passes=4 \
    --dot_period=2 \
    --log_period=20 \
    --trainer_count=2 \
    --pservers=127.0.0.1 \
    --saving_period_by_batches=5000 \
    --local=0 \
    --port=20134 \
    --ports_num_for_sparse=3 \
    --ports_num=3 \

