#!/bin/sh 

set -x

PYTHONPATH=./:../../../python ../../../build/paddle/pserver/paddle_pserver_main \
    --use_gpu=0 \
    --num_gradient_servers=1 \
    --ports_num_for_sparse=3 \
    --ports_num=3 \
    --nics=lo0 \
